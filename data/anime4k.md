# bloc97/anime4k
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_CODE_OF_CONDUCT_md](#_CODE_OF_CONDUCT_md)

* [_FAQ_Detail_md](#_FAQ_Detail_md)

* [_Java_Instructions_md](#_Java_Instructions_md)

* [_github_ISSUE_TEMPLATE_bug_report_md](#_github_ISSUE_TEMPLATE_bug_report_md)

* [_GLSL_Instructions_md](#_GLSL_Instructions_md)

* [_README_md](#_README_md)

* [_Preprint_md](#_Preprint_md)

* [_Upscaling_md](#_Upscaling_md)

* [_github_ISSUE_TEMPLATE_feature_request_md](#_github_ISSUE_TEMPLATE_feature_request_md)

* [_HLSL_Instructions_md](#_HLSL_Instructions_md)

[- Inline](#Inline)

* [_web_main_js](#_web_main_js)

* [_hlsl_Anime4K_Push_Weak_hlsl](#_hlsl_Anime4K_Push_Weak_hlsl)

* [_java_build_sh](#_java_build_sh)

* [_glsl_Anime4K_Adaptive_v0_9_glsl](#_glsl_Anime4K_Adaptive_v0_9_glsl)

* [_hlsl_Anime4K_ComputeGradient_hlsl](#_hlsl_Anime4K_ComputeGradient_hlsl)

* [_hlsl_Anime4K_PushGrad_Weak_hlsl](#_hlsl_Anime4K_PushGrad_Weak_hlsl)

* [_glsl_Anime4K_Adaptive_v1_0RC_glsl](#_glsl_Anime4K_Adaptive_v1_0RC_glsl)

* [_java_src_main_java_com_bloc97_anime4k_ImageKernel_java](#_java_src_main_java_com_bloc97_anime4k_ImageKernel_java)

* [_hlsl_Anime4K_Push_hlsl](#_hlsl_Anime4K_Push_hlsl)

* [_hlsl_Anime4K_ComputeLum_hlsl](#_hlsl_Anime4K_ComputeLum_hlsl)

* [_glsl_Anime4K_Adaptive_v1_0RC2_glsl](#_glsl_Anime4K_Adaptive_v1_0RC2_glsl)

* [_hlsl_Anime4K_PushGrad_hlsl](#_hlsl_Anime4K_PushGrad_hlsl)

* [_glsl_Anime4K_Adaptive_v1_0RC2_Fast_glsl](#_glsl_Anime4K_Adaptive_v1_0RC2_Fast_glsl)

* [_java_src_main_java_com_bloc97_anime4k_Main_java](#_java_src_main_java_com_bloc97_anime4k_Main_java)

* [_glsl_Anime4K_Adaptive_v1_0RC2_UltraFast_glsl](#_glsl_Anime4K_Adaptive_v1_0RC2_UltraFast_glsl)

[- Issues](#Issues)

* [5](#5)

* [31](#31)

* [19](#19)

* [26](#26)

* [12](#12)

* [8](#8)

* [49](#49)

* [18](#18)

* [16](#16)

* [29](#29)

* [47](#47)

* [11](#11)

[- Pull](#Pull)

* [37](#37)

* [48](#48)

* [38](#38)

* [42](#42)

* [15](#15)

* [22](#22)

* [14](#14)

* [13](#13)

<!-- toc -->

# Info
## description
A High-Quality Real Time Upscaler for Anime Video

# Markdown
## _CODE_OF_CONDUCT_md
```# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at anime4k.upscale@gmail.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
```
## _FAQ_Detail_md
```
## Why not do PSNR/SSIM on 480p->720p upscaling

I get this question a lot, and let me clarify things. Usually when I try to demonstrate a point I try to do it in the extreme, so that the reasoning becomes very clear.

Let's say in another hypothetical world (lets call it PixLand) all anime are just diagonal lines on a 2x2 image. So there are only two possible anime pictures possible in that world. Lets also say that in this world, all images are binary, no grayscale.

![Demo 0](results/Demo/TwoAnimes.png?raw=true)

The people inhabiting PixLand, called Pixels, have never seen 4x4 anime, but they do know what 4x4 images look like, they've seen them in drawings, manga and the sort.

One day, a few clever pixels publish an algorithm Diagonal4K. It is a very simple algorithm. It checks if the top left corner of the 2x2 anime is black, if so, produce a 4x4 image with a diagonal line running from the top left to bottom right. If the top left corner of the 2x2 anime is white, produce a 4x4 image with a diagonal line running from the top right to bottom left.

![Demo 1](results/Demo/DiagonalUpscale.png?raw=true)

Most people are amazed, they've never seen such clarity in anime before! It has only been seen in 4x4 manga and 4x4 drawings. But, a few are skeptical (in a good way).

> *"The lines are too long..."*

One skeptic says out loud.

> *"This is nonsense! A diagonal 2x2 line upscaled must be curvy, it can't be straight!"*

Another commented on Pixddit.

They might be right, or wrong, we will never know. In fact it is impossible to know since 4x4 anime doesn't exist in their world, nor can we comprehend them as outsiders.

We might look at the Pixels inhabiting PixLand in pity, but since each have their own preferences, we're not here to judge.

Thus, to assess its true effectiveness with a metric, a few Pixels had the genius idea to downscale 2x2 anime into a single pixel and apply the algorithm to see if it produces 2x2 anime correctly.

**As you've certainly realized, upscaling 1x1 anime into 2x2 with Diagonal2K does not make sense at all, and is not a good indicator of quality. There is no way the algorithm will recover the 2x2 anime with a single pixel.**

Let's also say that in their world, downscaling is always done using the Nearest-Neighbour algorithm.

Due to the small brains of Pixels, the authors of Diagonal4K do not realize that if the 1x1 image is black, it must be Anime 1, and if it were to be be white instead, Anime 2.

But 4 years prior, another group of smart pixels used the power of machine learning to augment their small brains. Their algorithm sexyCircle2x, a pixel-network, learnt that 1x1 black image is Anime 1, and 1x1 white is Anime 2. It learnt the distribution of Animes, and correctly guesses what anime corresponds to what pixel color.

People were dumbfounded. "Wow! It can basically generate anime!" "Incredible! Details out of thin air!" "Garbage In, Awesomeness out!"

Back to the present, those Pixels dug out sexyCircle2x and begun their comparison. The pixel-network upscales 1x1 -> 2x2 correctly, while Diagonal4K does not. Thus they concluded that Diagonal4K must be inferior.

![Demo 1](results/Demo/1x1-2x2.png?raw=true)

Applying sexyCircle2x to 2x2 anime also yields plausible 4x4 "anime", but they do not and will never know if it is truly anime. However they trust the algorithm enough since it is a pixel-network, and must be smarter than their small Pixel brains.  

So the results are:  
sexyCircle2x correctly upscales 1x1 -> 2x2  
sexyCircle2x upscales 2x2 -> 4x4, but some people do not like its output, as it always produces an X pattern. However most people accept its quality as the X pattern is a pleasing pattern to look at.

While:  
Diagonal4K fails on 1x1 -> 2x2  
Diagonal4K upscales 2x2 -> 4x4 and preserves the line straightness, but some Pixels fervently dislike straight lines.

![Demo 1](results/Demo/2x2-4x4.png?raw=true)

**Thus the question is: Is Diagonal4K an inferior algorithm compared sexyCircle2x?**

I think this question is nonsensical! It is impossible to even tell which algorithm is best at upscaling 2x2 to 4x4.

Of course, this example is very extreme, but the same principles applies here.

Comparing PSNR/SSIM on 480p->720p upscales and then claiming that it is a good indicator of 1080p->2160p upscaling quality does not make sense. 480p images have a lot of high frequency information (lines might be thinner than 1 pixel), while 1080p images have a lot of redundant information. 1080p->2160p upscaling on anime is thus objectively easier than 480p->720p.

Only each individual can really judge for themselves (not for others) if our algorithm is good or not.

Some people prefer sharp lines and don't really mind the pastel painting look that Anime4K sometime produces, while some will certainly despise sharp lines and the pastel look. We're not here to judge the individual, so please do not judge others' taste and keep it civil.
```
## _Java_Instructions_md
```
# Usage Instructions (Java)

1- Install Java JDK 12.  
2- Build the jar with the maven source project using the appropriate cmd/shell script.  
3- Run as administrator this command `java -jar Anime4K.jar input.png output.png` for 2x scale  

Available parameters:  
`java -jar Anime4K.jar [File_In] [File_Out] (Scale) (Push_Grad_Strength) (Push_Strength)`  

Default Scale: `2`  
Default Push_Grad_Strength: `Scale / 2`  
Default Push_Strength: `Scale / 6`  

Examples:  
`java -jar Anime4K.jar test.png test_upscaled.png 4`  
`java -jar Anime4K.jar test.png test_upscaled.png 2 0.6 0`  
`java -jar Anime4K.jar test.png test_upscaled.png 3 1 1`    

Note to developers:
For faster batch processing please look at Main.java and modify the code so that the Kernel is not re-created for each picture. (Kernel reuse will accelerate processing greatly.)
```
## _github_ISSUE_TEMPLATE_bug_report_md
```---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Windows 10]
 - Version [e.g. 0.9]
 - Media Player (If applicable) [e.g. MPC-BE, MPV]
 - Browser (If applicable) [e.g. chrome, safari]

**Additional context**
Add any other context about the problem here.
```
## _GLSL_Instructions_md
```
# Usage Instructions (GLSL / MPV)
*If you wish to use another media player, look at their documentation on how to install GLSL shaders and modify the shader accordingly if needed.*

1- Install [**mpv**](https://mpv.io/)  
2- Download the .glsl shader files [**here**](https://github.com/bloc97/Anime4K/releases)  
3- Copy the .glsl files to `%AppData%\mpv\shaders` for Windows or `~/.config/mpv/shaders` for Linux.  
4- If `mpv.conf` does not exist in `%AppData%\mpv\` or `~/.config/mpv`, create an empty file and follow [**these instructions**](https://wiki.archlinux.org/index.php/Mpv#Configuration) to optimize your configuration.  
5- Add this line to `mpv.conf` to enable the shaders: `glsl-shaders="~~/shaders/Anime4K_Adaptive.glsl"`  

*Unlike HLSL, the GLSL shader can auto-detect the scaling factor and adjust its strength accordingly.*  
```
## _README_md
```# Anime4K

Anime4K is a state-of-the-art*, open-source, high-quality real-time anime upscaling algorithm that can be implemented in any programming language.

![Thumbnail Image](results/Main.png?raw=true)

*\*State of the art as of August 2019 in the real-time anime 4K upscaling category, the fastest at achieving reasonable quality. We do not claim this is a superior quality general purpose SISR algorithm compared to machine learning approaches.*

***Disclaimer: All art assets used are for demonstration and educational purposes. All rights are reserved to their original owners. If you (as a person or a company) own the art and do not wish it to be associated with this project, please contact us at 	anime4k.upscale@gmail.com and we will gladly take it down.***

![Comparison](results/Comparisons/1_time.png?raw=true)

## Notice

We understand that this algorithm is far from perfect, and are working towards a hybrid approach (using Machine Learning) to improve Anime4K. 

The greatest difficulties encountered right now are caused by these issues that other media does not suffer from:

 - Lack of ground truth (No True 4K Anime)
 - Few true 1080p anime (Even some anime mastered at 1080p have sprites that were downsampled)
 - Non-1080p anime are upsampled to 1080p using simple algorithms, resulting in a blurry 1080p image. Our algorithm has to detect this. (Main reason why waifu2x does not work well on anime)
 - UV channels of anime are subsampled (4:2:0), which means the color channels of 1080p anime are in fact 540p, thus there is a lack of 1080p ground truth for the UV channels.
 - Simulating H.264/H.265 compression artifacts (for analysis and denoising) is not trivial and is relatively time-consuming.
 - Due to the workflow of animation studios and their lack of time/budget, resampling artifacts of individual sprites are present in many modern anime.
 - Speed (preferably real-time) is paramount, since we do not want to re-encode video each time the algorithm improves. There is also less risk of permanently altering original content.
 - So on...

However, we still believe by shrinking the size of VDSR or FSRCNN and using an hybrid approach we can achieve good results.  
Stay tuned for more info!
 

## v1.0 Release Candidate 2

Improved speed.

Performance is back on par with v0.9 Beta, but without any loss in quality. (3ms on RX Vega 64)

Two more versions are included for less powerful GPUs.  
 - Anime4K_Fast (1.5ms)  
 - Anime4K_UltraFast (1ms) (For potato PCs)

## v1.0 Release Candidate

Reduced texture loss, aliasing and banding in Anime4K v1.0 RC at the cost of performance. It now takes 6ms. +2ms for line detection and +1ms for line targeted FXAA.

What's new:
 - A line detection algorithm.
 - Gradient maximization is only applied near lines using the line detector, instead of indiscriminately affecting the entire image. This has the effect of ignoring textures and out of focus elements.
  - Finally, one iteration of targeted FXAA is applied on the lines using the line detector to reduce aliasing.

![ComparisonRC](https://raw.githubusercontent.com/bloc97/Anime4K/master/results/Comparisons/0.9-1.0/0_RC.png)
![ComparisonRC](https://raw.githubusercontent.com/bloc97/Anime4K/master/results/Comparisons/0.9-1.0/1_RC.png)
![ComparisonRC](https://raw.githubusercontent.com/bloc97/Anime4K/master/results/Comparisons/0.9-1.0/2_RC.png)
![ComparisonRC](https://raw.githubusercontent.com/bloc97/Anime4K/master/results/Comparisons/0.9-1.0/3_RC.png)

## HLSL Usage Instructions (MPC-BE with madVR)

This implementation is **only for Windows**.

### [HLSL Installation](HLSL_Instructions.md)  

Note for developers: For performance, the HLSL shaders use the Alpha channel to store the gradient. You might need to make a backup of the alpha channel before applying these shaders and restore it after if your rendering engine uses the alpha channel for other purposes. (In MPC-BE's case, it gets ignored.)

## GLSL Usage Instructions (MPV)

This implementation is **cross platform**.

### [GLSL Installation](GLSL_Instructions.md)

Note for developers: For performance, the GLSL shaders use the `POSTKERNEL` texture to store the gradient. You might need to make a backup of the `POSTKERNEL` texture before applying these shaders and restore it after if your other shaders or rendering engine uses the `POSTKERNEL` texture for other purposes. (In MPV's case, it gets ignored.)

## Java Usage Instructions (Standalone)

### [Java Installation](Java_Instructions.md)

Click on the link above to read Java version installation and usage instructions.

## Projects that use Anime4K
 - https://github.com/yeataro/TD-Anime4K (Anime4K for TouchDesigner)
 - https://github.com/keijiro/UnityAnime4K (Anime4K for Unity)
 - https://github.com/net2cn/Anime4KSharp (Anime4K Re-Implemented in C#)
 - https://github.com/k4yt3x/video2x (Anime Video Upscaling Pipeline)


## Pseudo-Preprint Preview

### [Read Full Pseudo-Preprint](Preprint.md)

B. Peng  
August 2019

*Ad perpetuam memoriam of all who perished in the Kyoto Animation arson attack.*

### Table of Contents

- [Abstract](Preprint.md#abstract)  
- [Introduction](Preprint.md#introduction)  
- [Proposed Method](Preprint.md#proposed-method)  
- [Results and Upscale Examples](Preprint.md#results)  
- [Discussion](Preprint.md#discussion)  
- [Analysis and Comparison to Other Algorithms](Preprint.md#analysis)  

### Abstract

We present a state-of-the-art high-quality real-time SISR algorithm designed to work with Japanese animation and cartoons that is extremely fast *(~3ms with Vega 64 GPU)*, temporally coherent, simple to implement *(~100 lines of code)*, yet very effective. We find it surprising that this method is not currently used 'en masse', since the intuition leading us to this algorithm is very straightforward.  
Remarkably, the proposed method does not use any machine-learning or statistical approach, and is tailored to content that puts importance to well defined lines/edges while tolerates a sacrifice of the finer textures. The proposed algorithm can be quickly described as an iterative algorithm that treats color information as a heightmap and 'pushes' pixels towards probable edges using gradient-ascent. This is very likely what learning-based approaches are already doing under the hood (eg. VDSR<sup>**[1]**</sup>, waifu2x<sup>**[2]**</sup>).

## FAQ

### Why not just use waifu2x

waifu2x is too slow for real time applications.

### Why not just use madVR with NGU

NGU is proprietary, this algorithm is licensed under MIT.

### How does FSRCNNX compare to this

Since it performs poorly (perceptually, for anime) compared to other algorithms, it was left out of our visual comparisons.

![ComparisonRC](https://raw.githubusercontent.com/bloc97/Anime4K/master/results/Comparisons/FSRCNNX.png)

*Note: FSRCNNX was not specifically trained/designed for anime. It is however a good general-purpose SISR algorithm for video.*

### Where are the PSNR/SSIM metrics

There are no ground truths of 4K anime.

### Why not do PSNR/SSIM on 480p->720p upscaling

[Story Time](FAQ_Detail.md)

Comparing PSNR/SSIM on 480p->720p upscales does not prove and is not a good indicator of 1080p->2160p upscaling quality. (Eg. poor performance of waifu2x on 1080p anime) 480p anime images have a lot of high frequency information (lines might be thinner than 1 pixel), while 1080p anime images have a lot of redundant information. 1080p->2160p upscaling on anime is thus objectively easier than 480p->720p.

### I think the results are worse than \<x>

Surely some people like sharper edges, some like softer ones. Do try it yourself on a few anime before reaching a definite conclusion. People *tend* to prefer sharper edges. Also, seeing the comparisons on a 1080p screen is not representative of the final results on a 4K screen, the pixel density and sharpness of the final image is simply not comparable.

### Note for those who think this is not a 'upscaling' algorithm.

[Explanation](Upscaling.md)

TL;DR

Sharpening, De-Blurring and Super-Resolution are equivalent.  
Anime4K can de-blur, and is equivalent to a SR algorithm.  
A Super-Resolution algorithm can do upscaling.  
Thus, Anime4K is an upscaling algorithm.
```
## _Preprint_md
```

# Psudo-Preprint 

B. Peng  
August 2019  

*Ad perpetuam memoriam of all who perished in the Kyoto Animation arson attack.*  

## Table of Contents

[Abstract](#abstract)  
[Introduction](#introduction)  
[Proposed Method](#proposed-method)  
[Results and Upscale Examples](#results)  
[Discussion](#discussion)  
[Analysis and Comparison to Other Algorithms](#analysis)  


## Abstract
We present a state-of-the-art high-quality real-time SISR algorithm designed to work with japanese animation and cartoons that is extremely fast *(~3ms with Vega 64 GPU)*, temporally coherent, simple to implement *(~100 lines of code)*, yet very effective. We find it surprising that this method is not currently used 'en masse', since the intuition leading us to this algorithm is very straightforward.  

Remarkably, the proposed method does not use any machine-learning or statistical approach, and is tailored to content that puts importance to well defined lines/edges while tolerates a sacrifice of the finer textures. The proposed algorithm can be quickly described as an iterative algorithm that treats color information as a heightmap and 'pushes' pixels towards probable edges using gradient-ascent. This is very likely what learning-based approaches are already doing under the hood (eg. VDSR<sup>**[1]**</sup>, waifu2x<sup>**[2]**</sup>).


## Introduction
Our primary motivation is to upscale 1080p anime content for 4K screens. Current upscaling algorithms<sup>**[4]**</sup> are unsuited for real-time anime upscaling due to numerous factors.  

Using existing kernel algorithms alone such as Bicubic or xBR<sup>**[5]**</sup> produces unsatisfactory results when applied to anime, they were designed for other content in mind and tend to soften edges, which is unacceptable for anime.  

Using traditionnal 'unblurring' or 'sharpening' techniques causes overshoot<sup>**[3]**</sup> to appear near edges, which distracts the viewer and reduces the perceptual quality of the picture.  

Learning-based approaches (such as waifu2x, VDSR, EDSR, etc.) are a few orders of magnitude too slow for real-time (<30ms) applications, especially at UHD resolutions.

To further complicate the issue, 1080p anime is often not true 1080p. They are usually mastered in the studio at around 900p, then upscaled to 1080p for the final product. Some exceptions include blu-ray masters of full-length animation films.

### Existing algorithms
As a general rule, an image can be decomposed into two parts, its low frequency components ***LR_U*** and a high frequency residual ***r***.

![Image Decomposition](results/Image_Decomposition.png?raw=true)

Intuitively, single image super-resolution is defined as recovering high-frequency residuals ***r*** using the low frequency data ***LR_U*** (the blurry, low resolution image).  
Common edge refinement algorithms such as unsharp masking<sup>**[6]**</sup> take the low resolution image, extract the low resolution image's residual by computing the difference between the low resolution image with a even lower resolution of that image, then it thins and sharpens that residual to finally add it to **LR_U**. This method creates ringing and overshoot commonly seen on existing sharpening algorithms. We need something better that does not distract the viewer.  

Learning-based algorithms take in **LR_U** and try to predict the residual ***r*** with a neural network, a sparse dictionary or look for self similarity in the image. Unfortunately learning based methods are for now too slow for real-time applications, but we cannot ignore their effectiveness. Algorithms such as waifu2x or VDSR vastly outperform any other general-purpose upscaling algorithms.  

However, we will take advantage of the fact that our upscaling algorithm only needs to work on a **single** type of content (animation), thus we might have a chance to match (or even outperform) learning-based algorithms.


## Proposed Method

Generally, animation frames do not contain a lot of textures, they are mostly composed of flat shaded objects and lines. Thus, a human can quickly recognize a low-quality upscale of an anime, since even slight bit of bluriness is noticeable.

Instead of going for a general purpose upscaling algorithm, we decided to find a good edge-refinement algorithm. Crisp edges are more important to anime upscaling than recovering small details such as texture.

By looking at the failure cases of existing edge refinement algorithms, we conclude that if predicted the residual is ever slightly wrong, we see ringing and overshoot on the final image. Thus, we took a different approach.


As a general rule, the less blurry an image is, the thinner the residual lines. To take advantage of that fact, our algorithm will try to minimize the residuals' line thickness. However, having a thin residual is useless, since applying an arbitrarily transformed residual to **LR_U** is wrong and meaningless (we can't compute **HR** with only a residual, we need its corresponding **LR_U**). But, we can use this idea to define an objective function that seeks to minimize that image's residual thickness.

![Residuals Comparison](results/Residuals_Comparison.png?raw=true)

The main objective is to modify **LR_U** (the blurry image) until its residual becomes thinnest, giving us one of the possible **HR** (sharp) images.

Our algorithm will simply take as input **LR_U** and its residual, push the residual's pixels so that the residual lines becomes thinner. For each 'push' operation performed on the residual, we do the same on the color image. The residual will serve as a guide where to push. This has the effect of iteratively maximizing the gradients of an image, which mathematically is equivalent to minimizing blur, but without overshoot or ringing artifacts commonly found on traditional 'unblurring' and 'sharpening' approaches.

Pseudocode:
'''
  for each pixel on the image:
    for each direction (north, northeast, east, etc.):
      using the residual, if an edge is found:
        push the residual pixel in the current direction
        push the color pixel in the current direction
'''

One trick our algorithm uses to improve performance is to use a sobel filter to approximate the image's residual instead of computing the residual with a gaussian filter, as computing a gaussian kernel is more expensive. Furthermore, maximizing the sobel gradient is mathematically similar (but not equivalent!) to minimizing the residual thickness. This modification yielded no quality degradation on visual inspection.


An advantage of this algorithm is the fact it is scale-independent. The anime could be incorrectly upscaled beforehand (double upscaling, or even downscaled then upscaled), and this algorithm will still detect the blurry edges and refine them. Thus, the image can be upscaled in advance with any algorithm the user prefers (Bilinear, Jinc, xBR, or even waifu2x), this algorithm will then correctly refine the edges and remove blur. Running this algorithm on animes mastered at 900p makes the result look like a true 1080p anime.
For a stronger deblur, we simply run the algorithm again. This algorithm iteratively sharpens the image.

However, for 2x upscales, we noticed that the lines were usually too thick and looked unnatural (since blur usually spread dark lines outwards, making them thicker), thus we added a pre-pass to thin lines. This pass is not integral to the algorithm and can be safely removed by the user if he wishes to keep the thick lines.  

We have implemented this algorithm both in Java and HLSL/C, they can be found in this repo.
The Java version can be used as an API to upscale images, while the HLSL code can be used as custom shaders for any media player supporting HLSL shaders. (In particular MPC-HC and MPC-BE with madVR)


## Results

To our surprise, such a simple method produced a exceptionally effective algorithm for unblurring and upscaling anime. It is not as good as waifu2x for recovering small details, but is very good at reconstructing sharp edges from blurry lines.  
Furthermore, due to the simplicity of this algorithm, running it on an GPU (*AMD RX Vega 64*) takes a mere 3 miliseconds, allowing us to upscale anime in real time. Even running on much less powerful integrated laptop GPUs (*Ryzen 5 2500U APU with Vega 8*) only takes 9 miliseconds.  
Instead of needing to upscale beforehand, the user can simply watch the anime with our algorithm running. This algorithm can potentially be implemented on phones or even run directly on the CPU if the user does not have a GPU.


Here are a few randomly selected comparisons:  
*Unless otherwise specified, all Anime4K upscales in comparisons are pre-upscaled with the Jinc algorithm found in madVR. The NGU variant used is NGU Sharp.*

### 1080p to 4K
![Upscale Comparison 0](results/Comparisons/0.png?raw=true)

![Upscale Comparison 1](results/Comparisons/1.png?raw=true)

![Upscale Comparison 2](results/Comparisons/2.png?raw=true)

![Upscale Comparison 3](results/Comparisons/3.png?raw=true)

### 720p to 1080p
![Upscale Comparison 4](results/Comparisons/7_1080.png?raw=true)

![Upscale Comparison 5](results/Comparisons/8_1080.png?raw=true)


### 480p to 1080p (A bit harder)

![Upscale Comparison 6](results/Comparisons/4.png?raw=true)

![Upscale Comparison 7](results/Comparisons/9.png?raw=true)

### 720p to 4K (Torture test)

![Upscale Comparison 8](results/Comparisons/7_4k.png?raw=true)

![Upscale Comparison 9](results/Comparisons/8_4k.png?raw=true)

### Art upscaling (Anime style)

Other algorithms are not shown as they perform poorly for art upscaling and are perceptually similar to bilinear.  

![Upscale Comparison 10](results/Comparisons/Art_0.png?raw=true)

![Upscale Comparison 11](results/Comparisons/Art_1_1.png?raw=true)

*More comparisons can be found in the appendix, and the raw images can be found in the repo under [/results/Upscale_Examples/](https://github.com/bloc97/Anime4K/tree/master/results/Upscale_Examples)*


## Discussion
Our algorithm can better recover sharp edges from all the pictures, even compared to waifu2x since it was specially tailored for this purpose.

However, a big weakness of our algorithm shows when we try to recover small details present in anime style art. waifu2x outperformed our algorithm by a large margin when there is texture detail, however since upscaling art was not our main goal, our results are acceptable.  
Furthermore, since our algorithm is scale-independent, we can apply it after running waifu2x, further enhancing and sharpening the edges.  

Then, as predicted, the bigger the upscaling scale, the harder it is for our algorithm. (Also harder for other algorithms) It succesfully sharpens the edges but cannot recover  sharp corners and texture, making the picture look like a pastel painting. Some people might like this style, some might not.  

One failure case of our algorithm is it tries to maximize soft gradients in the image, producing sharp bands of different colours if allowed to run for large amounts of iterations. A better edge detection will surely get rid of this problem.  

Interesting enough, waifu2x performed very poorly on anime. A plausible explaination is that the network was simply not trained to upscale these types of images. Usually anime style art have sharper lines and contain much more small details/textures compared to anime. The distribution of images used to train waifu2x must have been mostly art images from sites like DevianArt/Danbooru/Pixiv, and not anime.  
Furthermore, supervised training for a neural network to do 4K upscaling is currently not possible due to a lack of ground truth, there is simply no 4K anime yet! Unsupervised methods currently do not yield good enough quality to be used in practice. We will have to wait, until then, we believe our algorithm is state-of-the-art for real-time anime upscaling.


## Analysis

After a quick double blind test involving a few individuals, we were able to conjure up this (not-so-accurate) relative graph.  

Anime4K used as a standalone upscaling algorithm (Bilinear + Anime4K) already outperforms other more complex algorithms. With a little help (Jinc or xBR), it quickly becomes state of the art in the real time category. 

![Relative Quality Comparison Graph](results/Graph.png?raw=true)


## Conclusion
In conclusion, while our algorithm is very simple, it is also very good at upscaling anime within a short time budget. Furthermore, the resulting algorithm outputs good quality upscales of 720p anime for 1080p screens, potentially allowing users to save disk space and/or network bandwidth by only archiving 720p encodes. We are certain that some refinement (such as a better edge detection algorithm) will reduce artifacts, but that is left for another time. If the reader is interested enough, we encourage analyzing and improving this algorithm.  


## Sources
(1) *Jiwon Kim, Jung Kwon Lee, Kyoung Mu Lee*, [**Accurate Image Super-Resolution Using Very Deep Convolutional Networks**](https://arxiv.org/abs/1511.04587)  
(2) *nagadomi*, [**waifu2x, Image Super-Resolution for Anime-Style Art**](https://github.com/nagadomi/waifu2x)  
(3) *Wikipedia*, [**Overshoot (signal)**](https://en.wikipedia.org/wiki/Overshoot_(signal))  
(4) *Wikipedia*, [**Image scaling**](https://en.wikipedia.org/wiki/Image_scaling)  
(5) *Wikipedia*, [**Pixel-art scaling algorithms**](https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms)  
(6) *Wikipedia*, [**Unsharp masking**](https://en.wikipedia.org/wiki/Unsharp_masking)

## Appendix

### More Upscale Comparisons

*The raw images can be found in the repo under [/results/Upscale_Examples/](https://github.com/bloc97/Anime4K/tree/master/results/Upscale_Examples)*

![Upscale Comparison](results/Comparisons/5.png?raw=true)
![Upscale Comparison](results/Comparisons/6.png?raw=true)
![Upscale Comparison](results/Comparisons/10.png?raw=true)
![Upscale Comparison](results/Comparisons/11.png?raw=true)
![Upscale Comparison](results/Comparisons/12.png?raw=true)
![Upscale Comparison](results/Comparisons/13.png?raw=true)
![Upscale Comparison](results/Comparisons/14.png?raw=true)
![Upscale Comparison](results/Comparisons/15.png?raw=true)

![Upscale Comparison](results/Comparisons/Art_0_1.png?raw=true)
![Upscale Comparison](results/Comparisons/Art_1.png?raw=true)

```
## _Upscaling_md
```### Note for those who think this is not a 'upscaling' algorithm.

The word you are actually looking for is "interpolation".

No, this algorithm doesn't do any rigorous interpolation. The interpolation step can be done by Nearest-Neighbor, Bilinear, Bicubic or any of your algorithm of choice. It just happens that the better the interpolation algorithm, the better the final results.

However, it seems that when an upscaling algorithm is very complex (xBR or waifu2x), people tend to not care about the definitions and agree that it is somehow "super-resolution" and not a "sharpening" filter. But when the algorithm is extremely simple, like Anime4K in this case, they immediately assume it is a "sharpening" algorithm.  

Somehow "sharpening" is bad but "super-resolution" is good when they are referring to the same thing?

It is important to understand that De-Blurring/Sharpening (in the specific case of gaussian blur) and Super-Resolution are **equivalent** in signal processing. If your algorithm can do one, it can do the other!

A Super-Resolution algorithm can be used to deblur, by first determining the blur factor, downscaling the image accordingly, and applying the SR algorithm.  
A deblur algorithm can be used to super-resolve, by first upsampling an low resolution image, applying gaussian blur, and applying the deblur algorithm. (This is what Anime4K does!)

Over-sharpening is usually what people associate with "sharpening" algorithms. But, it is not because they are "sharpening" algorithms that they are somehow "bad", it is simply because they are too simple or used for the wrong purpose. In Anime4K's case, we're sacrificing smoothness by introducing some aliasing, but with the benefit of **zero** ringing artifacts. Ringing is much more noticeable compared to aliasing when watching anime on 4K screens.

Just as how unsharp masking can ruin an image with ringing, Anime4K can do the same with aliasing if not used properly. People who don't mind ringing can keep using unsharp masking while those who don't mind aliasing can use Anime4K.

For those commenting around about sharpening = bad, please, do some research before spreading misinformation.
```
## _github_ISSUE_TEMPLATE_feature_request_md
```---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
```
## _HLSL_Instructions_md
```
# Usage Instructions (HLSL)
*If you wish to use another media player, look at their documentation on how to install HLSL shaders and modify the shader accordingly if needed.*

1. Install [**MPC-HC**](https://github.com/clsid2/mpc-hc) or [**MPC-BE**](https://sourceforge.net/projects/mpcbe/) and [madVR](http://madvr.com/) (Optional, but good for quality)
1. (MPC-HC Only) Enable Full Floating Point Processing or Half Floating Point Processing in [Renderer Settings](https://trac.mpc-hc.org/wiki/New_Renderer_Settings).
1. Download the .hlsl shader files [**here**](https://github.com/bloc97/Anime4K/releases)  
1. (MPC-BE Only) Copy the .hlsl files to `%AppData%\MPC-BE\Shaders`  
1. Add the shaders **(The order is important!)**   

![Step1](results/Step1.png?raw=true)

**Different screen resolutions need different shaders:**  
Smaller or equal to 1080p  
'''
-Anime4K_ComputeLum  
-Anime4K_Push  
-Anime4K_ComputeGradient  
-Anime4K_PushGrad_Weak  
'''
Larger than 1080p  
'''
-Anime4K_ComputeLum  
-Anime4K_Push  
-Anime4K_ComputeGradient  
-Anime4K_PushGrad  
'''

Note: *Anime4K_Push* is an optional pass that thins lines, it can be removed if the effect is unsatisfactory for certain anime.

![Step2](results/Step2.png?raw=true)


### If madVR is installed
*These are heavy on the GPU, do not use them if rendering times rise above 30ms*  

Settings used for all the comparisons:  
![Settings1](results/Settings1.png?raw=true)

![Settings1](results/Settings2.png?raw=true)
```
# Inline
## _web_main_js
### Line 120-129
```
    return mix(mix(tl, tr, f.x), mix(bl, br, f.x), f.y);
}

void main() {
    gl_FragColor = interp(1.0 - v_tex_pos);
    //gl_FragColor = texture2D(u_texture, 1.0 - v_tex_pos);
}
`;

const lumFrag = `

```
### Line 151-160
```
uniform float u_scale;
uniform float u_bold;
uniform vec2 u_pt;
varying vec2 v_tex_pos;

#define strength (min(u_scale / u_bold, 1.0))

vec4 HOOKED_tex(vec2 pos) {
    return texture2D(u_texture, pos);
}

```
### Line 199-208
```
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	vec4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 213-222
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 227-236
```
		if (minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 241-250
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```
### Line 284-295
```
void main() {
    vec2 HOOKED_pos = v_tex_pos;
    
	vec2 d = u_pt;
	
	//[tl  t tr]
	//[ l cc  r]
	//[bl  b br]
    vec4 cc = getRGBL(HOOKED_pos);
	vec4 t = getRGBL(HOOKED_pos + vec2(0.0, -d.y));
	vec4 tl = getRGBL(HOOKED_pos + vec2(-d.x, -d.y));
	vec4 tr = getRGBL(HOOKED_pos + vec2(d.x, -d.y));

```
### Line 299-317
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0.0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-tl.a + tr.a - l.a - l.a + r.a + r.a - bl.a + br.a);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
    float ygrad = (-tl.a - t.a - t.a - tr.a + bl.a + b.a + b.a + br.a);
    
    gl_FragColor = vec4(1.0 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0.0, 1.0));
}

```
### Line 325-334
```
uniform vec2 u_pt;
uniform float u_scale;
uniform float u_blur;
varying vec2 v_tex_pos;

#define strength (min(u_scale / u_blur, 1.0))

vec4 HOOKED_tex(vec2 pos) {
    return texture2D(u_texture, vec2(pos.x, 1.0 - pos.y));
}

```
### Line 367-376
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0.0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 383-392
```
            gl_FragColor = getAverage(cc, br, b, bl);
            return;
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 399-408
```
            gl_FragColor = getAverage(cc, bl, l, b);
            return;
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 415-424
```
            gl_FragColor = getAverage(cc, l, tl, bl);
            return;
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```
### Line 542-551
```
    gl.disable(gl.STENCIL_TEST);

    gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);


    // First upscaling with Bicubic interpolation.

    bindFramebuffer(gl, this.framebuffer, this.scaleTexture);

    gl.useProgram(scalePgm.program);

```
### Line 555-564
```
    gl.uniform1i(scalePgm.u_texture, 0);
    gl.uniform2f(scalePgm.u_size, this.inputWidth, this.inputHeight);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: scaleTexture


    bindFramebuffer(gl, this.framebuffer, this.tempTexture);


```
### Line 568-578
```
    bindTexture(gl, this.scaleTexture, 0);
    gl.uniform1i(lumPgm.u_texture, 0);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: scaleTexture
    // PostKernel: tempTexture


    bindFramebuffer(gl, this.framebuffer, this.tempTexture2);


```
### Line 587-597
```
    gl.uniform2f(pushPgm.u_pt, 1.0 / gl.canvas.width, 1.0 / gl.canvas.height);
    gl.uniform1f(pushPgm.u_bold, this.bold);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: tempTexture2
    // PostKernel: tempTexture


    bindFramebuffer(gl, this.framebuffer, this.tempTexture);


```
### Line 601-611
```
    bindTexture(gl, this.tempTexture2, 0);
    gl.uniform1i(lumPgm.u_texture, 0);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: tempTexture2
    // PostKernel: tempTexture


    bindFramebuffer(gl, this.framebuffer, this.tempTexture3);


```
### Line 618-628
```
    gl.uniform1i(gradPgm.u_textureTemp, 1);
    gl.uniform2f(gradPgm.u_pt, 1.0 / gl.canvas.width, 1.0 / gl.canvas.height);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: tempTexture2
    // PostKernel: tempTexture3


    bindFramebuffer(gl, this.framebuffer, this.tempTexture);


```
### Line 637-647
```
    gl.uniform2f(finalPgm.u_pt, 1.0 / gl.canvas.width, 1.0 / gl.canvas.height);
    gl.uniform1f(finalPgm.u_blur, this.blur);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    // Scaled: tempTexture
    // PostKernel: tempTexture3


    bindFramebuffer(gl, null);


```

## _hlsl_Anime4K_Push_Weak_hlsl
### Line 1-41
```
// $MinimumShaderProfile: ps_2_a

// MIT License

// Copyright (c) 2019 bloc97

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define dx (p1[0])
#define dy (p1[1])
#define PI acos(-1)

#define strength 0.3

float min3(float4 a, float4 b, float4 c) {
	return min(min(a[3], b[3]), c[3]);
}

```
### Line 67-76
```
	float4 br = tex2D(s0, tex + float2(dx, dy));
	
	
	float4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3(br, b, bl);
	float minLight = min3(tl, t, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 81-90
```
		if (minLight > cc[3] && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3(cc, l, b);
	minLight = min3(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 95-104
```
		if (minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3(l, tl, bl);
	minLight = min3(r, br, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 109-118
```
		if (minLight > cc[3] && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3(cc, l, t);
	minLight = min3(r, br, b);
	
	if (minLight > maxDark) {

```

## _java_build_sh
### Line 1-5
```
#!/bin/bash

sh -c 'mvn clean compile assembly:single'

mv 'target/Anime4K-static.jar' 'Anime4K.jar'
```

## _glsl_Anime4K_Adaptive_v0_9_glsl
### Line 1-34
```
//Anime4K GLSL v0.9

// MIT License

// Copyright (c) 2019 bloc97

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


//!HOOK SCALED
//!BIND HOOKED
//!DESC Anime4K-ComputeLuma-v0.9
//!BIND POSTKERNEL
//!SAVE POSTKERNEL

float getLum(vec4 rgb) {
	return (rgb.r + rgb.r + rgb.g + rgb.g + rgb.g + rgb.b) / 6;
}

```
### Line 38-53
```
	float lum = getLum(rgb);
    return vec4(lum);
}


//!HOOK SCALED
//!BIND HOOKED
//!DESC Anime4K-ThinLines-v0.9
//!BIND POSTKERNEL
//!BIND NATIVE

#define strength (min((SCALED_size.x) / (NATIVE_size.x) / 6, 1))

vec4 getLargest(vec4 cc, vec4 lightestColor, vec4 a, vec4 b, vec4 c) {
	vec4 newColor = cc * (1 - strength) + ((a + b + c) / 3) * strength;
	if (newColor.a > lightestColor.a) {

```
### Line 83-92
```
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	vec4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 97-106
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 111-120
```
		if (minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 125-134
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```
### Line 144-157
```
	
	return lightestColor;
}


//!HOOK SCALED
//!BIND HOOKED
//!DESC Anime4K-ComputeLuma-v0.9
//!BIND POSTKERNEL
//!SAVE POSTKERNEL

float getLum(vec4 rgb) {
	return (rgb.r + rgb.r + rgb.g + rgb.g + rgb.g + rgb.b) / 6;
}

```
### Line 161-185
```
	float lum = getLum(rgb);
    return vec4(lum);
}


//!HOOK SCALED
//!BIND HOOKED
//!DESC Anime4K-ComputeGradient-v0.9
//!BIND POSTKERNEL
//!SAVE POSTKERNEL

vec4 getRGBL(vec2 pos) {
    return vec4(HOOKED_tex(pos).rgb, POSTKERNEL_tex(pos).x);
}

vec4 hook() { //Save grad on POSTKERNEL
	vec2 d = HOOKED_pt;
	
	//[tl  t tr]
	//[ l cc  r]
	//[bl  b br]
    vec4 cc = getRGBL(HOOKED_pos);
	vec4 t = getRGBL(HOOKED_pos + vec2(0, -d.y));
	vec4 tl = getRGBL(HOOKED_pos + vec2(-d.x, -d.y));
	vec4 tr = getRGBL(HOOKED_pos + vec2(d.x, -d.y));

```
### Line 190-223
```
	vec4 b = getRGBL(HOOKED_pos + vec2(0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-tl.a + tr.a - l.a - l.a + r.a + r.a - bl.a + br.a);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (-tl.a - t.a - t.a - tr.a + bl.a + b.a + b.a + br.a);
	
	//Computes the luminance's gradient and saves it in the unused alpha channel
	return vec4(1 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0, 1));
}



//!HOOK SCALED
//!BIND HOOKED
//!DESC Anime4K-Refine-v0.9
//!BIND POSTKERNEL
//!BIND NATIVE

#define strength (min((SCALED_size.x) / (NATIVE_size.x) / 2, 1))

vec4 getAverage(vec4 cc, vec4 a, vec4 b, vec4 c) {
	return cc * (1 - strength) + ((a + b + c) / 3) * strength;
}

```
### Line 247-256
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 261-270
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 275-284
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 289-298
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```

## _hlsl_Anime4K_ComputeGradient_hlsl
### Line 1-23
```
// $MinimumShaderProfile: ps_2_0
sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define dx  (p1[0])
#define dy (p1[1])
#define PI acos(-1)

float4 main(float2 tex : TEXCOORD0) : COLOR {
	float4 c0 = tex2D(s0, tex);
	
	//[tl  t tr]
	//[ l     r]
	//[bl  b br]
	float t  = tex2D(s0, tex + float2(  0, -dy))[3];
	float tl = tex2D(s0, tex + float2(-dx, -dy))[3];
	float tr = tex2D(s0, tex + float2( dx, -dy))[3];
	

```
### Line 26-45
```
	
	float b  = tex2D(s0, tex + float2(  0,  dy))[3];
	float bl = tex2D(s0, tex + float2(-dx,  dy))[3];
	float br = tex2D(s0, tex + float2( dx,  dy))[3];
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-tl + tr - l - l + r + r - bl + br);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (-tl - t - t - tr + bl + b + b + br);
	
	//Computes the luminance's gradient and saves it in the unused alpha channel
	return float4(c0[0], c0[1], c0[2], 1 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0, 1));
}

```

## _hlsl_Anime4K_PushGrad_Weak_hlsl
### Line 1-41
```
// $MinimumShaderProfile: ps_2_a

// MIT License

// Copyright (c) 2019 bloc97

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define dx (p1[0])
#define dy (p1[1])
#define PI acos(-1)

#define strength 0.7

float min3(float4 a, float4 b, float4 c) {
	return min(min(a[3], b[3]), c[3]);
}

```
### Line 63-72
```
	float4 br = tex2D(s0, tex + float2(dx, dy));
	
	
	float4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3(br, b, bl);
	float minLight = min3(tl, t, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 77-86
```
		if (minLight > cc[3] && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3(cc, l, b);
	minLight = min3(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 91-100
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3(l, tl, bl);
	minLight = min3(r, br, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 105-114
```
		if (minLight > cc[3] && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3(cc, l, t);
	minLight = min3(r, br, b);
	
	if (minLight > maxDark) {

```

## _glsl_Anime4K_Adaptive_v1_0RC_glsl
### Line 1-34
```

```
### Line 75-84
```

```
### Line 89-98
```

```
### Line 103-112
```

```
### Line 117-126
```

```
### Line 137-150
```

```
### Line 154-167
```

```
### Line 178-191
```

```
### Line 201-221
```

```
### Line 223-246
```

```
### Line 257-270
```

```
### Line 281-294
```

```
### Line 298-309
```

```
### Line 314-350
```

```
### Line 379-388
```

```
### Line 393-402
```

```
### Line 407-416
```

```
### Line 421-430
```

```
### Line 439-465
```

```
### Line 509-519
```

```

## _java_src_main_java_com_bloc97_anime4k_ImageKernel_java
### Line 64-73
```
    public void setPushGradStrength(float strength) {
        runtype[2] = clamp((int)(strength * 255), 0, 0xFFFF);
    }

    public void process() {
        //Compute Lum
        runtype[0] = 0;
        this.execute(colorData.length);
        
        int maxUnblur = runtype[1];

```
### Line 87-96
```
            remainingUnblur -= currentThin;
        }
        
        runtype[1] = maxUnblur; //Restore original value
        
        //Compute Gradient
        if (isForwardPass) {
            runtype[0] = 3;
        } else {
            runtype[0] = 4;

```
### Line 203-218
```
        strength = clamp(strength, 0, 0xFF);

        int x = id % width;
        int y = id / width;

        //Default translation constants
        int xn = -1;
        int xp = 1;
        int yn = -width;
        int yp = width;

        //If x or y is on the border, don't move out of bounds
        if (x == 0) {
            xn = 0;
        } else if (x == width - 1) {
            xp = 0;

```
### Line 221-230
```
            yn = 0;
        } else if (y == height - 1) {
            yp = 0;
        }

        //Get indices for adjacent cells
        int ti = id + yn;
        int tli = ti + xn;
        int tri = ti + xp;


```
### Line 406-421
```
        strength = clamp(strength, 0, 0xFF);

        int x = id % width;
        int y = id / width;

        //Default translation constants
        int xn = -1;
        int xp = 1;
        int yn = -width;
        int yp = width;

        //If x or y is on the border, don't move out of bounds
        if (x == 0) {
            xn = 0;
        } else if (x == width - 1) {
            xp = 0;

```
### Line 424-433
```
            yn = 0;
        } else if (y == height - 1) {
            yp = 0;
        }

        //Get indices for adjacent cells
        int ti = id + yn;
        int tli = ti + xn;
        int tri = ti + xp;


```
### Line 621-636
```
        }

        int x = id % width;
        int y = id / width;

        //Default translation constants
        int xn = -1;
        int xp = 1;
        int yn = -width;
        int yp = width;

        //If x or y is on the border, don't move out of bounds
        if (x == 0) {
            xn = 0;
        } else if (x == width - 1) {
            xp = 0;

```
### Line 639-648
```
            yn = 0;
        } else if (y == height - 1) {
            yp = 0;
        }

        //Get indices for adjacent cells
        int topi = id + yn;
        int topLefti = topi + xn;
        int topRighti = topi + xp;


```
### Line 651-660
```

        int bottomi = id + yp;
        int bottomLefti = bottomi + xn;
        int bottomRighti = bottomi + xp;

        //Get values for adjacent cells
        int top = ((int)thisDerivData[topi]) & 0xFF;
        int topLeft = ((int)thisDerivData[topLefti]) & 0xFF;
        int topRight = ((int)thisDerivData[topRighti]) & 0xFF;


```
### Line 663-672
```

        int bottom = ((int)thisDerivData[bottomi]) & 0xFF;
        int bottomLeft = ((int)thisDerivData[bottomLefti]) & 0xFF;
        int bottomRight = ((int)thisDerivData[bottomRighti]) & 0xFF;

        //Perform Sobel Operation
        int xSobel = abs(-topLeft + topRight
                - left - left + right + right
                - bottomLeft + bottomRight);
        int ySobel = abs(-topLeft - top - top - topRight

```

## _hlsl_Anime4K_Push_hlsl
### Line 1-42
```
// $MinimumShaderProfile: ps_2_a

// MIT License

// Copyright (c) 2019 bloc97

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define dx (p1[0])
#define dy (p1[1])
#define PI acos(-1)

#define strength 0.3

float min3(float4 a, float4 b, float4 c) {
	return min(min(a[3], b[3]), c[3]);
}

```
### Line 68-77
```
	float4 br = tex2D(s0, tex + float2(dx, dy));
	
	
	float4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3(br, b, bl);
	float minLight = min3(tl, t, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 82-91
```
		if (minLight > cc[3] && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3(cc, l, b);
	minLight = min3(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 96-105
```
		if (minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3(l, tl, bl);
	minLight = min3(r, br, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 110-119
```
		if (minLight > cc[3] && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3(cc, l, t);
	minLight = min3(r, br, b);
	
	if (minLight > maxDark) {

```

## _hlsl_Anime4K_ComputeLum_hlsl
### Line 1-22
```
// $MinimumShaderProfile: ps_2_0
sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define one_over_width  (p1[0])
#define one_over_height (p1[1])
#define PI acos(-1)

float4 main(float2 tex : TEXCOORD0) : COLOR {
	float4 c0 = tex2D(s0, tex);
	
	//Quick luminance approximation
	float lum = (c0[0] + c0[0] + c0[1] + c0[1] + c0[1] + c0[2]) / 6;
	
	//Computes the luminance and saves it in the unused alpha channel
	return float4(c0[0], c0[1], c0[2], lum);
}

```

## _glsl_Anime4K_Adaptive_v1_0RC2_glsl
### Line 1-48
```
//Anime4K GLSL v1.0 Release Candidate 2

// MIT License

// Copyright (c) 2019 bloc97, DextroseRe

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

//!DESC Anime4K-Luma-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!WIDTH OUTPUT.w
//!HEIGHT OUTPUT.h
//!SAVE LUMAX
//!COMPONENTS 1

vec4 hook() {
	return HOOKED_tex(HOOKED_pos);
}

//!DESC Anime4K-ComputeGaussianX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian7(vec2 pos, vec2 d) {
	float g = LUMA_tex(pos - (d * 3)).x * 0.121597;
	g = g + LUMA_tex(pos - (d * 2)).x * 0.142046;

```
### Line 60-76
```
    return vec4(g, 0, 0, 0);
}



//!DESC Anime4K-ComputeGaussianY-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian7(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 3)).x * 0.121597;
	g = g + LUMAG_tex(pos - (d * 2)).x * 0.142046;

```
### Line 87-109
```
	float g = lumGaussian7(HOOKED_pos, vec2(0, LUMAX_pt.y));
    return vec4(g, 0, 0, 0);
}


//!DESC Anime4K-LineDetect-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

#define BlendColorDodgef(base, blend) 	(((blend) == 1.0) ? (blend) : min((base) / (1.0 - (blend)), 1.0))
#define BlendColorDividef(top, bottom) 	(((bottom) == 1.0) ? (bottom) : min((top) / (bottom), 1.0))

// Component wise blending
#define Blend(base, blend, funcf) 		vec3(funcf(base.r, blend.r), funcf(base.g, blend.g), funcf(base.b, blend.b))
#define BlendColorDodge(base, blend) 	Blend(base, blend, BlendColorDodgef)


vec4 hook() {
	float lum = clamp(LUMA_tex(HOOKED_pos).x, 0.001, 0.999);

```
### Line 115-131
```
    return vec4(pseudolines, 0, 0, 0);
}



//!DESC Anime4K-ComputeLineGaussianX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian7(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 3)).x * 0.121597;
	g = g + LUMAG_tex(pos - (d * 2)).x * 0.142046;

```
### Line 143-159
```
    return vec4(g, 0, 0, 0);
}



//!DESC Anime4K-ComputeLineGaussianY-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian7(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 3)).x * 0.121597;
	g = g + LUMAG_tex(pos - (d * 2)).x * 0.142046;

```
### Line 170-266
```
	float g = lumGaussian7(HOOKED_pos, vec2(0, LUMAX_pt.y));
    return vec4(g, 0, 0, 0);
}


//!DESC Anime4K-ComputeGradientX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!SAVE LUMAD
//!COMPONENTS 2

vec4 hook() {
	vec2 d = LUMAX_pt;
	
	//[tl  t tr]
	//[ l  c  r]
	//[bl  b br]
	float l = LUMA_tex(HOOKED_pos + vec2(-d.x, 0)).x;
    float c = LUMA_tex(HOOKED_pos).x;
	float r = LUMA_tex(HOOKED_pos + vec2(d.x, 0)).x;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-l + r);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (l + c + c + r);
	
	//Computes the luminance's gradient
	return vec4(xgrad, ygrad, 0, 0);
}


//!DESC Anime4K-ComputeGradientY-v1.0RC2
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMAD
//!SAVE LUMAD
//!COMPONENTS 1

vec4 hook() {
	vec2 d = LUMAX_pt;
	
	//[tl  t tr]
	//[ l cc  r]
	//[bl  b br]
	float tx = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).x;
    float cx = LUMAD_tex(HOOKED_pos).x;
	float bx = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).x;
	
	
	float ty = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).y;
    //float cy = LUMAD_tex(HOOKED_pos).y;
	float by = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).y;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (tx + cx + cx + bx);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (-ty + by);
	
	//Computes the luminance's gradient
	return vec4(1 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0, 1), 0, 0, 0);
}


//!DESC Anime4K-ThinLines-v1.0RC2
//!HOOK SCALED
//!BIND HOOKED
//!BIND LUMA
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMAG

#define LINE_DETECT_THRESHOLD 0.06

#define lineprob (LUMAG_tex(HOOKED_pos).x)

float getLum(vec4 rgb) {
	return (rgb.r + rgb.r + rgb.g + rgb.g + rgb.g + rgb.b) / 6.0;
}

```
### Line 308-317
```
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	vec4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 322-331
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 336-345
```
		if (minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 350-359
```
		if (minLight > cc.a && minLight > maxDark) {
			lightestColor = getLargest(cc, lightestColor, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```
### Line 369-391
```
	
	return lightestColor;
}


//!DESC Anime4K-Refine-v1.0RC2
//!HOOK SCALED
//!BIND HOOKED
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMA
//!BIND LUMAD
//!BIND LUMAG

#define LINE_DETECT_MUL 6
#define LINE_DETECT_THRESHOLD 0.06
#define MAX_STRENGTH 1

#define strength (min((SCALED_size.x) / (LUMA_size.x), 1))
#define lineprob (LUMAG_tex(HOOKED_pos).x)

vec4 getAverage(vec4 cc, vec4 a, vec4 b, vec4 c) {
	float realstrength = clamp(strength * lineprob * LINE_DETECT_MUL, 0, MAX_STRENGTH);
	return cc * (1 - realstrength) + ((a + b + c) / 3) * realstrength;

```
### Line 421-430
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 435-444
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 449-458
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 463-472
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```
### Line 482-509
```
	
	return cc;
}


//Fast FXAA (1 Iteration) courtesy of Geeks3D
//https://www.geeks3d.com/20110405/fxaa-fast-approximate-anti-aliasing-demo-glsl-opengl-test-radeon-geforce/3/

//!DESC Anime4K-PostFXAA-v1.0RC2
//!HOOK SCALED
//!BIND HOOKED
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMA
//!BIND LUMAG

#define FXAA_MIN (1.0 / 128.0)
#define FXAA_MUL (1.0 / 8.0)
#define FXAA_SPAN 8.0

#define LINE_DETECT_MUL 6
#define LINE_DETECT_THRESHOLD 0.06

#define strength (min((SCALED_size.x) / (LUMA_size.x), 1))
#define lineprob (LUMAG_tex(HOOKED_pos).x)

vec4 getAverage(vec4 cc, vec4 xc) {
	float prob = clamp(lineprob, 0, 1);
	if (prob < LINE_DETECT_THRESHOLD) {

```

## _hlsl_Anime4K_PushGrad_hlsl
### Line 1-41
```
// $MinimumShaderProfile: ps_2_a

// MIT License

// Copyright (c) 2019 bloc97

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

sampler s0 : register(s0);
float4 p0 :  register(c0);
float4 p1 :  register(c1);

#define width   (p0[0])
#define height  (p0[1])
#define counter (p0[2])
#define clock   (p0[3])
#define dx (p1[0])
#define dy (p1[1])
#define PI acos(-1)

#define strength 1

float min3(float4 a, float4 b, float4 c) {
	return min(min(a[3], b[3]), c[3]);
}

```
### Line 63-72
```
	float4 br = tex2D(s0, tex + float2(dx, dy));
	
	
	float4 lightestColor = cc;

	//Kernel 0 and 4
	float maxDark = max3(br, b, bl);
	float minLight = min3(tl, t, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 77-86
```
		if (minLight > cc[3] && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3(cc, l, b);
	minLight = min3(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 91-100
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3(l, tl, bl);
	minLight = min3(r, br, tr);
	
	if (minLight > cc[3] && minLight > maxDark) {

```
### Line 105-114
```
		if (minLight > cc[3] && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3(cc, l, t);
	minLight = min3(r, br, b);
	
	if (minLight > maxDark) {

```

## _glsl_Anime4K_Adaptive_v1_0RC2_Fast_glsl
### Line 1-48
```
//Anime4K GLSL v1.0 Release Candidate 2

// MIT License

// Copyright (c) 2019 bloc97, DextroseRe

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

//!DESC Anime4K-Luma-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!WIDTH OUTPUT.w
//!HEIGHT OUTPUT.h
//!SAVE LUMAX
//!COMPONENTS 1

vec4 hook() {
	return HOOKED_tex(HOOKED_pos);
}

//!DESC Anime4K-ComputeGaussianX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMA_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMA_tex(pos - d).x * 0.206038;

```
### Line 58-74
```
    return vec4(g, 0, 0, 0);
}



//!DESC Anime4K-ComputeGaussianY-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMAG_tex(pos - d).x * 0.206038;

```
### Line 83-105
```
	float g = lumGaussian5(HOOKED_pos, vec2(0, LUMAX_pt.y));
    return vec4(g, 0, 0, 0);
}


//!DESC Anime4K-LineDetect-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

#define BlendColorDodgef(base, blend) 	(((blend) == 1.0) ? (blend) : min((base) / (1.0 - (blend)), 1.0))
#define BlendColorDividef(top, bottom) 	(((bottom) == 1.0) ? (bottom) : min((top) / (bottom), 1.0))

// Component wise blending
#define Blend(base, blend, funcf) 		vec3(funcf(base.r, blend.r), funcf(base.g, blend.g), funcf(base.b, blend.b))
#define BlendColorDodge(base, blend) 	Blend(base, blend, BlendColorDodgef)


vec4 hook() {
	float lum = clamp(LUMA_tex(HOOKED_pos).x, 0.001, 0.999);

```
### Line 111-127
```
    return vec4(pseudolines, 0, 0, 0);
}



//!DESC Anime4K-ComputeLineGaussianX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMAG_tex(pos - d).x * 0.206038;

```
### Line 137-153
```
    return vec4(g, 0, 0, 0);
}



//!DESC Anime4K-ComputeLineGaussianY-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!BIND LUMAG
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMAG_tex(pos - d).x * 0.206038;

```
### Line 162-262
```
	float g = lumGaussian5(HOOKED_pos, vec2(0, LUMAX_pt.y));
    return vec4(g, 0, 0, 0);
}


//!DESC Anime4K-ComputeGradientX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!SAVE LUMAD
//!COMPONENTS 2

vec4 hook() {
	vec2 d = LUMAX_pt;
	
	//[tl  t tr]
	//[ l  c  r]
	//[bl  b br]
	float l = LUMA_tex(HOOKED_pos + vec2(-d.x, 0)).x;
    float c = LUMA_tex(HOOKED_pos).x;
	float r = LUMA_tex(HOOKED_pos + vec2(d.x, 0)).x;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-l + r);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (l + c + c + r);
	
	//Computes the luminance's gradient
	return vec4(xgrad, ygrad, 0, 0);
}


//!DESC Anime4K-ComputeGradientY-v1.0RC2
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAX
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMAD
//!SAVE LUMAD
//!COMPONENTS 1

vec4 hook() {
	vec2 d = LUMAX_pt;
	
	//[tl  t tr]
	//[ l cc  r]
	//[bl  b br]
	float tx = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).x;
    float cx = LUMAD_tex(HOOKED_pos).x;
	float bx = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).x;
	
	
	float ty = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).y;
    //float cy = LUMAD_tex(HOOKED_pos).y;
	float by = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).y;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (tx + cx + cx + bx);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (-ty + by);
	
	//Computes the luminance's gradient
	return vec4(1 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0, 1), 0, 0, 0);
}


//!DESC Anime4K-Refine-v1.0RC2
//!HOOK SCALED
//!BIND HOOKED
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMA
//!BIND LUMAD
//!BIND LUMAG

#define LINE_DETECT_MUL 6
#define LINE_DETECT_THRESHOLD 0.07
#define MAX_STRENGTH 0.6

#define strength (min((SCALED_size.x) / (LUMA_size.x), 1))
#define lineprob (LUMAG_tex(HOOKED_pos).x)

vec4 getAverage(vec4 cc, vec4 a, vec4 b, vec4 c) {
	float realstrength = clamp(strength * lineprob * LINE_DETECT_MUL, 0, MAX_STRENGTH);
	return cc * (1 - realstrength) + ((a + b + c) / 3) * realstrength;

```
### Line 292-301
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 306-315
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 320-329
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 334-343
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```

## _java_src_main_java_com_bloc97_anime4k_Main_java

## _glsl_Anime4K_Adaptive_v1_0RC2_UltraFast_glsl
### Line 1-111
```
//Anime4K GLSL v1.0 Release Candidate 2

// MIT License

// Copyright (c) 2019 bloc97, DextroseRe

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

//!DESC Anime4K-ComputeGradientX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!SAVE LUMAD
//!COMPONENTS 2

vec4 hook() {
	vec2 d = HOOKED_pt;
	
	//[tl  t tr]
	//[ l  c  r]
	//[bl  b br]
	float l = LUMA_tex(HOOKED_pos + vec2(-d.x, 0)).x;
    float c = LUMA_tex(HOOKED_pos).x;
	float r = LUMA_tex(HOOKED_pos + vec2(d.x, 0)).x;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (-l + r);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (l + c + c + r);
	
	//Computes the luminance's gradient
	return vec4(xgrad, ygrad, 0, 0);
}


//!DESC Anime4K-ComputeGradientY-v1.0RC2
//!HOOK LUMA
//!BIND HOOKED
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMAD
//!SAVE LUMAD
//!COMPONENTS 1

vec4 hook() {
	vec2 d = HOOKED_pt;
	
	//[tl  t tr]
	//[ l cc  r]
	//[bl  b br]
	float tx = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).x;
    float cx = LUMAD_tex(HOOKED_pos).x;
	float bx = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).x;
	
	
	float ty = LUMAD_tex(HOOKED_pos + vec2(0, -d.y)).y;
    //float cy = LUMAD_tex(HOOKED_pos).y;
	float by = LUMAD_tex(HOOKED_pos + vec2(0, d.y)).y;
	
	
	//Horizontal Gradient
	//[-1  0  1]
	//[-2  0  2]
	//[-1  0  1]
	float xgrad = (tx + cx + cx + bx);
	
	//Vertical Gradient
	//[-1 -2 -1]
	//[ 0  0  0]
	//[ 1  2  1]
	float ygrad = (-ty + by);
	
	//Computes the luminance's gradient
	return vec4(1 - clamp(sqrt(xgrad * xgrad + ygrad * ygrad), 0, 1), 0, 0, 0);
}


//!DESC Anime4K-ComputeLineGaussianX-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAD
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMAD_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMAD_tex(pos - d).x * 0.206038;

```
### Line 121-137
```
    return vec4(g, 0, 0, 0);
}



//!DESC Anime4K-ComputeLineGaussianY-v1.0RC2
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!HOOK LUMA
//!BIND HOOKED
//!BIND LUMAG
//!BIND LUMAD
//!SAVE LUMAG
//!COMPONENTS 1

float lumGaussian5(vec2 pos, vec2 d) {
	float g = LUMAG_tex(pos - (d * 2)).x * 0.187691;
	g = g + LUMAG_tex(pos - d).x * 0.206038;

```
### Line 145-166
```
vec4 hook() {
	float g = lumGaussian5(HOOKED_pos, vec2(0, HOOKED_pt.y));
    return vec4(1 - g, 0, 0, 0);
}

//!DESC Anime4K-Refine-v1.0RC2
//!HOOK SCALED
//!BIND HOOKED
//!WHEN OUTPUT.w LUMA.w / 1.400 > OUTPUT.h LUMA.h / 1.400 > *
//!BIND LUMA
//!BIND LUMAD
//!BIND LUMAG

#define LINE_DETECT_THRESHOLD 0.4
#define MAX_STRENGTH 0.6

#define strength (min((SCALED_size.x) / (LUMA_size.x), 1))
#define lineprob (LUMAG_tex(HOOKED_pos).x)

vec4 getAverage(vec4 cc, vec4 a, vec4 b, vec4 c) {
	float realstrength = clamp(strength, 0, MAX_STRENGTH);
	return cc * (1 - realstrength) + ((a + b + c) / 3) * realstrength;

```
### Line 196-205
```
	
	vec4 b = getRGBL(HOOKED_pos + vec2(0, d.y));
	vec4 bl = getRGBL(HOOKED_pos + vec2(-d.x, d.y));
	vec4 br = getRGBL(HOOKED_pos + vec2(d.x, d.y));
	
	//Kernel 0 and 4
	float maxDark = max3v(br, b, bl);
	float minLight = min3v(tl, t, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 210-219
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, br, b, bl);
		}
	}
	
	//Kernel 1 and 5
	maxDark = max3v(cc, l, b);
	minLight = min3v(r, t, tr);
	
	if (minLight > maxDark) {

```
### Line 224-233
```
		if (minLight > maxDark) {
			return getAverage(cc, bl, l, b);
		}
	}
	
	//Kernel 2 and 6
	maxDark = max3v(l, tl, bl);
	minLight = min3v(r, br, tr);
	
	if (minLight > cc.a && minLight > maxDark) {

```
### Line 238-247
```
		if (minLight > cc.a && minLight > maxDark) {
			return getAverage(cc, l, tl, bl);
		}
	}
	
	//Kernel 3 and 7
	maxDark = max3v(cc, l, t);
	minLight = min3v(r, br, b);
	
	if (minLight > maxDark) {

```

# Issues
## 5
Title:
```

        Noob here, Can someone giude me to run this? 
      
```
Author:
```
pranavburnwal
```
Text:
```

Hi,
Noob here so please avoid my ignorance. I am not well versed with the field but would like to convert &/or view Anime. Even to 1080p of old once from 480p will be awesome!
I own a 2017 macPro with Raedon 560.
Thanks!

```
Author:
```
MystesofEternity
```
Text:
```

Since you are using a Mac and I'm unsuare if mac has mpv, your best bet is this
https://github.com/bloc97/Anime4K/blob/master/Java_Instructions.md
You need to ensure java is installed
You can get the files of this software here: https://github.com/bloc97/Anime4K/releases
Releases can be accessed by clicking the part indicating the number of releases, use CTRL + F in https://github.com/bloc97/Anime4K to find it
Making just about anything work in Github takes patience and heart so I hope you understand I can't just spoon feed you everything. Feel free to ask questions as you go through the process of making this work.
If you find out that Mac has mpv player then these set of instructions will work:
https://github.com/bloc97/Anime4K/blob/master/GLSL_Instructions.md

```
Author:
```
pranavburnwal
```
Text:
```

Thanks! Will try!
Will reopen if I get stuck.

```
Author:
```
Suleman-Elahi
```
Text:
```

Can't run...even java is up to date.


```
Author:
```
stefnotch
```
Text:
```

java -version and post the output

```
Author:
```
Suleman-Elahi
```
Text:
```

C:\>java -version
java version "12.0.1" 2019-04-16
Java(TM) SE Runtime Environment (build 12.0.1+12)
Java HotSpot(TM) 64-Bit Server VM (build 12.0.1+12, mixed mode, sharing)

Also, can this tool work on videos as well ?

```
Author:
```
stefnotch
```
Text:
```

That is rather strange. The first message basically says that you have Java 8 (class file version 52.0) and need Java 12 (class file version 56.0). However, it appears that you have Java 12 installed.
I suppose you could check if there is a stray Java 8 version still installed on your system.

```
Author:
```
Suleman-Elahi
```
Text:
```

I installed JDK from here after googling it by myself and it seems to be working fine.
https://jdk.java.net/13/
Thanks...

```
Author:
```
MystesofEternity
```
Text:
```

@Suleman-Elahi Can you post your PATH variables in here? Censor/Remove/Redact your Windows username if need be but we need to find out if you have some hideous path that points to a Java 8 so we can further diagnose this problem.

```

## 31
Title:
```

        web cannot run
      
```
Author:
```
lephuhung
```
Text:
```

chrome cannot run with error on console
Uncaught DOMException: Failed to execute 'texImage2D' on 'WebGLRenderingContext': The image element contains cross-origin data, and may not be loaded. at createTexture (file:///E:/Download/Anime4K-master/Anime4K-master/web/main.js:56:12) at Scaler.inputImage (file:///E:/Download/Anime4K-master/Anime4K-master/web/main.js:487:21) at Image.inputImg.onload (file:///E:/Download/Anime4K-master/Anime4K-master/web/main.js:693:16) createTexture @ main.js:56 Scaler.inputImage @ main.js:487 inputImg.onload @ main.js:693 load (async) onLoad @ main.js:689 onload @ index.html:11

```
Author:
```
stefnotch
```
Text:
```

@lephuhung That's a limitation of some web browsers caused by directly opening the .html file. You would need a web-server to get around this limitation.
@bloc97
I think it'd be great if you could set up GitHub pages for this. Setting up GitHub pages just takes a bunch of clicks and ensures that a web demo is always available.

Click on the Settings tab and scroll down to the GitHub Pages section. Then select the master branch source and click on the Save.
Add an index.html to the root which just redirects you to the other index.html

<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=web">
        <title>Page Redirection</title>
    </head>
    <body>
        If you are not redirected automatically, <a href="web">click here</a>
    </body>
</html>

https://bloc97.github.io/Anime4K should be up after a few minutes


```
Author:
```
lephuhung
```
Text:
```


@lephuhung That's a limitation of some web browsers caused by directly opening the .html file. You would need a web-server to get around this limitation.
@bloc97
I think it'd be great if you could set up GitHub pages for this. Setting up GitHub pages just takes a bunch of clicks and ensures that a web demo is always available.

Click on the Settings tab and scroll down to the GitHub Pages section. Then select the master branch source and click on the Save.
Add an index.html to the root which just redirects you to the other index.html

<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=web">
        <title>Page Redirection</title>
    </head>
    <body>
        If you are not redirected automatically, <a href="web">click here</a>
    </body>
</html>


https://bloc97.github.io/Anime4K should be up after a few minutes


many thank to you, i dowloaded xampp and run anime4k perfecterly

```

## 19
Title:
```

        Reduce soft gradient banding
      
```
Author:
```
DextroseRe
```
Text:
```

Noticeable color banding in some instances.


```
Author:
```
bloc97
```
Text:
```

Reduced banding in Anime4K v1.0 Release Candidate





```

## 26
Title:
```

        Enhanced bob deinterlacing
      
```
Author:
```
moghingold
```
Text:
```

I believe Anime4K can be applied to another use case where a video signal has sharp edges and reduced color spaces: retro video games. Many retro video games were designed to have part or all of their video signal output 480i/576i, a signal that modern displays cannot natively interpret. While complex deinterlacing algorithms exist and may be suitable for full motion video, they introduce too much latency to video games to be desirable.
The current solution used by enthusiast retro gamers is to use devices like the Retro Tink 2x or the Open Source Scan Converter (OSSC) to perform an operation known as "bob deinterlacing" (so-named because of the noticeable up-and-down bobbing of stationary parts of the screen that have edges changing their height between fields). It is, intentionally, the most naive version of line-doubling, and produces usually-good-enough results with acceptably little image processing time.
The upscaling method described by Anime4k might be able to noticeably improve the visual quality of line-doubling without introducing a significant amount of signal latency by treating the 240/288 line resolution of each field as the source and the 480/576 line resolution as the target.
Prior to finding Anime4k, I also investigated alternative methods of deinterlacing. The best quality results, as with anime, were achieved with AI[0]. Unfortunately, the lowest latency achieved for SD content was between 13-14ms (nearly a full frame of delay for 60fps content), and was only possible using a workstation with an Intel i7-5930, 65GiB of RAM, and an Nvidia Titan GPU[0, pg 8]. Like with anime, real-time results will require a more direct approach. The low latency of Anime4k and the consistent edges of video game content may make Anime4k a viable alternative to bob deinterlacing.
If you decide that you are interested in possibly integrating Anime4k into realtime video game deinterlacing solutions, a good person to contact would be Markus Hiienkari (marqs on the Video Game Perfection forums), as he is the designer of the OSSC.
[0] Real-time Deep Video Deinterlacing by Zhu, Liu, Mao, and Wong from The Chinese University of Hong Kong

```

## 12
Title:
```

        Docker Container variant
      
```
Author:
```
kirinnee
```
Text:
```

Seems like it requires OpenCL, but is it possible to run it in docker containers for easier deployment on servers or cross-platform development?

```
Author:
```
stefnotch
```
Text:
```

Where did you get the impression that it requires OpenCL?

```
Author:
```
stefnotch
```
Text:
```

Regarding Docker container, yes, it could theoretically run inside a Docker container, however, seeing as how it's a realtime algorithm that can easily run on any platform, most likely even the web, I'm not quite seeing the point of using Docker? Is there some use-case that I'm overlooking.

```
Author:
```
kirinnee
```
Text:
```

Impression was from when I ran everything within docker containers: (I hate to post logs but..)
PS D:\same> docker run -v ${PWD}:/anime 4kanime ruby 4k.rb Aug 15, 2019 11:44:14 AM com.aparapi.internal.opencl.OpenCLLoader <clinit> SEVERE: Check your environment. Failed to load codegen native library  or possibly failed to locate opencl native library (opencl.dll/opencl.so). Ensure that OpenCL is in your PATH (windows) or in LD_LIBRARY_PATH (linux). Exception in thread "main" javax.imageio.IIOException: Can't read input file! at java.desktop/javax.imageio.ImageIO.read(ImageIO.java:1308) at com.bloc97.anime4k.Main.main(Main.java:36)
Host OS: Windows 10 Pro
Docker-image: openjdk:12-alpine
Perhaps its an alpine problem, I apologize for not checking if its an alpine problem before reporting, but I shall go do that tomorrow.
For starters, I prefer to not have Java installed on my computer.
Bu main reason being it makes if I were running servers that use the image to post-process image or anything of that sort, deployments will be much simpler than to write scripts to pre-install FFMPEG and JDK & curling the jar binary for every server spun up. Building it into a static image would make my other service dependent on it more readily.

```
Author:
```
stefnotch
```
Text:
```

Oh, you're right about the OpenCL usage. Anime4k apparently uses Arapi which in turn uses OpenCL to execute Java code on the GPU. This means that you need a Docker image with OpenCL support.

```
Author:
```
ddouglas87
```
Text:
```

It works without OpenCL but complains while running.
On Docker Ubuntu apt-get install -y ocl-icd-opencl-dev removes the complaining, but I don't notice a speed difference.

```
Author:
```
bloc97
```
Text:
```

The algorithm is so simple that it is easy to be bounded by the memory speed. (Copying the image back and forth from the System Memory to the GPU Buffers) If your CPU is powerful enough (Recent CPUs with 8+ cores) it might even outperform GPUs since PCIe lanes are not as fast as the memory bus.

```
Author:
```
kirinnee
```
Text:
```

I have created a PR for basic Dockerfile, to build an ubuntu image that's portable.
I also have another one that packs FFMPEG into the image and added a script upscales videos by splitting and merging them (quite slow due to the restart of image kernel each time), should I add a PR for that too?

```

## 8
Title:
```

        Question: Type of algorithm
      
```
Author:
```
HelpSeeker
```
Text:
```

Why describe this algorithm an as upscaling algorithm and not a sharpening algorithm? From what I understand it doesn't have anything to do with the actual scaling process and relies on conventional scaling algorithms.

```
Author:
```
bloc97
```
Text:
```

We have to define "what is upscaling". If you see bicubic upscaling as an higher order expansion of bilinear, this algorithm can also be seen as an enhancement to bilinear upscaling, as it can be used with it.
Bilinear is so trivial now that people do not even see it as "upscaling" anymore, so the fact that this algorithm, even used with something as trivial as Bilinear can achieve reasonable results, you can say that the heavy lifting of the upscaling operation was done by Anime4K, and not the bilinear step.
The main goal is to let users watch 1080p anime on 2160p screens. The most descriptive way of saying that is to call this an upscaling algorithm. But we know that technically, it is an iterative edge refinement algorithm.

```
Author:
```
HelpSeeker
```
Text:
```


Bilinear is so trivial now that people do not even see it as "upscaling" anymore

But that is simply wrong and you don't make the situation better by motivating people to use incorrect terminology.

you can say that the heavy lifting of the upscaling operation was done by Anime4K

I don't see the logic behind that statement. Your algorithm has simply nothing to do with the scaling process (the process of increasing the resolution of a video signal). You can chain many operations on a frame to get visually appealing results. That doesn't change the role of each operation.

But we know that technically, it is an iterative edge refinement algorithm.

That is the problem though. Not everyone knows and this will only cause further confusion. Is it really worth it to spread misinformation, just because people tend to be more interested in upscaling than edge refinement algorithms?

```
Author:
```
bloc97
```
Text:
```

By your definition most early neural network upscaling algorithms are not upscaling either.
Before the discovery of the effectiveness of Transposed Convolutions, most upscaling algorithms such as SRCNN and VDSR take as an input an already upscaled version of the low resolution image, with bilinear/bicubic filtering. The original implementation of waifu2x does this too, however I'm not sure if they still do it now that people are using Transposed Convolutions or PixelShuffle Layers everywhere.

```
Author:
```
HelpSeeker
```
Text:
```

Only if you restrict the definition of resolution to the amount of pixels. Image resolution can also refer to the detail an image holds, which is why super-resolution algorithms can fairly claim to increase the resolution of an image.

```
Author:
```
bloc97
```
Text:
```

Sorry but I just don't see the difference between
Low Resolution -> Bicubic -> VDSR -> High Resolution
and
Low Resolution -> Bicubic -> Anime4K -> High Resolution
The "Upscaling" algorithm in these two cases is not Bicubic, as its contribution is minimal.

```
Author:
```
HelpSeeker
```
Text:
```

Anime4K in no way increases the resolution (neither pixel- nor detail- wise). Anime4K alters the image in a very specific way, not with the goal to increase the resolution, but to make the content more pleasant for a certain audience (people who like sharp edges over everything else). In fact you destroy a lot of detail when running Anime4K.
From my perspective you are trying to sell me

Low Resolution -> Bicubic -> High Resolution -> Denoiser -> Altered High Resolution

as

Low Resolution -> Bicubic -> Denoiser -> High Resolution


```
Author:
```
bloc97
```
Text:
```

The smoothing of texture is something that can be taken care of with a better line detection algorithm, which is what we're currently working on.
Other upscalers use those better detection algorithms, and without them they will destroy texture too. The fact that such a simple algorithm that can be described in 5 lines of pseudocode works as well, we can incorporate all the techniques other algorithms use and it will only get better.
Otherwise even right now, if you take the Anime4K upscales and downscale them to 1080p, you will notice that the detail loss is minimal.

```
Author:
```
marcan
```
Text:
```

The waifu2x neural network actually uses 2x2 pixel duplication for the input (nearest neighbor), so yeah, it's technically a straight filter, not an upscaler.

```
Author:
```
woctezuma
```
Text:
```


The waifu2x neural network actually uses 2x2 pixel duplication for the input (nearest neighbor)

Do you have a reference for this?
If I quickly check the paper, I see that:

and that:

I think it makes sense to call Waifu2x a Super-Resolution algorithm.

As for Anime4k, it depends what the word encompasses. If it is the whole pipeline, then it is an upscaler. If it just the novel part, then it is a sharpening filter, which can be used in a larger pipeline to upscale anime images with a pleasing effect.
I think the confusion stems from the fact that @HelpSeeker thought Anime4k was claiming to do Super-Resolution, which it does not do because it is not adding information to the image, e.g. by merging several views, or by bringing in information learnt on other images.

```
Author:
```
bloc97
```
Text:
```

Depends on your definition of Super-Resolution too. If you define SR as recovering texture detail, then no, Anime4K is not a texture SR algorithm. However, it can recover lines from blurry upscales, thus can be considered a line SR algorithm.
I think the real confusion here is between SISR Algorithm and General-Purpose SISR Algorithm.
Anime4K is not a General-Purpose SISR Algorithm.
Waifu2x is not a General-Purpose SISR Algorithm since it was only trained on Anime Art. (With the exception of the waifu2x trained on pictures, but that's basically SRCNN with modifications.)
SRCNN is a General-Purpose SISR Algorithm since it can be trained on any subset of images from our universe.
Bicubic is a General-Purpose SISR Algorithm as it is not biased towards any kind of spatial data.
If you apply SR algorithms for MRI scans on real pictures, you would get garbage, yet it is still an SR algorithm. (And if you look carefully in the implementations MRI SR algorithm are similar to denoising algorithms, yet they are called SR.)

```
Author:
```
net2cn
```
Text:
```

Actually I have the same confusion after understanding this algorithm. It seems that it works as a sharpening algorithm like USM but specially designed for anime instead of upscaling algorithm like bicubic interpolation (which actually upscale your image to a bigger size).
However, it is still a very interesting method in these days when ML-based methods get heated too much. Thank you for sharing this.

```
Author:
```
marcan
```
Text:
```

Re: waifu2x using a box/nearest neighbor filter, see:
https://github.com/nagadomi/waifu2x/blob/master/lib/reconstruct.lua#L192

```
Author:
```
bloc97
```
Text:
```

After some thought and doing some research online, I finally understood why people thought this is not upscaling. I have added a small paragraph at the end of the FAQ dedicated to those people. Years of working in this field had made me understand the words differently than most people.
The action of de-blurring (gaussian) and super-resolution is known to be equivalent in this domain, but this was not the case for people less invested in image processing.
I apologize for any confusion my earlier comments might have given.

```

## 49
Title:
```

        Burned-In Subtitles on Videos looks weird when compared with other upscaler
      
```
Author:
```
Tsubajashi
```
Text:
```

Describe the bug
Burned-In Text on Video looks weird when compared with other upscaler.
To Reproduce
Steps to reproduce the behavior:

Open Any Video with burned-in Subs with mpv
See error

Expected behavior
Good Readable Text.
Screenshots
https://imgur.com/a/XrHuHKV

OS: Windows 10
Version 1.0rc2
Media Player: MPV (latest shinchiro build mpv-x86_64-20191013-git-a85fa2d)


```
Author:
```
bloc97
```
Text:
```

This will be fixed in the experimental AnimeSR variant of Anime4K using machine learning. It is currently very difficult to fix this in the vanilla algorithm due to its simplicity.

```
Author:
```
Tsubajashi
```
Text:
```

@bloc97 Sounds alright, thanks!

```

## 18
Title:
```

        The current HLSL implementation applies the algorithm on subtitles.
      
```
Author:
```
bloc97
```
Text:
```

Due to how MPC handles shaders, they are always applied after subtitles. I am not sure if it is changeable.
For MPV, the user can choose to not apply shaders on subtitles.

```

## 16
Title:
```

        2 questions
      
```
Author:
```
splinter21
```
Text:
```

1
https://github.com/bloc97/Anime4K/blob/master/Java_Instructions.md
how do you get the default upsampling scale first, by bicubic? or bilinear?of other methods? And then use the enhancement Anime4K method.
2
https://github.com/bloc97/Anime4K/blob/master/results/Graph.png?raw=true
how do you get the perceptual quality?

```
Author:
```
stefnotch
```
Text:
```

1

the image can be upscaled in advance with any algorithm the user prefers
-- https://github.com/bloc97/Anime4K/blob/master/Preprint.md

The Java application uses bicubic interpolation



Anime4K/java/src/main/java/com/bloc97/anime4k/Main.java


         Line 75
      in
      17340b1






 g2.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BICUBIC); 





2
https://github.com/bloc97/Anime4K/blob/master/Preprint.md#analysis

```
Author:
```
bloc97
```
Text:
```

More exactly, Mean Opinion Score from a dozen people comparing all the different algorithms, a few tests were to choose the best of 2, and a few were to rate all the algorithms from 0 to 10. The tests were double blind but we do know this is not rigorous enough to be considered a serious publication.
Also, to simulate real viewing conditions users were not able to pause the video or get closer to the screen. They viewed video clips of few seconds at the same distance to an 4K 30-inch monitor.

```
Author:
```
splinter21
```
Text:
```

@bloc97 how to set the Push_Strength and Push_Grad_Strength parameters when using?

```
Author:
```
stefnotch
```
Text:
```


Available parameters:
java -jar Anime4K.jar [File_In] [File_Out] (Scale) (Push_Strength) (Push_Grad_Strength)

is what the instructions say. What are you having troubles with?

```
Author:
```
stefnotch
```
Text:
```

@bloc97 Actually, am I overlooking something or is the documentation wrong about the order of the (Push_Strength) and (Push_Grad_Strength)



Anime4K/java/src/main/java/com/bloc97/anime4k/Main.java


        Lines 45 to 53
      in
      3d75fd6






 float pushStrength = scale / 6f; 



 float pushGradStrength = scale / 2f; 



 



 if (args.length >= 4) { 



     pushGradStrength = Float.parseFloat(args[3]); 



 } 



 if (args.length >= 5) { 



     pushStrength = Float.parseFloat(args[4]); 



 } 






```
Author:
```
splinter21
```
Text:
```

I mean that I don't know what does these two parmeters mean, how to set these two parameters to make the output image better?

```
Author:
```
bloc97
```
Text:
```

@stefnotch You are right, they are wrong. I must have overlooked the change when writing the md.

```
Author:
```
bloc97
```
Text:
```

@splinter21 You can play around with the settings and see what they do, but to put it simply, Push_Stength thins black lines.  Push_Grad_Strength is the edge refinement strength. The higher it is, the sharper the edges. Put it too high and you lose texture detail. But we are currently working on fixing this issue.

```
Author:
```
splinter21
```
Text:
```

I know. Thanks！

```

## 29
Title:
```

        Run through ffmpeg (or similar tool)
      
```
Author:
```
BeeeQueue
```
Text:
```

I've been googling around but haven't been able to find anything useful about running the shader on a video file and saving the output.

```
Author:
```
BeeeQueue
```
Text:
```

Nevermind, I just found https://github.com/k4yt3x/video2x

```
Author:
```
bloc97
```
Text:
```

I'm not familiar with FFMPEG scripting. We also didn't think of a good use scenario for that. Is there any particular reason you need to re-encode a video with this algorithm?
This was intended to be used as a on-line algorithm that can be toggled off at will, since we believe re-encoding a video using this is not ideal.

```

## 47
Title:
```

        Will there be an update for the hlsl version?
      
```
Author:
```
Artins90
```
Text:
```

Hi, I have been using your algorithm on top of NGU for the past 3 months or so.
I have noticed that the hlsl version has not been updated in quite a while.
I tried to convert the glsl shader to hlsl using glslang and SPIRV-Cross but I failed.
I would like to know if you are going to update the hlsl version in the future or if there is an easier way to convert the glsl shader.

```
Author:
```
amayra
```
Text:
```

i went to know i prefer to use madvr+player than MPV

```
Author:
```
bloc97
```
Text:
```

I cannot find MPC documentation about HLSL. Currently the GLSL code uses 3-4 extra textures to store intermediate values, but HLSL only provides one extra memory variable (the alpha channel).
However I think it would be possible to store multiple values in that single alpha channel by compressing the variables, but the quality won't be equal to the GLSL version.

```
Author:
```
rxvincent
```
Text:
```

So the GLSL version has better effect at this time?

```
Author:
```
bloc97
```
Text:
```

Version 0.9 for GLSL and HLSL have the same quality, but v1.0RC for GLSL has better quality.

```

## 11
Title:
```

        How does the method compare to Anisotropic diffusion or Total variation denoising?
      
```
Author:
```
woctezuma
```
Text:
```

How does the method compare to Anisotropic diffusion or Total variation denoising? Are there similarities in the approach?

```
Author:
```
bloc97
```
Text:
```

The technique is similar, but the objective function is different, they are minimizing ((Denoised Image - Noisy Image) + Laplacian of Denoised Image), while we are simply maximizing the gradient using a different kernel than the standard Discrete Laplacian operator.
We use the first order derivative while they use the second order derivative.

```

# Pull
## 37
Title:
```

        Added Dockerfile
      
```
Author:
```
kirinnee
```
Text:
```

Added Dockerfile and dockerignore for more portable (no installation needed) form.
Uses jdk12 image

```

## 48
Title:
```

        Fix sentence error
      
```
Author:
```
rjworks
```
Text:
```

Fix sentence error

```

## 38
Title:
```

        Fix GPU data fetching issue of ImageKernel.
      
```
Author:
```
Donny-Hikari
```
Text:
```

It is necessary to update runtype to the GPU after changing its value. The original code will generate unmodified images while running on GPU.

```

## 42
Title:
```

        Spelling changes
      
```
Author:
```
SLaGrave
```
Text:
```

Found this repo and am very interested in delving more into the code in the future.
Saw these small spelling tweaks and made them in class.

```

## 15
Title:
```

        updated README to comply with GitHub Flavored Markdown
      
```
Author:
```
k4yt3x
```
Text:
```

The README file has some headings that are incorrectly incremented. It also has a style that does not comply with GFM and regular Markdown conventions.
This PR aims to fix the problems mentioned above.

GFM: https://github.github.com/gfm/


```
Author:
```
bloc97
```
Text:
```

Thank you for the improvements, I did not know the existence of GFM specifications.

```

## 22
Title:
```

        v1.0 Release Candidate
      
```
Author:
```
DextroseRe
```
Text:
```


No description provided.


```

## 14
Title:
```

        Create CODE_OF_CONDUCT.md
      
```
Author:
```
bloc97
```
Text:
```


No description provided.


```

## 13
Title:
```

        Add //!DESC Anime4K 
      
```
Author:
```
GreyWing3
```
Text:
```

Add //!DESC Anime4K so that stats in mpv show user shader:Anime4k
Cunentlly shows user shade:unknown

```
Author:
```
bloc97
```
Text:
```

Thanks, we should also add a name for each of the passes.

```

