# Scraper to scrape some information from a Github repository (website and cloned repo)
# From Github:
# Description
# Issues
# Pull requests

# From Cloned Repo:
# .markdown files
# in-line comments

from shutil import rmtree
import os, sys

import bs4 as soup
import requests

from myutils import onerror, choose_subset, run_proc, clone, slurp, write_as_bytes

code_extensions = ['cpp','c','cxx','py','sh','js']
comment_starters = ['//','#']
to_clean = ['.','/','-']

comment_merge_distance = 5
max_issues = 20
max_inline = 20
max_markdown = 20

def parse_inline(qualified):
    with open(qualified, 'r') as g:
        try:
            lines = g.readlines()
        except:
            print("can't read {}, skipping".format(qualified))
            lines = []

        comments = []
        for i,line in enumerate(lines):
            stripped = line.lstrip()

            for cs in comment_starters:
                if stripped.startswith(cs):
                    if len(comments) and comments[-1][1] > i-comment_merge_distance:
                        stop = min(i+comment_merge_distance,len(lines))
                        comments[-1] = (comments[-1][0], stop)
                    else:
                        start = max(i-comment_merge_distance,0)
                        stop = min(i+comment_merge_distance,len(lines))
                        comments += [(start, stop)]
                    break

        merged = []
        for comment in comments:
            merged += ['### Line ',str(comment[0]+1),'-',str(comment[1]),'\n']
            merged += ['```\n']
            for i in range(comment[0],comment[1]):
                if len(line.strip()) == 0:
                    continue
                line = line.replace('```',"'''")
                merged += [lines[i]]
            merged += ['\n```\n']
        merged = ''.join(merged)
        return merged

def parse_markdown(qualified):
    b = None
    with open(qualified, 'rb') as g:
        b = g.read()

    b = b.replace(b'```', b"'''")
    return b'```' + b + b'```'

def extract_from_repo(repo, out):
    candidates = {"markdown": [], "inline": []}
    _extract_from_repo(repo, candidates, path='/.')

    inline_ = choose_subset(max_inline, len(candidates["inline"]))
    markdown_ = choose_subset(max_markdown, len(candidates["markdown"]))

    for i in inline_:
        npath = candidates["inline"][i]
        print('Scraping',npath)
        qualified = repo + npath
        extension = npath.split('.')[-1]

        cleaned_path = npath
        for symbol in to_clean:
            cleaned_path = '_'.join(cleaned_path.split(symbol))
        while '__' in cleaned_path:
            cleaned_path = cleaned_path.replace('__', '_')

        merged = parse_inline(qualified)
        out["inline"][cleaned_path] = merged

    for i in markdown_:
        npath = candidates["markdown"][i]
        print('Scraping',npath)
        qualified = repo + npath
        extension = npath.split('.')[-1]

        cleaned_path = npath
        for symbol in to_clean:
            cleaned_path = '_'.join(cleaned_path.split(symbol))
        while '__' in cleaned_path:
            cleaned_path = cleaned_path.replace('__', '_')

        merged = parse_markdown(qualified)
        out["markdown"][cleaned_path] = merged

def _extract_from_repo(repo, out, path='/.'):
    for f in os.listdir(repo + path):
        npath = path + '/' + f
        qualified = repo + npath
        extension = f.split('.')[-1]

        if os.path.isdir(qualified):
            _extract_from_repo(repo, out, npath)
        elif extension == 'md':
            out["markdown"] += [npath]
        elif extension in code_extensions:
            out["inline"] += [npath]

def count_issues(url):
    max_jump = 65536
    guess = 0
    while max_jump:
        nguess = guess + max_jump
        page = requests.get(url + str(nguess))
        if page.status_code is 200:
            guess = nguess
        max_jump = max_jump // 2
    return guess

def extract_from_url(url, out):
    souped = slurp(url)[0]

    desc = souped.find('span', {'itemprop': 'about'}).getText()
    out["info"]["description"] = desc.strip() + '\n'

    issue_count = count_issues(url + '/issues/')
    to_scrape = choose_subset(max_issues, issue_count)

    for target in to_scrape:
        target_url = url + '/issues/' + str(target + 1)
        page,target_url = slurp(target_url)

        if type(page) is not soup.BeautifulSoup:
            print(target_url,', status_code =',page,', skipping.')
            continue
        print('Scraping',target_url)

        issue_type = target_url.split('/')[-2]

        merged = []
        title = page.find('span', {'class': 'js-issue-title'}).getText()
        merged += ['Title:\n```\n', title, '\n```\n']

        comments = page.find_all('div', {'class': 'timeline-comment-group'})
        for comment in comments:
            author = comment.find('a', {'class': 'author'}).getText()
            text = comment.find('td', {'class': 'comment-body'}).getText()

            merged += ['Author:\n```\n',
                       author,
                       '\n```\n',
                       'Text:\n```\n',
                       text,
                       '\n```\n']

        merged = ''.join(merged)
        out[issue_type][str(target+1)] = merged

def write_summary(title, extracted, out):
    with open(out, 'wb') as f:
        write_as_bytes(f, '# ' + title + '\n')
        for heading in extracted:
            heading_adj = heading.capitalize()
            write_as_bytes(f, '[- {}](#{})\n\n'.format(heading_adj, heading_adj))
            for path in extracted[heading]:
                path_ = path.split('/')[-1]
                write_as_bytes(f, '* [{}](#{})\n\n'.format(path_, path))

        write_as_bytes(f, '<!-- toc -->\n\n')
        for heading in extracted:
            heading_adj = heading.capitalize()
            write_as_bytes(f, '# ' + str(heading_adj) + '\n')
            for path in extracted[heading]:
                write_as_bytes(f, '## ' + str(path) + '\n')

                to_write = extracted[heading][path]
                if type(to_write) is str:
                    f.write(extracted[heading][path].encode())
                else:
                    f.write(extracted[heading][path])

                write_as_bytes(f, '\n')

def go(url, out_file):
    repo = './repo'
    rmtree(repo, onerror=onerror)
    clone(url, repo)

    extracted = {"info": {}, "markdown": {}, "inline": {}, "issues": {}, "pull": {}}
    extract_from_repo(repo, extracted)
    extract_from_url(url, extracted)

    write_summary('/'.join(url.split('/')[-2:]), extracted, out_file)

if __name__ == '__main__':
    repo_list = 'repos.txt' if len(sys.argv) < 2 else sys.argv[1]
    with open(repo_list, 'r') as f:
        while True:
            line = f.readline()
            if line.strip() == 'END':
                break

            url = line.split(',')[1].strip()
            name = url.split('/')[-1]
            print('repo:',name)
            go(url, name + '.md')
