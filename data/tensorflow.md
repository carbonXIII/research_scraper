# tensorflow/tensorflow
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_tensorflow_python_autograph_g3doc_reference_common_errors_md](#_tensorflow_python_autograph_g3doc_reference_common_errors_md)

* [_tensorflow_security_advisory_tfsa_2018_003_md](#_tensorflow_security_advisory_tfsa_2018_003_md)

* [_tensorflow_security_advisory_tfsa_2018_005_md](#_tensorflow_security_advisory_tfsa_2018_005_md)

* [_tensorflow_c_README_md](#_tensorflow_c_README_md)

* [_tensorflow_lite_g3doc_guide_ios_md](#_tensorflow_lite_g3doc_guide_ios_md)

* [_github_ISSUE_TEMPLATE_50_other_issues_md](#_github_ISSUE_TEMPLATE_50_other_issues_md)

* [_tensorflow_python_debug_README_md](#_tensorflow_python_debug_README_md)

* [_tensorflow_lite_g3doc_guide_get_started_md](#_tensorflow_lite_g3doc_guide_get_started_md)

* [_tensorflow_lite_tools_evaluation_tasks_coco_object_detection_README_md](#_tensorflow_lite_tools_evaluation_tasks_coco_object_detection_README_md)

* [_tensorflow_tools_dockerfiles_readme_for_jupyter_md](#_tensorflow_tools_dockerfiles_readme_for_jupyter_md)

* [_tensorflow_lite_g3doc_r1_convert_python_api_md](#_tensorflow_lite_g3doc_r1_convert_python_api_md)

* [_tensorflow_lite_examples_android_app_README_md](#_tensorflow_lite_examples_android_app_README_md)

* [_tensorflow_lite_g3doc_performance_gpu_advanced_md](#_tensorflow_lite_g3doc_performance_gpu_advanced_md)

* [_tensorflow_compiler_mlir_g3doc_overview_md](#_tensorflow_compiler_mlir_g3doc_overview_md)

* [_tensorflow_lite_g3doc_guide_faq_md](#_tensorflow_lite_g3doc_guide_faq_md)

* [_tensorflow_lite_README_md](#_tensorflow_lite_README_md)

* [_tensorflow_lite_experimental_ios_TensorFlowLiteC_md](#_tensorflow_lite_experimental_ios_TensorFlowLiteC_md)

* [_tensorflow_lite_experimental_micro_README_md](#_tensorflow_lite_experimental_micro_README_md)

* [_tensorflow_compiler_mlir_tensorflow_tests_tf_saved_model_README_md](#_tensorflow_compiler_mlir_tensorflow_tests_tf_saved_model_README_md)

* [_tensorflow_lite_kernels_internal_reference_integer_ops_README_md](#_tensorflow_lite_kernels_internal_reference_integer_ops_README_md)

[- Inline](#Inline)

* [_tensorflow_tools_test_upload_test_benchmarks_py](#_tensorflow_tools_test_upload_test_benchmarks_py)

* [_tensorflow_python_data_benchmarks_from_tensor_slices_benchmark_py](#_tensorflow_python_data_benchmarks_from_tensor_slices_benchmark_py)

* [_third_party_mlir_tools_mlir_tblgen_OpDocGen_cpp](#_third_party_mlir_tools_mlir_tblgen_OpDocGen_cpp)

* [_tensorflow_lite_experimental_microfrontend_lib_noise_reduction_io_c](#_tensorflow_lite_experimental_microfrontend_lib_noise_reduction_io_c)

* [_third_party_mlir_lib_Dialect_QuantOps_IR_QuantTypes_cpp](#_third_party_mlir_lib_Dialect_QuantOps_IR_QuantTypes_cpp)

* [_tensorflow_python_ops_check_ops_py](#_tensorflow_python_ops_check_ops_py)

* [_tensorflow_python_grappler_memory_optimizer_test_py](#_tensorflow_python_grappler_memory_optimizer_test_py)

* [_tensorflow_tools_ci_build_windows_gpu_bazel_run_cc_test_windows_sh](#_tensorflow_tools_ci_build_windows_gpu_bazel_run_cc_test_windows_sh)

* [_tensorflow_examples_adding_an_op_zero_out_op_1_py](#_tensorflow_examples_adding_an_op_zero_out_op_1_py)

* [_tensorflow_python_kernel_tests_string_split_op_test_py](#_tensorflow_python_kernel_tests_string_split_op_test_py)

* [_tensorflow_python_data_experimental_benchmarks_map_and_batch_benchmark_py](#_tensorflow_python_data_experimental_benchmarks_map_and_batch_benchmark_py)

* [_tensorflow_python_kernel_tests_linalg_init_py](#_tensorflow_python_kernel_tests_linalg_init_py)

* [_tensorflow_python_ops_parallel_for_pfor_py](#_tensorflow_python_ops_parallel_for_pfor_py)

* [_tensorflow_tools_ci_build_builds_cmake_sh](#_tensorflow_tools_ci_build_builds_cmake_sh)

* [_tensorflow_python_ops_matmul_benchmark_test_py](#_tensorflow_python_ops_matmul_benchmark_test_py)

* [_tensorflow_tools_dockerfiles_tests_build_cpu_sh](#_tensorflow_tools_dockerfiles_tests_build_cpu_sh)

* [_tensorflow_python_keras_distribute_distributed_training_utils_test_py](#_tensorflow_python_keras_distribute_distributed_training_utils_test_py)

* [_tensorflow_python_profiler_internal_flops_registry_py](#_tensorflow_python_profiler_internal_flops_registry_py)

* [_tensorflow_python_keras_saving_saved_model_save_impl_py](#_tensorflow_python_keras_saving_saved_model_save_impl_py)

* [_tensorflow_python_compiler_tensorrt_test_reshape_transpose_test_py](#_tensorflow_python_compiler_tensorrt_test_reshape_transpose_test_py)

[- Issues](#Issues)

* [20075](#20075)

* [2885](#2885)

* [3069](#3069)

* [32351](#32351)

* [1702](#1702)

* [10712](#10712)

* [3593](#3593)

* [7956](#7956)

* [16979](#16979)

* [10819](#10819)

* [24919](#24919)

* [25314](#25314)

* [12546](#12546)

[- Pull](#Pull)

* [18846](#18846)

* [1302](#1302)

* [19999](#19999)

* [15901](#15901)

* [2110](#2110)

* [14298](#14298)

* [24983](#24983)

<!-- toc -->

# Info
## description
An Open Source Machine Learning Framework for Everyone

# Markdown
## _tensorflow_python_autograph_g3doc_reference_common_errors_md
```# AutoGraph reference

[Index](index.md)

## Common AutoGraph errors

### "WARNING: AutoGraph could not transform `<name>`"

This warning is output when AutoGraph could not convert a function, for an
unexpected reason. The error message contains the reason why the function could
not be converted, as well as guidance on how to proceed next.

Note: AutoGraph does not always output a warning. For example, constructors
are silently called without conversion.

When this warning is printed, the code returned by AutoGraph still executes, but
the functions indicated in the warning will be executed as they are, without
conversion. If the functions contain pure Python or graph code (for example,
they have no Tensor-dependent control flow), then the code is likely to still
run without error. However, if it contains any constructs that are only
supported in AutoGraph, expect subsequent exceptions.

Note: the warning is output to the [abseil](https://github.com/abseil/abseil-py)
logger, with `WARNING` severity. To direct these warnings to `stdout`, use
`tf.autograph.set_verbosity(0, True)`.

### "OperatorNotAllowedInGraphError: using a `tf.Tensor` as a Python `bool`"

This exception is raised whenever a `tf.Tensor` is type-cast as a Python `bool`,
in a context where eager execution is not active. The exception is only raised
when graph execution is active, for example inside a `@tf.function` with
AutoGraph turned off. It can be caused by using a `tf.Tensor` value as:

  * the condition of an `if` or `while` statement: `if <tensor>:`
  * the argument in a logical expression: `tensor and another_tensor`
  * the argument to the `bool` built-in: `bool(tensor)`

Note: These operations are allowed when executing eagerly.

Within the context of AutoGraph, it usually indicates eager-style control
flow that has not been converted by AutoGraph, for any reason.

When encountering this error, make sure that the function is either decorated
with `@tf.function`, or called from another function decorated in this way. Also
look at the console and logging output for conversion warnings (see the section
above).

### "OperatorNotAllowedInGraphError: iterating over `tf.Tensor`"

This exception is raised whenever you try to iterate over a `tf.Tensor`,
in a context where eager execution is not active. The exception is only raised
when graph execution is active, for example inside a `@tf.function` with
AutoGraph turned off. It can be caused by using a `tf.Tensor` value as:

  * the iterated of a `for` statement: `for i in tensor:`
  * the argument to the `iter` built-in: `iter(tensor)`

Note: These operations are allowed when executing eagerly.

This exception is similar to the previous example, and has similar causes and
remedies.

### "InaccessibleTensorError: The tensor `<name>` is defined in another function or code block"

This exception is common to code which attempts to obtain values calculated
within a `tf.cond`, `tf.while_loop`, or another `@tf.function` without using
functional style or through mutable collections. See
[Limitations](limitations.md) for more details.

### "StagingError: in converted code"

This exception is used by AutoGraph to wrap exceptions with custom constructors
that it cannot re-raise with the original type. See
[Error handling](error_handling.md) for more details. If your code uses custom
exceptions, expect them to be wrapped by this exception.

### "Unable to identify source code of lambda function"

This error usually appears in the context of a conversion warning. It indicates
that a lambda function could not be parsed (see [Limitations](limitations.md)).

This type of errors can usually be avoided by creating lambda functions in
separate simple assignments, for example:

'''
l = lambda <args>: <body>
'''
```
## _tensorflow_security_advisory_tfsa_2018_003_md
```## TFSA-2018-003: TensorFlow Lite TOCO FlatBuffer Parsing Vulnerability

### CVE Number

CVE-2018-8825

### Issue Description

The TensorFlow Lite TOCO compiler does not perform correct boundary checks when
reading from some fields within TFLite files. 

As background, TFLite files are based on the FlatBuffers serialization format,
which does not have bounds checking built-in, rather it relies on the clients to
handle the appropriate security checks by themselves.

In particular, TOCO is not performing correct bounds checks in the following places:
* Out of bounds read in TOCO in import.cc:42
* Null dereference in TOCO in import.cc:135
* Out of bounds read in TOCO in import.cc:104
* Null dereference in TOCO in import.cc:121
* Out of bounds read in TOCO in import.cc:62
* Out of bounds read in TOCO in operator.cc:48
* Out of bounds read in TOCO graph_transformations (propagate_fixed_sizes.cc:93)


### Impact

Users passing a malformed or malicious version of a TFLite graph into TOCO will
cause TOCO to crash or cause a buffer overflow, potentially allowing malicious
code to be executed.

### Vulnerable Versions

TensorFlow 1.5.0, 1.5.1, 1.6.0, 1.7.0

### Mitigation

We have patched the vulnerability in GitHub commits [41335abb](https://github.com/tensorflow/tensorflow/commit/41335abb46f80ca644b5738550daef6136ba5476) and
[8badd11d](https://github.com/tensorflow/tensorflow/commit/8badd11d875a826bd318ed439909d5c47a7fb811).
If users are running the TensorFlow TFLite TOCO compiler in production or on
untrusted data, they are encouraged to apply this patch.

Additionally, we have released TensorFlow version 1.7.1 to mitigate this
vulnerability.

### Credits

This issue was discovered by the Blade Team of Tencent.
```
## _tensorflow_security_advisory_tfsa_2018_005_md
```## TFSA-2018-005: Old Snappy Library Usage Resulting in Memcpy Parameter Overlap

### CVE Number

CVE-2018-7577

### Issue Description

TensorFlow checkpoint meta file uses Google's [https://github.com/google/snappy](snappy)
compression/decompression library. There is a memcpy-param-overlap issue in the
version of snappy currently used by TensorFlow.

### Impact

A maliciously crafted checkpoint meta file could cause TensorFlow to crash or
read from other parts of its process memory.

### Vulnerable Versions

TensorFlow 1.1.0, 1.2.0, 1.2.1, 1.3.0, 1.3.1, 1.4.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.7.0

### Mitigation

We have patched the vulnerability in GitHub commit
[dfa9921e](https://github.com/tensorflow/tensorflow/commit/dfa9921e6343727b05f42f8d4a918b19528ff994)
by upgrading the version of the snappy library used by TensorFlow to v1.1.7.

If users are loading untrusted checkpoints in TensorFlow, we encourage users to
apply the patch to upgrade snappy.

Additionally, we have released TensorFlow version 1.7.1 to mitigate this
vulnerability.

### Credits

This issue was discovered by the Blade Team of Tencent.
```
## _tensorflow_c_README_md
```# TensorFlow C API

- See [www.tensorflow.org/install/lang_c](https://www.tensorflow.org/install/lang_c)
- Nightly builds:
  - [Linux CPU-only](https://storage.googleapis.com/tensorflow-nightly/github/tensorflow/lib_package/libtensorflow-cpu-linux-x86_64.tar.gz)
  - [Linux GPU](https://storage.googleapis.com/tensorflow-nightly/github/tensorflow/lib_package/libtensorflow-gpu-linux-x86_64.tar.gz)
  - [MacOS CPU-only](https://storage.googleapis.com/tensorflow-nightly/github/tensorflow/lib_package/libtensorflow-cpu-darwin-x86_64.tar.gz)
```
## _tensorflow_lite_g3doc_guide_ios_md
```# iOS quickstart

To get started with TensorFlow Lite on iOS, we recommend exploring the following
example:

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios">iOS
image classification example</a>

For an explanation of the source code, you should also read
[TensorFlow Lite iOS image classification](https://www.tensorflow.org/lite/models/image_classification/ios).

This example app uses
[image classification](https://www.tensorflow.org/lite/models/image_classification/overview)
to continuously classify whatever it sees from the device's rear-facing camera,
displaying the top most probable classifications. It allows the user to choose
between a floating point or
[quantized](https://www.tensorflow.org/lite/performance/post_training_quantization)
model and select the number of threads to perform inference on.

Note: Additional iOS applications demonstrating TensorFlow Lite in a variety of
use cases are available in [Examples](https://www.tensorflow.org/lite/examples).

## Add TensorFlow Lite to your Swift or Objective-C project

TensorFlow Lite offers native iOS libraries written in
[Swift](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/swift)
and
[Objective-C](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/objc).
To get started quickly writing your own iOS code, we recommend using our
[Swift image classification example](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios)
as a starting point.

The sections below demonstrate how to add TensorFlow Lite Swift or Objective-C
to your project:

### CocoaPods developers

In your `Podfile`, add the TensorFlow Lite pod. Then, run `pod install`.

#### Swift

'''ruby
use_frameworks!
pod 'TensorFlowLiteSwift'
'''

#### Objective-C

'''ruby
pod 'TensorFlowLiteObjC'
'''

#### Specifying versions

There are stable releases, and nightly releases available for both
`TensorFlowLiteSwift` and `TensorFlowLiteObjC` pods. If you do not specify a
version constraint as in the above examples, CocoaPods will pull the latest
stable release by default.

You can also specify a version contraint. For example, if you wish to depend on
version 2.0.0, you can write the dependency as:

'''ruby
pod 'TensorFlowLiteSwift', '~> 2.0.0'
'''

This will ensure the latest available 2.x.y version of `TensorFlowLiteSwift` pod
is used in your app. Alternatively, if you want to depend on the nightly builds,
you can write:

'''ruby
pod 'TensorFlowLiteSwift', '0.0.1-nightly'
'''

This will allow you to use the latest features added to TensorFlow Lite. Note
that once the `Podfile.lock` file is created when you run `pod install` command
for the first time, the nightly library version will be locked at the current
date's version. If you wish to update the nightly library to the newer one, you
should run `pod update` command.

For more information on different ways of specifying version constraints, see
[Specifying pod versions](https://guides.cocoapods.org/using/the-podfile.html#specifying-pod-versions).

### Bazel developers

In your `BUILD` file, add the `TensorFlowLite` dependency to your target.

#### Swift

'''python
swift_library(
  deps = [
      "//tensorflow/lite/experimental/swift:TensorFlowLite",
  ],
)
'''

#### Objective-C

'''python
objc_library(
  deps = [
      "//tensorflow/lite/experimental/objc:TensorFlowLite",
  ],
)
'''

### Import the library

For Swift files, import the TensorFlow Lite module:

'''swift
import TensorFlowLite
'''

For Objective-C files, import the umbrella header:

'''objectivec
#import "TFLTensorFlowLite.h"
'''

Or, the module if you set `CLANG_ENABLE_MODULES = YES` in your Xcode project:

'''objectivec
@import TFLTensorFlowLite;
'''

Note: For CocoaPods developers who want to import the Objective-C TensorFlow
Lite module, you must also include `use_frameworks!` in your `Podfile`.
```
## _github_ISSUE_TEMPLATE_50_other_issues_md
```---
name: Other Issues
about: Use this template for any other non-support related issues

---

This template is for miscellaneous issues not covered by the other issue categories.

For questions on how to work with TensorFlow, or support for problems that are not verified bugs in TensorFlow, please go to [StackOverflow](https://stackoverflow.com/questions/tagged/tensorflow).

If you are reporting a vulnerability, please use the [dedicated reporting process](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md).

For high-level discussions about TensorFlow, please post to discuss@tensorflow.org, for questions about the development or internal workings of TensorFlow, or if you would like to know how to contribute to TensorFlow, please post to developers@tensorflow.org.
```
## _tensorflow_python_debug_README_md
```# TensorFlow Debugger (TFDBG)

[TOC]

TensorFlow Debugger (TFDBG) is a specialized debugger for TensorFlow's computation
graphs. It provides access to internal graph structures and tensor values at
TensorFlow runtime.

<!-- TODO(cais): Add release notes starting from 1.3. -->

## Why TFDBG?

In TensorFlow's current
[computation-graph framework](https://www.tensorflow.org/get_started/get_started#the_computational_graph),
almost all actual computation after graph construction happens in a single
Python function, namely
[tf.Session.run](https://www.tensorflow.org/api_docs/python/tf/Session#run).
Basic Python debugging tools such as [pdb](https://docs.python.org/2/library/pdb.html)
cannot be used to debug `Session.run`, due to the fact that TensorFlow's graph
execution happens in the underlying C++ layer. C++ debugging tools such as
[gdb](https://www.gnu.org/software/gdb/) are not ideal either, because of their
inability to recognize and organize the stack frames and variables in a way
relevant to TensorFlow's operations, tensors and other graph constructs.

TFDBG addresses these limitations. Among the features provided by TFDBG, the
following ones are designed to facilitate runtime debugging of TensorFlow
models:

* Easy access through session wrappers
* Easy integration with common high-level APIs, such as
  [TensorFlow Estimators](https://www.tensorflow.org/guide/estimators) and
  [Keras](https://keras.io/)
* Inspection of runtime tensor values and node connections
* Conditional breaking after runs that generate tensors satisfying given
  predicates, which makes common debugging tasks such as tracing the origin
  of infinities and [NaNs](https://en.wikipedia.org/wiki/NaN) easier
* Association of nodes and tensors in graphs with Python source lines
* Profiling of models at the level of graph nodes and Python source lines.
(Omitted internal-only feature)
* A [gRPC](https://grpc.io/)-based remote debugging protocol, which allows us to
  build a browser-based graphical user interface (GUI) for TFDBG: the
  [TensorBoard Debugger Plugin](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/plugins/debugger/README.md).

## How to use TFDBG?

* For a walkthrough of TFDBG command-line interface, see https://www.tensorflow.org/guide/debugger.
* For information on the web GUI of TFDBG (TensorBoard Debugger Plugin), see
  [this README](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/plugins/debugger/README.md).
* For programmatic use of the API of TFDBG, see https://www.tensorflow.org/api_docs/python/tfdbg.


## Related Publications

* Cai, S., Breck E., Nielsen E., Salib M., Sculley D. (2016) TensorFlow Debugger:
  Debugging Dataflow Graphs for Machine Learning. https://research.google.com/pubs/pub45789.html
```
## _tensorflow_lite_g3doc_guide_get_started_md
```# Get started with TensorFlow Lite

TensorFlow Lite provides all the tools you need to convert and run TensorFlow
models on mobile, embedded, and IoT devices. The following guide walks through
each step of the developer workflow and provides links to further instructions.

[TOC]

## 1. Choose a model

<a id="1_choose_a_model"></a>

A TensorFlow model is a data structure that contains the logic and knowledge of
a machine learning network trained to solve a particular problem.
There are many ways to obtain a TensorFlow model, from using pre-trained models
to training your own.

To use a model with TensorFlow Lite, you must convert a
full TensorFlow model into the TensorFlow Lite format—you
cannot create or train a model using TensorFlow Lite. So you must start with a
regular TensorFlow model, and then
[convert the model](#2_convert_the_model_format).

Note: TensorFlow Lite supports a limited subset of TensorFlow operations, so not
all models can be converted. For details, read about the
[TensorFlow Lite operator compatibility](ops_compatibility.md).


### Use a pre-trained model

The TensorFlow Lite team provides a set of pre-trained models that solve a
variety of machine learning problems. These models have been converted to work
with TensorFlow Lite and are ready to use in your applications.

The pre-trained models include:

*   [Image classification](../models/image_classification/overview.md)
*   [Object detection](../models/object_detection/overview.md)
*   [Smart reply](../models/smart_reply/overview.md)
*   [Pose estimation](../models/pose_estimation/overview.md)
*   [Segmentation](../models/segmentation/overview.md)

See our full list of pre-trained models in [Models](../models).

#### Models from other sources

There are many other places you can obtain pre-trained TensorFlow models,
including [TensorFlow Hub](https://www.tensorflow.org/hub). In most cases, these
models will not be provided in the TensorFlow Lite format, and you'll have to
[convert](#2_convert_the_model_format) them before use.

### Re-train a model (transfer learning)

Transfer learning allows you to take a trained model and re-train it to perform
another task. For example, an
[image classification](../models/image_classification/overview.md) model could
be retrained to recognize new categories of image. Re-training takes less time
and requires less data than training a model from scratch.

You can use transfer learning to customize pre-trained models to your
application. Learn how to perform transfer learning in the
<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android">Recognize
flowers with TensorFlow</a> codelab.

### Train a custom model

If you have designed and trained your own TensorFlow model, or you have trained
a model obtained from another source, you must
[convert it to the TensorFlow Lite format](#2_convert_the_model_format).

## 2. Convert the model

<a id="2_convert_the_model_format"></a>

TensorFlow Lite is designed to execute models efficiently on mobile and other
embedded devices with limited compute and memory resources. Some of
this efficiency comes from the use of a special format for storing models.
TensorFlow models must be converted into this format before they can be used by
TensorFlow Lite.

Converting models reduces their file size and introduces optimizations that do
not affect accuracy. The TensorFlow Lite converter provides options
that allow you to further reduce file size and increase speed of execution, with
some trade-offs.

Note: TensorFlow Lite supports a limited subset of TensorFlow operations, so not
all models can be converted. For details, read about the
[TensorFlow Lite operator compatibility](ops_compatibility.md).


### TensorFlow Lite converter

The [TensorFlow Lite converter](../convert) is a tool available as a Python API
that converts trained TensorFlow models into the TensorFlow Lite format. It can
also introduce optimizations, which are covered in section 4,
[Optimize your model](#4_optimize_your_model_optional).

The following example shows a
TensorFlow `SavedModel` being converted into the TensorFlow Lite format:

'''python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
'''

You can [convert TensorFlow 2.0 models](../convert/index.md) in a similar way.

The converter can also be used from the
[command line](../convert/cmdline.md), but the Python API is recommended.

### Options

The converter can convert from a variety of input types.

When [converting TensorFlow 1.x models](../convert/python_api.md), these are:

*   [SavedModel directories](https://www.tensorflow.org/guide/saved_model)
*   Frozen GraphDef (models generated by
    [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py))
*   [Keras](https://keras.io) HDF5 models
*   Models taken from a `tf.Session`

When [converting TensorFlow 2.x models](../convert/python_api.md), these are:

*   [SavedModel directories](https://www.tensorflow.org/guide/saved_model)
*   [`tf.keras` models](https://www.tensorflow.org/guide/keras/overview)
*   [Concrete functions](../convert/concrete_function.md)

The converter can be configured to apply various optimizations that can improve
performance or reduce file size. This is covered in section 4,
[Optimize your model](#4_optimize_your_model_optional).

### Ops compatibility

TensorFlow Lite currently supports a [limited subset of TensorFlow
operations](ops_compatibility.md). The long term goal is for all TensorFlow
operations to be supported.

If the model you wish to convert contains unsupported operations, you can use
[TensorFlow Select](ops_select.md) to include operations from TensorFlow. This
will result in a larger binary being deployed to devices.

## 3. Run inference with the model

<a id="3_use_the_tensorflow_lite_model_for_inference_in_a_mobile_app"></a>

*Inference* is the process of running data through a model to obtain
predictions. It requires a model, an interpreter, and input data.

### TensorFlow Lite interpreter

The [TensorFlow Lite interpreter](inference.md) is a library that takes a model
file, executes the operations it defines on input data, and provides access to
the output.

The interpreter works across multiple platforms and provides a simple API for
running TensorFlow Lite models from Java, Swift, Objective-C, C++, and Python.

The following code shows the interpreter being invoked from Java:

'''java
try (Interpreter interpreter = new Interpreter(tensorflow_lite_model_file)) {
  interpreter.run(input, output);
}
'''

### GPU acceleration and Delegates

Some devices provide hardware acceleration for machine learning operations. For
example, most mobile phones have GPUs, which can perform floating point matrix
operations faster than a CPU.

The speed-up can be substantial. For example, a MobileNet v1 image
classification model runs 5.5x faster on a Pixel 3 phone when GPU acceleration
is used.

The TensorFlow Lite interpreter can be configured with
[Delegates](../performance/delegates.md) to make use of hardware acceleration on
different devices. The [GPU Delegate](../performance/gpu.md) allows the
interpreter to run appropriate operations on the device's GPU.

The following code shows the GPU Delegate being used from Java:

'''java
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
Interpreter interpreter = new Interpreter(tensorflow_lite_model_file, options);
try {
  interpreter.run(input, output);
}
'''

To add support for new hardware accelerators you can
[define your own delegate](../performance/delegates.md#how_to_add_a_delegate).

### Android and iOS

The TensorFlow Lite interpreter is easy to use from both major mobile platforms.
To get started, explore the [Android quickstart](android.md) and
[iOS quickstart](ios.md) guides.
[Example applications](https://www.tensorflow.org/lite/examples) are available
for both platforms.

To obtain the required libraries, Android developers should use the
[TensorFlow Lite AAR](android.md#use_the_tensorflow_lite_aar_from_jcenter). iOS
developers should use the
[CocoaPods for Swift or Objective-C](ios.md#add_tensorflow_lite_to_your_swift_or_objective-c_project).

### Linux

Embedded Linux is an important platform for deploying machine learning. To get
started using Python to perform inference with your TensorFlow Lite models,
follow the [Python quickstart](python.md).

To instead install the C++ library, see the
build instructions for [Raspberry Pi](build_rpi.md) or
[Arm64-based boards](build_arm64.md) (for boards such as Odroid C2, Pine64, and
NanoPi).


### Microcontrollers

[TensorFlow Lite for Microcontrollers](../microcontrollers/overview.md) is an
experimental port of TensorFlow Lite aimed at microcontrollers and other devices
with only kilobytes of memory.

### Operations

If your model requires TensorFlow operations that are not yet implemented in
TensorFlow Lite, you can use [TensorFlow Select](ops_select.md) to use them in
your model. You'll need to build a custom version of the interpreter that
includes the TensorFlow operations.

You can use [Custom operators](ops_custom.md) to write your own operations, or
port new operations into TensorFlow Lite.

[Operator versions](ops_version.md) allows you to add new functionalities and
parameters into existing operations.

## 4. Optimize your model

<a id="4_optimize_your_model_optional"></a>

TensorFlow Lite provides tools to optimize the size and performance of your
models, often with minimal impact on accuracy. Optimized models may require
slightly more complex training, conversion, or integration.

Machine learning optimization is an evolving field, and TensorFlow Lite's
[Model Optimization Toolkit](#model-optimization-toolkit) is continually growing
as new techniques are developed.

### Performance

The goal of model optimization is to reach the ideal balance of performance,
model size, and accuracy on a given device.
[Performance best practices](../performance/best_practices.md) can help guide
you through this process.

### Quantization

By reducing the precision of values and operations within a model, quantization
can reduce both the size of model and the time required for inference. For many
models, there is only a minimal loss of accuracy.

The TensorFlow Lite converter makes it easy to quantize TensorFlow models. The
following Python code quantizes a `SavedModel` and saves it to disk:

'''python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quantized_model)
'''

TensorFlow Lite supports reducing precision of values from full floating point
to half-precision floats (float16) or 8-bit integers. There are trade-offs in
model size and accuracy for each choice, and some operations have optimized
implementations for these reduced precision types.

To learn more about quantization, see
[Post-training quantization](../performance/post_training_quantization.md).

### Model Optimization Toolkit

The [Model Optimization Toolkit](../performance/model_optimization.md) is a set
of tools and techniques designed to make it easy for developers to optimize
their models. Many of the techniques can be applied to all TensorFlow models and
are not specific to TensorFlow Lite, but they are especially valuable when
running inference on devices with limited resources.

## Next steps

Now that you're familiar with TensorFlow Lite, explore some of the following
resources:

*   If you're a mobile developer, visit [Android quickstart](android.md) or
    [iOS quickstart](ios.md).
*   If you're building Linux embedded devices, see the [Python quickstart](
    python.md) or C++ build instructions for [Raspberry Pi](build_rpi.md) and
    [Arm64-based boards](build_arm64.md).
*   Explore our [pre-trained models](../models).
*   Try our [example apps](https://www.tensorflow.org/lite/examples).
```
## _tensorflow_lite_tools_evaluation_tasks_coco_object_detection_README_md
```# Object Detection evaluation using the 2014 COCO minival dataset.

This binary evaluates the following parameters of TFLite models trained for the
**bounding box-based**
[COCO Object Detection](http://cocodataset.org/#detection-eval) task:

*   Native pre-processing latency
*   Inference latency
*   mean Average Precision (mAP) averaged across IoU thresholds from 0.5 to 0.95
    (in increments of 0.05) and all object categories.

The binary takes the path to validation images and a ground truth proto file as
inputs, along with the model and inference-specific parameters such as delegate
and number of threads. It outputs the metrics as a text proto to a file, similar
to the following:

'''
num_runs: 8059
process_metrics {
  object_detection_metrics {
    pre_processing_latency {
      last_us: 27197
      max_us: 61372
      min_us: 6166
      sum_us: 189403170
      avg_us: 23502.068494850479
    }
    inference_latency {
      last_us: 386378
      max_us: 412804
      min_us: 378841
      sum_us: 3122849071
      avg_us: 387498.33366422635 # Average Inference Latency.
    }
    inference_metrics {
      num_inferences: 8059 # Number of images evaluated.
    }
    average_precision_metrics {
      individual_average_precisions {
        iou_threshold: 0.5
        average_precision: 0.26113987
      }
      individual_average_precisions {
        iou_threshold: 0.55
        average_precision: 0.2456704
      }
      individual_average_precisions {
        iou_threshold: 0.6
        average_precision: 0.22885525
      }
      individual_average_precisions {
        iou_threshold: 0.65
        average_precision: 0.20678344
      }
      individual_average_precisions {
        iou_threshold: 0.7
        average_precision: 0.18185228
      }
      individual_average_precisions {
        iou_threshold: 0.75
        average_precision: 0.14681709 # AP at IoU threshold of 0.75.
      }
      individual_average_precisions {
        iou_threshold: 0.8
        average_precision: 0.107850626
      }
      individual_average_precisions {
        iou_threshold: 0.85
        average_precision: 0.061735578
      }
      individual_average_precisions {
        iou_threshold: 0.9
        average_precision: 0.017980274
      }
      individual_average_precisions {
        iou_threshold: 0.95
        average_precision: 0.0010084915
      }
      overall_mean_average_precision: 0.14596924 # Overall mAP average.
    }
  }
}
'''

To run the binary, please follow the
[Preprocessing section](#preprocessing-the-minival-dataset) to prepare the data,
and then execute the commands in the
[Running the binary section](#running-the-binary).

## Parameters

The binary takes the following parameters:

*   `model_file` : `string` \
    Path to the TFlite model file. It should accept images preprocessed in the
    Inception format, and the output signature should be similar to the
    [SSD MobileNet model](https://www.tensorflow.org/lite/models/object_detection/overview#output.):

*   `model_output_labels`: `string` \
    Path to labels that correspond to output of model. E.g. in case of
    COCO-trained SSD model, this is the path to a file where each line contains
    a class detected by the model in correct order, starting from 'background'.

A sample model & label-list combination for COCO can be downloaded from the
TFLite
[Hosted models page](https://www.tensorflow.org/lite/guide/hosted_models#object_detection).

*   `ground_truth_images_path`: `string` \
    The path to the directory containing ground truth images.

*   `ground_truth_proto`: `string` \
    Path to file containing tflite::evaluation::ObjectDetectionGroundTruth proto
    in text format. If left empty, mAP numbers are not provided.

The above two parameters can be prepared using the `preprocess_coco_minival`
script included in this folder.

*   `output_file_path`: `string` \
    The final metrics are dumped into `output_file_path` as a string-serialized
    instance of `tflite::evaluation::EvaluationStageMetrics`.

The following optional parameters can be used to modify the inference runtime:

*   `num_interpreter_threads`: `int` (default=1) \
    This modifies the number of threads used by the TFLite Interpreter for
    inference.

*   `delegate`: `string` \
    If provided, tries to use the specified delegate for accuracy evaluation.
    Valid values: "nnapi", "gpu".

### Debug Mode

The script also supports a debug mode with the following parameter:

*   `debug_mode`: `boolean` \
    Whether to enable debug mode. Per-image predictions are written to the
    output file along with metrics. NOTE: Its not possible to parse the output
    file as a proto in this mode, since it contains demarcations between
    per-file outputs for readability.

This mode lets you debug the output of an object detection model that isn't
necessarily trained on the COCO dataset (by leaving `ground_truth_proto` empty).
The model output signature would still need to follow the convention mentioned
above, and you we still need an output labels file.

## Preprocessing the minival dataset

To compute mAP in a consistent and interpretable way, we utilize the same 2014
COCO 'minival' dataset that is mentioned in the
[Tensorflow detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md).

The links to download the components of the validation set are:

*   [2014 COCO Validation Images](http://images.cocodataset.org/zips/val2014.zip)
*   [2014 COCO Train/Val annotations](http://images.cocodataset.org/annotations/annotations_trainval2014.zip):
    Out of the files from this zip, we only require `instances_val2014.json`.
*   [minival Image IDs](https://github.com/tensorflow/models/blob/master/research/object_detection/data/mscoco_minival_ids.txt) :
    Only applies to the 2014 validation set. You would need to copy the contents
    into a text file.

Since evaluation has to be performed on-device, we first filter the above data
and extract a subset that only contains the images & ground-truth bounding boxes
we need.

To do so, we utilize the `preprocess_coco_minival` Python binary as follows:

'''
bazel run //tensorflow/lite/tools/evaluation/tasks/coco_object_detection:preprocess_coco_minival -- \
  --images_folder=/path/to/val2014 \
  --instances_file=/path/to/instances_val2014.json \
  --whitelist_file=/path/to/minival_whitelist.txt \
  --output_folder=/path/to/output/folder

'''

Optionally, you can specify a `--num_images=N` argument, to preprocess the first
`N` image files (based on sorted list of filenames).

The script generates the following within the output folder:

*   `images/`: the resulting subset of the 2014 COCO Validation images.

*   `ground_truth.pbtxt`: a `.pbtxt` (text proto) file holding
    `tflite::evaluation::ObjectDetectionGroundTruth` corresponding to image
    subset.

## Running the binary

### On Android

(0) Refer to
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android
for configuring NDK and SDK.

(1) Build using the following command:

'''
bazel build -c opt \
  --config=android_arm64 \
  --cxxopt='--std=c++17' \
  //tensorflow/lite/tools/evaluation/tasks/coco_object_detection:run_eval
'''

(2) Connect your phone. Push the binary to your phone with adb push (make the
directory if required):

'''
adb push bazel-bin/third_party/tensorflow/lite/tools/evaluation/tasks/coco_object_detection/run_eval /data/local/tmp
'''

(3) Make the binary executable.

'''
adb shell chmod +x /data/local/tmp/run_eval
'''

(4) Push the TFLite model that you need to test:

'''
adb push ssd_mobilenet_v1_float.tflite /data/local/tmp
'''

(5) Push the model labels text file to device.

'''
adb push /path/to/labelmap.txt /data/local/tmp/labelmap.txt
'''

(6) Preprocess the dataset using the instructions given in the
[Preprocessing section](#preprocessing-the-minival-dataset) and push the data
(folder containing images & ground truth proto) to the device:

'''
adb shell mkdir /data/local/tmp/coco_validation && \
adb push /path/to/output/folder /data/local/tmp/coco_validation
'''

(7) Run the binary.

'''
adb shell /data/local/tmp/run_eval \
  --model_file=/data/local/tmp/ssd_mobilenet_v1_float.tflite \
  --ground_truth_images_path=/data/local/tmp/coco_validation/images \
  --ground_truth_proto=/data/local/tmp/coco_validation/ground_truth.pbtxt \
  --model_output_labels=/data/local/tmp/labelmap.txt \
  --output_file_path=/data/local/tmp/coco_output.txt
'''

Optionally, you could also pass in the `--num_interpreter_threads` &
`--delegate` arguments to run with different configurations.

### On Desktop

(1) Build and run using the following command:

'''
bazel run -c opt \
  --cxxopt='--std=c++11' \
  -- \
  //tensorflow/lite/tools/evaluation/tasks/coco_object_detection:run_eval \
  --model_file=/path/to/ssd_mobilenet_v1_float.tflite \
  --ground_truth_images_path=/path/to/images \
  --ground_truth_proto=/path/to/ground_truth.pbtxt \
  --model_output_labels=/path/to/labelmap.txt \
  --output_file_path=/path/to/coco_output.txt
'''
```
## _tensorflow_tools_dockerfiles_readme_for_jupyter_md
```Want more tutorials like these?

Check out tensorflow.org/tutorials!
```
## _tensorflow_lite_g3doc_r1_convert_python_api_md
```# Converter Python API guide

This page describes how to convert TensorFlow models into the TensorFlow Lite
format using the TensorFlow Lite Converter Python API.

If you're looking for information about how to run a TensorFlow Lite model,
see [TensorFlow Lite inference](../guide/inference.md).

Note: This page describes the converter in the TensorFlow nightly release,
installed using `pip install tf-nightly`. For docs describing older versions
reference ["Converting models from TensorFlow 1.12"](#pre_tensorflow_1.12).


## High-level overview

While the TensorFlow Lite Converter can be used from the command line, it is
often convenient to use in a Python script as part of the model development
pipeline. This allows you to know early that you are designing a model that can
be targeted to devices with mobile.

## API

The API for converting TensorFlow models to TensorFlow Lite is
`tf.lite.TFLiteConverter`, which provides class methods based on the original
format of the model. For example, `TFLiteConverter.from_session()` is available
for GraphDefs, `TFLiteConverter.from_saved_model()` is available for
SavedModels, and `TFLiteConverter.from_keras_model_file()` is available for
`tf.Keras` files.

Example usages for simple float-point models are shown in
[Basic Examples](#basic). Examples usages for more complex models is shown in
[Complex Examples](#complex).

## Basic examples <a name="basic"></a>

The following section shows examples of how to convert a basic float-point model
from each of the supported data formats into a TensorFlow Lite FlatBuffers.

### Exporting a GraphDef from tf.Session <a name="basic_graphdef_sess"></a>

The following example shows how to convert a TensorFlow GraphDef into a
TensorFlow Lite FlatBuffer from a `tf.Session` object.

'''python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
var = tf.get_variable("weights", dtype=tf.float32, shape=(1, 64, 64, 3))
val = img + var
out = tf.identity(val, name="out")

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
'''

### Exporting a GraphDef from file <a name="basic_graphdef_file"></a>

The following example shows how to convert a TensorFlow GraphDef into a
TensorFlow Lite FlatBuffer when the GraphDef is stored in a file. Both `.pb` and
`.pbtxt` files are accepted.

The example uses
[Mobilenet_1.0_224](https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz).
The function only supports GraphDefs frozen using
[freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py).

'''python
import tensorflow as tf

graph_def_file = "/path/to/Downloads/mobilenet_v1_1.0_224/frozen_graph.pb"
input_arrays = ["input"]
output_arrays = ["MobilenetV1/Predictions/Softmax"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
'''

### Exporting a SavedModel <a name="basic_savedmodel"></a>

The following example shows how to convert a SavedModel into a TensorFlow Lite
FlatBuffer.

'''python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
'''

For more complex SavedModels, the optional parameters that can be passed into
`TFLiteConverter.from_saved_model()` are `input_arrays`, `input_shapes`,
`output_arrays`, `tag_set` and `signature_key`. Details of each parameter are
available by running `help(tf.lite.TFLiteConverter)`.

### Exporting a tf.keras File <a name="basic_keras_file"></a>

The following example shows how to convert a `tf.keras` model into a TensorFlow
Lite FlatBuffer. This example requires
[`h5py`](http://docs.h5py.org/en/latest/build.html) to be installed.

'''python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("keras_model.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
'''

The `tf.keras` file must contain both the model and the weights. A comprehensive
example including model construction can be seen below.

'''python
import numpy as np
import tensorflow as tf

# Generate tf.keras model.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_shape=(3,)))
model.add(tf.keras.layers.RepeatVector(3))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(3)))
model.compile(loss=tf.keras.losses.MSE,
              optimizer=tf.keras.optimizers.RMSprop(lr=0.0001),
              metrics=[tf.keras.metrics.categorical_accuracy],
              sample_weight_mode='temporal')

x = np.random.random((1, 3))
y = np.random.random((1, 3, 3))
model.train_on_batch(x, y)
model.predict(x)

# Save tf.keras model in HDF5 format.
keras_file = "keras_model.h5"
tf.keras.models.save_model(model, keras_file)

# Convert to TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_file)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
'''

## Complex examples <a name="complex"></a>

For models where the default value of the attributes is not sufficient, the
attribute's values should be set before calling `convert()`. In order to call
any constants use `tf.lite.constants.<CONSTANT_NAME>` as seen below with
`QUANTIZED_UINT8`. Run `help(tf.lite.TFLiteConverter)` in the Python
terminal for detailed documentation on the attributes.

Although the examples are demonstrated on GraphDefs containing only constants.
The same logic can be applied irrespective of the input data format.

### Exporting a quantized GraphDef <a name="complex_quant"></a>

The following example shows how to convert a quantized model into a TensorFlow
Lite FlatBuffer.

'''python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
const = tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
val = img + const
out = tf.fake_quant_with_min_max_args(val, min=0., max=1., name="output")

with tf.Session() as sess:
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  converter.inference_type = tf.lite.constants.QUANTIZED_UINT8
  input_arrays = converter.get_input_arrays()
  converter.quantized_input_stats = {input_arrays[0] : (0., 1.)}  # mean, std_dev
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
'''


## Additional instructions

### Build from source code <a name="latest_package"></a>

In order to run the latest version of the TensorFlow Lite Converter Python API,
either install the nightly build with
[pip](https://www.tensorflow.org/install/pip) (recommended) or
[Docker](https://www.tensorflow.org/install/docker), or
[build the pip package from source](https://www.tensorflow.org/install/source).

### Converting models from TensorFlow 1.12 <a name="pre_tensorflow_1.12"></a>

Reference the following table to convert TensorFlow models to TensorFlow Lite in
and before TensorFlow 1.12. Run `help()` to get details of each API.

TensorFlow Version | Python API
------------------ | ---------------------------------
1.12               | `tf.contrib.lite.TFLiteConverter`
1.9-1.11           | `tf.contrib.lite.TocoConverter`
1.7-1.8            | `tf.contrib.lite.toco_convert`
```
## _tensorflow_lite_examples_android_app_README_md
```# TF Lite Android Example (Deprecated)

This example has been moved to the new
[TensorFlow examples repo](https://github.com/tensorflow/examples), and split
into several distinct examples:

*   [Image Classification](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android)
*   [Object Detection](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/android)
*   [Speech Commands](https://github.com/tensorflow/examples/tree/master/lite/examples/speech_commands/android)
```
## _tensorflow_lite_g3doc_performance_gpu_advanced_md
```# TensorFlow Lite on GPU

[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) supports several
hardware accelerators.  This document describes how to use the GPU backend using
the TensorFlow Lite delegate APIs on Android (requires OpenGL ES 3.1 or higher)
and iOS (requires iOS 8 or later).

## Benefits of GPU Acceleration

### Speed

GPUs are designed to have high throughput for massively parallelizable
workloads. Thus, they are well-suited for deep neural nets, which consist of a
huge number of operators, each working on some input tensor(s) that can be
easily divided into smaller workloads and carried out in parallel. This
parallelism typically results in lower latency. In the best scenario, inference
on the GPU may run fast enough to become suitable for real-time applications
that were not previously possible.

### Accuracy

GPUs do their computation with 16-bit or 32-bit floating point numbers and
(unlike the CPUs) do not require quantization for optimal performance. If
decreased accuracy made quantization untenable for your models, running your
neural network on a GPU may eliminate this concern.

### Energy Efficiency

Another benefit that comes with GPU inference is its power efficiency. A GPU
carries out computations in a very efficient and optimized way, consuming less
power and generating less heat than the same task run on a CPU.

## Supported Ops

TensorFlow Lite on GPU supports the following ops in 16-bit and 32-bit float
precision:

* `ADD v1`
* `AVERAGE_POOL_2D v1`
* `CONCATENATION v1`
* `CONV_2D v1`
* `DEPTHWISE_CONV_2D v1-2`
* `FULLY_CONNECTED v1`
* `LOGISTIC v1`
* `MAX_POOL_2D v1`
* `MUL v1`
* `PAD v1`
* `PRELU v1`
* `RELU v1`
* `RELU6 v1`
* `RESHAPE v1`
* `RESIZE_BILINEAR v1`
* `SOFTMAX v1`
* `STRIDED_SLICE v1`
* `SUB v1`
* `TRANSPOSE_CONV v1`

## Basic Usage

### Android (Java)

Run TensorFlow Lite on GPU with `TfLiteDelegate`. In Java, you can specify the
GpuDelegate through `Interpreter.Options`.

'''java
// NEW: Prepare GPU delegate.
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);

// Set up interpreter.
Interpreter interpreter = new Interpreter(model, options);

// Run inference.
writeToInputTensor(inputTensor);
interpreter.run(inputTensor, outputTensor);
readFromOutputTensor(outputTensor);

// Clean up.
delegate.close();
'''

### Android (C/C++)

For C/C++ usage of TensorFlow Lite GPU on Android, the GPU delegate can be
created with `TfLiteGpuDelegateCreate()` and destroyed with
`TfLiteGpuDelegateDelete()`.

'''c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.
const TfLiteGpuDelegateOptions options = {
  .metadata = NULL,
  .compile_options = {
    .precision_loss_allowed = 1,  // FP16
    .preferred_gl_object_type = TFLITE_GL_OBJECT_TYPE_FASTEST,
    .dynamic_batch_enabled = 0,   // Not fully functional yet
  },
};
auto* delegate = TfLiteGpuDelegateCreate(&options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// NEW: Clean up.
TfLiteGpuDelegateDelete(delegate);
'''

TFLite GPU for Android C/C++ uses the [Bazel](https://bazel.io) build system.
The delegate can be built, for example, using the following command:

'''sh
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:gl_delegate                  # for static library
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:libtensorflowlite_gpu_gl.so  # for dynamic library
'''

### iOS (ObjC++)

To use TensorFlow Lite on GPU, get the GPU delegate via `NewGpuDelegate()` and
then pass it to `Interpreter::ModifyGraphWithDelegate()` (instead of calling
`Interpreter::AllocateTensors()`).

'''c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
tflite::ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.

const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// Clean up.
DeleteGpuDelegate(delegate);
'''

Note: When calling `Interpreter::ModifyGraphWithDelegate()` or
`Interpreter::Invoke()`, the caller must have an `EGLContext` in the current
thread and `Interpreter::Invoke()` must be called from the same `EGLContext`. If
an `EGLContext` does not exist, the delegate will internally create one, but
then the developer must ensure that `Interpreter::Invoke()` is always called
from the same thread in which `Interpreter::ModifyGraphWithDelegate()` was
called.

## Advanced Usage

### Delegate Options for iOS

`NewGpuDelegate()` accepts a `struct` of options.

'''c++
struct GpuDelegateOptions {
  // Allows to quantify tensors, downcast values, process in float16 etc.
  bool allow_precision_loss;

  enum class WaitType {
    // waitUntilCompleted
    kPassive,
    // Minimize latency. It uses active spinning instead of mutex and consumes
    // additional CPU resources.
    kActive,
    // Useful when the output is used with GPU pipeline then or if external
    // command encoder is set
    kDoNotWait,
  };
  WaitType wait_type;
};
'''

Passing `nullptr` into `NewGpuDelegate()` sets the default options (which are
explicated in the Basic Usage example above).

'''c++

// THIS:
const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);

// IS THE SAME AS THIS:
auto* delegate = NewGpuDelegate(nullptr);

'''

While it is convenient to use `nullptr`, we recommend that you explicitly set
the options, to avoid any unexpected behavior if default values are changed in
the future.

### Input/Output Buffers

To do computation on the GPU, data must be made available to the GPU. This often
requires performing a memory copy. It is desirable not to cross the CPU/GPU
memory boundary if possible, as this can take up a significant amount of time.
Usually, such crossing is inevitable, but in some special cases, one or the
other can be omitted.

If the network's input is an image already loaded in the GPU memory (for
example, a GPU texture containing the camera feed) it can stay in the GPU memory
without ever entering the CPU memory. Similarly, if the network's output is in
the form of a renderable image (for example,
[image style transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)_)
it can be directly displayed on the screen.

To achieve best performance, TensorFlow Lite makes it possible for users to
directly read from and write to the TensorFlow hardware buffer and bypass
avoidable memory copies.

#### Android

Assuming the image input is in the GPU memory, it must first be converted to an
OpenGL Shader Storage Buffer Object (SSBO). You can associate a TfLiteTensor to
a user-prepared SSBO with `Interpreter.bindGlBufferToTensor()`. Note that
`Interpreter.bindGlBufferToTensor()` must be called before
`Interpreter.modifyGraphWithDelegate()`.

'''java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create an SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, inputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int inputSsboId = id[0];

// Create interpreter.
Interpreter interpreter = new Interpreter(tfliteModel);
Tensor inputTensor = interpreter.getInputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(inputTensor, inputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null input argument indicates use of the bound buffer for input.
fillSsboWithCameraImageTexture(inputSsboId);
float[] outputArray = new float[outputSize];
interpreter.runInference(null, outputArray);
'''

A similar approach can be applied to the output tensor. In that case,
`Interpreter.Options.setAllowBufferHandleOutput(true)` should be passed on, to
disable the default copying of the network's output from GPU memory to CPU
memory.

'''java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create a SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, outputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int outputSsboId = id[0];

// Create interpreter.
Interpreter.Options options = (new Interpreter.Options()).setAllowBufferHandleOutput(true);
Interpreter interpreter = new Interpreter(tfliteModel, options);
Tensor outputTensor = interpreter.getOutputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(outputTensor, outputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null output argument indicates use of the bound buffer for output.
ByteBuffer input = getCameraImageByteBuffer();
interpreter.runInference(input, null);
renderOutputSsbo(outputSsboId);
'''

#### iOS

Assuming the image input is in GPU memory, it must first be converted to a
`MTLBuffer` object for Metal. You can associate a TfLiteTensor to a
user-prepared `MTLBuffer` with `BindMetalBufferToTensor()`. Note that
`BindMetalBufferToTensor()` must be called before
`Interpreter::ModifyGraphWithDelegate()`. Additionally, the inference output is,
by default, copied from GPU memory to CPU memory. This behavior can be turned
off by calling `Interpreter::SetAllowBufferHandleOutput(true)` during
initialization.

'''c++
// Prepare GPU delegate.
auto* delegate = NewGpuDelegate(nullptr);
interpreter->SetAllowBufferHandleOutput(true);  // disable default gpu->cpu copy
if (!BindMetalBufferToTensor(delegate, interpreter->inputs()[0], user_provided_input_buffer)) return false;
if (!BindMetalBufferToTensor(delegate, interpreter->outputs()[0], user_provided_output_buffer)) return false;
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
if (interpreter->Invoke() != kTfLiteOk) return false;
'''

Note: Once the default behavior is turned off, copying the inference output from
GPU memory to CPU memory requires an explicit call to
`Interpreter::EnsureTensorDataIsReadable()` for each output tensor.

## Tips and Tricks

*   Some operations that are trivial on the CPU may be high cost on a GPU. One
    class of such operation includes various forms of reshape operations
    (including `BATCH_TO_SPACE`, `SPACE_TO_BATCH`, `SPACE_TO_DEPTH`, and similar
    operation). If these operations are not required (for example, they were
    inserted to help the network architect reason about the system but do not
    otherwise affect output), it is worth removing them for performance.

*   On a GPU, tensor data is sliced into 4-channels. Thus, a computation on a
    tensor of shape `[B, H, W, 5]` will perform about the same on a tensor of
    shape `[B, H, W, 8]`, but significantly worse than `[B, H, W, 4]`.

    *   For example, if the camera hardware supports image frames in RGBA,
        feeding that 4-channel input is significantly faster, because a memory
        copy (from 3-channel RGB to 4-channel RGBX) can be avoided.

*   For best performance, do not hesitate to re-train your classifier with
    mobile-optimized network architecture. That is a significant part of
    optimization for on-device inference.
```
## _tensorflow_compiler_mlir_g3doc_overview_md
```# MLIR

## Overview

MLIR, or Multi-Level Intermediate Representation, is a representation format
and library of compiler utilities that sits between the model representation
and low-level compilers/executors that generate hardware-specific code.

MLIR is, at its heart, a flexible infrastructure for modern optimizing
compilers. This means it consists of a specification for intermediate
representations (IR) and a code toolkit to perform transformations on that
representation. (In compiler parlance, as you move from higher-level
representations to lower-level representations, these transformations can be
called “lowerings”)

MLIR is highly influenced by [LLVM](https://llvm.org/) and unabashedly reuses
many great ideas from it. It has a flexible type system, and allows
representing, analyzing and transforming graphs combining multiple levels of
abstraction in the same compilation unit. These abstractions include TensorFlow
operations, nested polyhedral loop regions, and even LLVM instructions and fixed
hardware operations and types.

We expect MLIR to be of interest to many groups, including:

*   Compiler researchers and implementers looking to optimize performance and
    memory consumption of machine learning models
*   Hardware makers looking for a way to connect their hardware to TensorFlow,
    such as TPUs, portable neural hardware in phones, and other custom ASICs
*   People writing language bindings that want to take advantage of optimizing
    compilers and hardware acceleration.

The TensorFlow ecosystem contains a number of compilers and optimizers that
operate at multiple levels of the software and hardware stack. We expect the
gradual adoption of MLIF to simplify every aspect of this stack.

<img alt="MLIR overview diagram" src="./images/mlir-infra.svg"/>
```
## _tensorflow_lite_g3doc_guide_faq_md
```# Frequently Asked Questions

If you don't find an answer to your question here, please look through our
detailed documentation for the topic or file a
[GitHub issue](https://github.com/tensorflow/tensorflow/issues).

## Model Conversion

#### What formats are supported for conversion from TensorFlow to TensorFlow Lite?

The TensorFlow Lite converter supports the following formats:

*   SavedModels:
    [TFLiteConverter.from_saved_model](../convert/python_api.md#exporting_a_savedmodel_)
*   Frozen GraphDefs generated by
    [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py):
    [TFLiteConverter.from_frozen_graph](../convert/python_api.md#exporting_a_graphdef_from_file_)
*   tf.keras HDF5 models:
    [TFLiteConverter.from_keras_model_file](../convert/python_api.md#exporting_a_tfkeras_file_)
*   tf.Session:
    [TFLiteConverter.from_session](../convert/python_api.md#exporting_a_graphdef_from_tfsession_)

The recommended approach is to integrate the
[Python converter](../convert/python_api.md) into your model pipeline in order to
detect compatibility issues early on.

#### Why doesn't my model convert?

Since the number of TensorFlow Lite operations is smaller than TensorFlow's,
some inference models may not be able to convert. For unimplemented operations,
take a look at the question on
[missing operators](faq.md#why-are-some-operations-not-implemented-in-tensorflow-lite).
Unsupported operators include embeddings and LSTM/RNNs. For models with
LSTM/RNNs, you can also try the experimental API
[OpHint](https://www.tensorflow.org/api_docs/python/tf/lite/OpHint) to convert.
Models with control flow ops (Switch, Merge, etc) are not convertible at the
moment, but we are working on adding support for control flow in Tensorflow
Lite, please see
[GitHub issues](https://github.com/tensorflow/tensorflow/issues/28485).

For conversion issues not related to missing operations or control flow ops,
search our
[GitHub issues](https://github.com/tensorflow/tensorflow/issues?q=label%3Acomp%3Alite+)
or file a [new one](https://github.com/tensorflow/tensorflow/issues).

#### How do I determine the inputs/outputs for GraphDef protocol buffer?

The easiest way to inspect a graph from a `.pb` file is to use the
[summarize_graph](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/graph_transforms/README.md#inspecting-graphs)
tool.

If that approach yields an error, you can visualize the GraphDef with
[TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard) and
look for the inputs and outputs in the graph. To visualize a `.pb` file, use the
[`import_pb_to_tensorboard.py`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/import_pb_to_tensorboard.py)
script like below:

'''
python import_pb_to_tensorboard.py --model_dir <model path> --log_dir <log dir path>
'''

#### How do I inspect a `.tflite` file?

TensorFlow Lite models can be visualized using the
[visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py)
script in our repository.

*   [Clone the TensorFlow repository](https://www.tensorflow.org/install/source)
*   Run the `visualize.py` script with bazel:

'''
bazel run //tensorflow/lite/tools:visualize model.tflite visualized_model.html
'''

## Models & Operations

#### Why are some operations not implemented in TensorFlow Lite?

In order to keep TensorFlow Lite lightweight, only certain operations were used
in the converter. The [Compatibility Guide](ops_compatibility.md) provides a
list of operations currently supported by TensorFlow Lite.

If you don’t see a specific operation (or an equivalent) listed, it's likely
that it has not been prioritized. The team tracks requests for new operations on
GitHub [issue #21526](https://github.com/tensorflow/tensorflow/issues/21526).
Leave a comment if your request hasn’t already been mentioned.

In the meanwhile, you could try implementing a
[custom operator](ops_custom.md) or using a different model that only
contains supported operators. If binary size is not a constraint, try using
TensorFlow Lite with [select TensorFlow ops](ops_select.md).

#### How do I test that a TensorFlow Lite model behaves the same as the original TensorFlow model?

The best way to test the behavior of a TensorFlow Lite model is to use our API
with test data and compare the outputs to TensorFlow for the same inputs. Take a
look at our [Python Interpreter example](../convert/python_api.md) that generates
random data to feed to the interpreter.

## Optimization

#### How do I reduce the size of my converted TensorFlow Lite model?

[Post-training quantization](../performance/post_training_quantization.md) can be
used during conversion to TensorFlow Lite to reduce the size of the model.
Post-training quantization quantizes weights to 8-bits of precision from
floating-point and dequantizes them during runtime to perform floating point
computations. However, note that this could have some accuracy implications.

If retraining the model is an option, consider
[Quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize).
However, note that quantization-aware training is only available for a subset of
convolutional neural network architectures.

For a deeper understanding of different optimization methods, look at
[Model optimization](../performance/model_optimization.md).

#### How do I optimize TensorFlow Lite performance for my machine learning task?

The high-level process to optimize TensorFlow Lite performance looks something
like this:

*   *Make sure that you have the right model for the task.* For image
    classification, check out our [list of hosted models](hosted_models.md).
*   *Tweak the number of threads.* Many TensorFlow Lite operators support
    multi-threaded kernels. You can use `SetNumThreads()` in the
    [C++ API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L345)
    to do this. However, increasing threads results in performance variability
    depending on the environment.
*   *Use Hardware Accelerators.* TensorFlow Lite supports model acceleration for
    specific hardware using delegates. For example, to use Android’s Neural
    Networks API, call
    [`UseNNAPI`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L343)
    on the interpreter. Or take a look at our
    [GPU delegate tutorial](../performance/gpu.md).
*   *(Advanced) Profile Model.* The Tensorflow Lite
    [benchmarking tool](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark)
    has a built-in profiler that can show per-operator statistics. If you know
    how you can optimize an operator’s performance for your specific platform,
    you can implement a [custom operator](ops_custom.md).

For a more in-depth discussion on how to optimize performance, take a look at
[Best Practices](../performance/best_practices.md).
```
## _tensorflow_lite_README_md
```# TensorFlow Lite

TensorFlow Lite is TensorFlow's lightweight solution for mobile and embedded
devices. It enables low-latency inference of on-device machine learning models
with a small binary size and fast performance supporting hardware acceleration.

See the documentation: https://www.tensorflow.org/lite/
Documentation edits can be made here: [tensorflow/lite/g3doc](./g3doc/)
```
## _tensorflow_lite_experimental_ios_TensorFlowLiteC_md
```# TensorFlow Lite for iOS
- For Swift developers, add the `TensorFlowLiteSwift` pod to your Podfile. For
  Objective-C developers, add `TensorFlowLiteObjC`. See the TensorFlow Lite
  [Swift](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/swift)
  and
  [ObjC](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/objc)
  directories for more details.
```
## _tensorflow_lite_experimental_micro_README_md
```# TensorFlow Lite for Microcontrollers

This an experimental port of TensorFlow Lite aimed at micro controllers and
other devices with only kilobytes of memory. It doesn't require any operating
system support, any standard C or C++ libraries, or dynamic memory allocation,
so it's designed to be portable even to 'bare metal' systems. The core runtime
fits in 16KB on a Cortex M3, and with enough operators to run a speech keyword
detection model, takes up a total of 22KB.

## Table of Contents

-   [Getting Started](#getting-started)
    *   [Examples](#examples)
    *   [Getting Started with Portable Reference Code](#getting-started-with-portable-reference-code)
    *   [Building Portable Reference Code using Make](#building-portable-reference-code-using-make)
    *   [Building for the "Blue Pill" STM32F103 using Make](#building-for-the-blue-pill-stm32f103-using-make)
    *   [Building for "Hifive1" SiFive FE310 development board using Make](#building-for-hifive1-sifive-fe310-development-board)
    *   [Building for Ambiq Micro Apollo3Blue EVB using Make](#building-for-ambiq-micro-apollo3blue-evb-using-make)
        *   [Additional Apollo3 Instructions](#additional-apollo3-instructions)
    *   [Building for the Eta Compute ECM3531 EVB using Make](#Building-for-the-Eta-Compute-ECM3531-EVB-using-Make)

-   [Goals](#goals)

-   [Generating Project Files](#generating-project-files)

-   [Generating Arduino Libraries](#generating-arduino-libraries)

-   [How to Port TensorFlow Lite Micro to a New Platform](#how-to-port-tensorflow-lite-micro-to-a-new-platform)

    *   [Requirements](#requirements)
    *   [Getting Started](#getting-started-1)
    *   [Troubleshooting](#troubleshooting)
    *   [Optimizing for your Platform](#optimizing-for-your-platform)
    *   [Code Module Organization](#code-module-organization)
    *   [Working with Generated Projects](#working-with-generated-projects)
    *   [Supporting a Platform with Makefiles](#supporting-a-platform-with-makefiles)
    *   [Supporting a Platform with Emulation Testing](#supporting-a-platform-with-emulation-testing)
    *   [Implementing More Optimizations](#implementing-more-optimizations)

# Getting Started

## Examples

The fastest way to learn how TensorFlow Lite for Microcontrollers works is by
exploring and running our examples, which include application code and trained
TensorFlow models.

The following examples are available:

- [hello_world](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world)
  * Uses a very simple model, trained to reproduce a sine wave, to control an
    LED or animation
  * Application code for Arduino, SparkFun Edge, and STM32F746
  * Colab walkthrough of model training and conversion

- [micro_speech](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_speech)
  * Uses a 20 KB model to recognize keywords in spoken audio
  * Application code for Arduino, SparkFun Edge, and STM32F746
  * Python scripts for model training and conversion

- [person_detection](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/person_detection)
  * Uses a 250 KB model to recognize presence or absence of a person in images
    captured by a camera
  * Application code for SparkFun Edge

- [magic_wand](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/magic_wand)
  * Uses a 20 KB model to recognize gestures using accelerometer data
  * Application code for Arduino and SparkFun Edge

## Pre-generated Project Files

One of the challenges of embedded software development is that there are a lot
of different architectures, devices, operating systems, and build systems. We
aim to support as many of the popular combinations as we can, and make it as
easy as possible to add support for others.

If you're a product developer, we have build instructions or pre-generated
project files that you can download for the following platforms:

Device                                                                                         | Mbed                                                                           | Keil                                                                           | Make/GCC
---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------
[STM32F746G Discovery Board](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)     | [Download](https://drive.google.com/open?id=1OtgVkytQBrEYIpJPsE8F6GUKHPBS3Xeb) | -                                                                              | [Instructions](#generating-project-files)
["Blue Pill" STM32F103-compatible development board](https://github.com/google/stm32_bare_lib) | -                                                                              | -                                                                              | [Instructions](#building-for-the-blue-pill-stm32f103-using-make)
[Ambiq Micro Apollo3Blue EVB using Make](https://ambiqmicro.com/apollo-ultra-low-power-mcus/)  | -                                                                              | -                                                                              | [Instructions](#building-for-ambiq-micro-apollo3blue-evb-using-make)
[Generic Keil uVision Projects](http://www2.keil.com/mdk5/uvision/)                            | -                                                                              | [Download](https://drive.google.com/open?id=1Lw9rsdquNKObozClLPoE5CTJLuhfh5mV) | -
[Eta Compute ECM3531 EVB](https://etacompute.com/)                                             | -                                                                              | -                                                                              | [Instructions](#Building-for-the-Eta-Compute-ECM3531-EVB-using-Make)

If your device is not yet supported, it may not be too hard to add support. You
can learn about that process
[here](#how-to-port-tensorflow-lite-micro-to-a-new-platform). We're looking
forward to getting your help expanding this table!

## Getting Started with Portable Reference Code

If you don't have a particular microcontroller platform in mind yet, or just
want to try out the code before beginning porting, the easiest way to begin is
by
[downloading the platform-agnostic reference code](https://drive.google.com/open?id=1cawEQAkqquK_SO4crReDYqf_v7yAwOY8).
You'll see a series of folders inside the archive, with each one containing just
the source files you need to build one binary. There is a simple Makefile for
each folder, but you should be able to load the files into almost any IDE and
build them. There's also a [Visual Studio Code](https://code.visualstudio.com/) project file already set up, so
you can easily explore the code in a cross-platform IDE.

## Building Portable Reference Code using Make

It's easy to build portable reference code directly from GitHub using make if
you're on a Linux or OS X machine with an internet connection.

-   Open a terminal
-   Download the TensorFlow source with `git clone
    https://github.com/tensorflow/tensorflow.git`
-   Enter the source root directory by running `cd tensorflow`
-   Build and test the library with `make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile test`

You should see a series of compilation steps, followed by `~~~ALL TESTS
PASSED~~~` for the various tests of the code that it will run. If there's an
error, you should get an informative message from make about what went wrong.

These tests are all built as simple binaries with few dependencies, so you can
run them manually. For example, here's how to run the depthwise convolution
test, and its output:

'''
tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/bin/depthwise_conv_test

Testing SimpleTest
Testing SimpleTestQuantized
Testing SimpleTestRelu
Testing SimpleTestReluQuantized
4/4 tests passed
~ALL TESTS PASSED~~~
'''

Looking at the
[depthwise_conv_test.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/depthwise_conv_test.cc)
code, you'll see a sequence that looks like this:

'''
...
TF_LITE_MICRO_TESTS_BEGIN

TF_LITE_MICRO_TEST(SimpleTest) {
...
}
...
TF_LITE_MICRO_TESTS_END
'''

These macros work a lot like
[the Google test framework](https://github.com/google/googletest), but they
don't require any dependencies and just write results to stderr, rather than
aborting the program. If all the tests pass, then `~~~ALL TESTS PASSED~~~` is
output, and the test harness that runs the binary during the make process knows
that everything ran correctly. If there's an error, the lack of the expected
string lets the harness know that the test failed.

So, why are we running tests in this complicated way? So far, we've been
building binaries that run locally on the Mac OS or Linux machine you're
building on, but this approach becomes important when we're targeting simple
micro controller devices.

## Building for the "Blue Pill" STM32F103 using Make

The goal of this library is to enable machine learning on resource-constrained
micro controllers and DSPs, and as part of that we've targeted the
["Blue Pill" STM32F103-compatible development board](https://github.com/google/stm32_bare_lib)
as a cheap and popular platform. It only has 20KB of RAM and 64KB of flash, so
it's a good device to ensure we can run efficiently on small chips.

It's fairly easy to
[buy and wire up a physical board](https://github.com/google/stm32_bare_lib#wiring-up-your-blue-pill),
but even if you don't have an actual device, the
[Renode project](https://renode.io/) makes it easy to run a faithful emulation
on your desktop machine. You'll need [Docker](https://www.docker.com/)
installed, but once you have that set up, try running the following command:

`make -f tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=bluepill
test`

You should see a similar set of outputs as you did in the previous section, with
the addition of some extra Docker logging messages. These are because we're
using Docker to run the Renode micro controller emulation tool, and the tests
themselves are being run on a simulated STM32F103 device. The communication
channels between an embedded device and the host are quite limited, so the test
harness looks at the output of the debug log to see if tests have passed, just
as it did in the previous section. This makes it a very flexible way to run
cross-platform tests, even when a platform has no operating system facilities,
as long as it can output debugging text logs.

To understand what's happening here, try running the same depthwise convolution
test, but through the emulated device test harness, with the following command:

'''
tensorflow/lite/experimental/micro/testing/test_bluepill_binary.sh \
tensorflow/lite/experimental/micro/tools/make/gen/bluepill_cortex-m3/bin/depthwise_conv_test \
'~~~ALL TESTS PASSED~~~'

'''

You should see output that looks something like this:

'''
Sending build context to Docker daemon   21.5kB
Step 1/2 : FROM antmicro/renode:latest
 ---> 1b670a243e8f
Step 2/2 : LABEL maintainer="Pete Warden <petewarden@google.com>"
 ---> Using cache
 ---> 3afcd410846d
Successfully built 3afcd410846d
Successfully tagged renode_bluepill:latest
LOGS:
...
03:27:32.4340 [INFO] machine-0: Machine started.
03:27:32.4790 [DEBUG] cpu.uartSemihosting: [+0.22s host +0s virt 0s virt from start] Testing SimpleTest
03:27:32.4812 [DEBUG] cpu.uartSemihosting: [+2.21ms host +0s virt 0s virt from start]   Testing SimpleTestQuantized
03:27:32.4833 [DEBUG] cpu.uartSemihosting: [+2.14ms host +0s virt 0s virt from start]   Testing SimpleTestRelu
03:27:32.4834 [DEBUG] cpu.uartSemihosting: [+0.18ms host +0s virt 0s virt from start]   Testing SimpleTestReluQuantized
03:27:32.4838 [DEBUG] cpu.uartSemihosting: [+0.4ms host +0s virt 0s virt from start]   4/4 tests passed
03:27:32.4839 [DEBUG] cpu.uartSemihosting: [+41µs host +0s virt 0s virt from start]   ~~~ALL TESTS PASSED~~~
03:27:32.4839 [DEBUG] cpu.uartSemihosting: [+5µs host +0s virt 0s virt from start]
...
tensorflow/lite/experimental/micro/tools/make/gen/bluepill_cortex-m3/bin/depthwise_conv_test: PASS
'''

There's a lot of output here, but you should be able to see that the same tests
that were covered when we ran locally on the development machine show up in the
debug logs here, along with the magic string `~~~ALL TESTS PASSED~~~`. This is
the exact same code as before, just compiled and run on the STM32F103 rather
than your desktop. We hope that the simplicity of this testing approach will
help make adding support for new platforms as easy as possible.

## Building for "Hifive1" SiFive FE310 development board

We've targeted the
["HiFive1" Arduino-compatible development board](https://www.sifive.com/boards/hifive1)
as a test platform for RISC-V MCU.

Similar to Blue Pill setup, you will need Docker installed. The binary can be
executed on either HiFive1 board or emulated using
[Renode project](https://renode.io/) on your desktop machine.

The following instructions builds and transfers the source files to the Docker
`docker build -t riscv_build \ -f
{PATH_TO_TENSORFLOW_ROOT_DIR}/tensorflow/lite/experimental/micro/testing/Dockerfile.riscv
\ {PATH_TO_TENSORFLOW_ROOT_DIR}/tensorflow/lite/experimental/micro/testing/`

You should see output that looks something like this:

'''
Sending build context to Docker daemon  28.16kB
Step 1/4 : FROM antmicro/renode:latest
 ---> 19c08590e817
Step 2/4 : LABEL maintainer="Pete Warden <petewarden@google.com>"
 ---> Using cache
 ---> 5a7770d3d3f5
Step 3/4 : RUN apt-get update
 ---> Using cache
 ---> b807ab77eeb1
Step 4/4 : RUN apt-get install -y curl git unzip make g++
 ---> Using cache
 ---> 8da1b2aa2438
Successfully built 8da1b2aa2438
Successfully tagged riscv_build:latest
'''

Building micro_speech_test binary

-   Launch the Docker that we just created using: `docker run -it-v
    /tmp/copybara_out:/workspace riscv_build:latest bash`
-   Enter the source root directory by running `cd /workspace`
-   Set the path to RISC-V tools: `export
    PATH=${PATH}:/workspace/tensorflow/lite/experimental/micro/tools/make/downloads/riscv_toolchain/bin/`
-   Build the binary: `make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=riscv32_mcu`

Launching Renode to test the binary, currently this set up is not automated.

-   Execute the binary on Renode: `renode -P 5000 --disable-xwt -e 's
    @/workspace/tensorflow/lite/experimental/micro/testing/sifive_fe310.resc'`

You should see the following log with the magic string `~~~ALL TEST PASSED~~~`:

'''
02:25:22.2059 [DEBUG] uart0: [+17.25s host +80ms virt 80ms virt from start] core freq at 0 Hz
02:25:22.2065 [DEBUG] uart0: [+0.61ms host +0s virt 80ms virt from start]   Testing TestInvoke
02:25:22.4243 [DEBUG] uart0: [+0.22s host +0.2s virt 0.28s virt from start]   Ran successfully
02:25:22.4244 [DEBUG] uart0: [+42µs host +0s virt 0.28s virt from start]
02:25:22.4245 [DEBUG] uart0: [+0.15ms host +0s virt 0.28s virt from start]   1/1 tests passed
02:25:22.4247 [DEBUG] uart0: [+62µs host +0s virt 0.28s virt from start]   ~~~ALL TESTS PASSED~~~
02:25:22.4251 [DEBUG] uart0: [+8µs host +0s virt 0.28s virt from start]
02:25:22.4252 [DEBUG] uart0: [+0.39ms host +0s virt 0.28s virt from start]
02:25:22.4253 [DEBUG] uart0: [+0.16ms host +0s virt 0.28s virt from start]   Progam has exited with code:0x00000000
'''

## Building for Ambiq Micro Apollo3Blue EVB using Make

Follow these steps to get the micro_speech yes example working on Apollo 3 EVB:

1.  Make sure to run the "Building Portable Reference Code using Make" section
    before performing the following steps
2.  Compile the project with the following command: make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=apollo3evb
    micro_speech_bin
3.  Install [Segger JLink tools](https://www.segger.com/downloads/jlink/)
4.  Connect the Apollo3 EVB (with mic shield in slot 3 of Microbus Shield board)
    to the computer and power it on.
5.  Start the GDB server in a new terminal with the following command:
    JLinkGDBServer -select USB -device AMA3B1KK-KBR -endian little -if SWD
    -speed 1000 -noir -noLocalhostOnly
    1.  The command has run successfully if you see the message "Waiting for GDB
        connection"
6.  Back in the original terminal, run the program via the debugger
    1.  Navigate to
        tensorflow/lite/experimental/micro/examples/micro_speech/apollo3evb
    2.  Start gdb by entering the following command: arm-none-eabi-gdb
    3.  Run the command script by entering the following command: source
        micro_speech.cmd. This script does the following:
        1.  Load the binary created in step 2
        2.  Reset
        3.  Begin program execution
        4.  Press Ctrl+c to exit
    4.  The EVB LEDs will indicate detection.
        1.  LED0 (rightmost LED) - ON when Digital MIC interface is initialized
        2.  LED1 - Toggles after each inference
        3.  LED2 thru 4 - "Ramp ON" when "Yes" is detected
    5.  Say "Yes"

### Additional Apollo3 Instructions

To flash a part with JFlash Lite, do the following:

1.  At the command line: JFlashLiteExe
2.  Device = AMA3B1KK-KBR
3.  Interface = SWD at 1000 kHz
4.  Data file =
    `tensorflow/lite/experimental/micro/tools/make/gen/apollo3evb_cortex-m4/bin/micro_speech.bin`
5.  Prog Addr = 0x0000C000

## Building for the Eta Compute ECM3531 EVB using Make

1.  Follow the instructions at
    [Tensorflow Micro Speech](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_speech#getting-started)
    to down load the Tensorflow source code and the support libraries \(but do
    not run the make command shown there.\)
2.  Download the Eta Compute SDK, version 0.0.17. Contact info@etacompute.com
3.  You will need the Arm compiler arm-none-eabi-gcc, version 7.3.1
    20180622, release ARM/embedded-7-branch revision 261907, 7-2018-q2-update.
    This compiler is downloaded through make.
4.  Edit the file
    tensorflow/lite/experimental/micro/tools/make/targets/ecm3531_makefile.inc
    so that the variables ETA_SDK and GCC_ARM point to the correct directories.
5.  Compile the code with the command \
    &nbsp;&nbsp;&nbsp;&nbsp;make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=ecm3531
    TAGS="CMSIS" test \
    This will produce a set of executables in the
    tensorflow/lite/experimental/micro/tools/make/gen/ecm3531_cortex-m3/bin
    directory.
6.  To load an executable into SRAM \
    &nbsp;&nbsp;&nbsp;&nbsp;Start ocd \
    &nbsp;&nbsp;&nbsp;&nbsp;cd
    tensorflow/lite/experimental/micro/tools/make/targets/ecm3531 \
    &nbsp;&nbsp;&nbsp;&nbsp;./load_program name_of_executable, for e.g.,
    ./load_program audio_provider_test \
    &nbsp;&nbsp;&nbsp;&nbsp;Start PuTTY \(Connection type = Serial, Speed =
    11520, Data bits = 8, Stop bits = 1, Parity = None\) \
    The following output should appear: \
    Testing TestAudioProvider \
    Testing TestTimer \
    2/2 tests passed \
    \~\~\~ALL TESTS PASSED\~\~\~ \
    Execution time \(msec\) = 7
7.  To load into flash \
    &nbsp;&nbsp;&nbsp;&nbsp;Edit the variable ETA_LDS_FILE in
    tensorflow/lite/experimental/micro/tools/&nbsp;&nbsp;make/targets/ecm3531_makefile.inc
    to point to the ecm3531_flash.lds file \
    &nbsp;&nbsp;&nbsp;&nbsp;Recompile \( make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=ecm3531
    TAGS="CMSIS" test\) \
    &nbsp;&nbsp;&nbsp;&nbsp;cd
    tensorflow/lite/experimental/micro/tools/make/targets/ecm3531 \
    &nbsp;&nbsp;&nbsp;&nbsp;./flash_program executable_name to load into flash.

## Implement target optimized kernels

The reference kernels in tensorflow/lite/experimental/micro/kernels are
implemented in pure C/C++. It might not utilize all HW architecture specific
optimizations, such as DSP instructions etc. The instructions below provides an
example on how to compile an external lib with HW architecture specific
optimizations and link it with the microlite lib.

### CMSIS-NN optimized kernels (---under development---)

To utilize the CMSIS-NN optimized kernels, choose your target, e.g. Bluepill,
and build with:

'''
make -f tensorflow/lite/experimental/micro/tools/make/Makefile TAGS=cmsis-nn TARGET=bluepill test
'''

That will build the microlite lib including CMSIS-NN optimized kernels based on
the version downloaded by 'download_dependencies.sh', so make sure you have run
this script. If you want to utilize another version of CMSIS, clone it to a
custom location run the following command:

'''
make -f tensorflow/lite/experimental/micro/tools/make/Makefile CMSIS_PATH=<CUSTOM_LOCATION> TAGS=cmsis-nn TARGET=bluepill test
'''

To test the optimized kernel(s) on your target platform using mbed (depthwise
conv in this example), follow these steps:

1.  Clone CMSIS to a custom location (<CUSTOM_LOCATION>) url:
    https://github.com/ARM-software/CMSIS_5.git Make sure you're on the
    development branch.
2.  Generate the project for depthwise conv mbed test: `make -f
    tensorflow/lite/experimental/micro/tools/make/Makefile TAGS=cmsis-nn
    CMSIS_PATH=<CUSTOM_LOCATION> generate_depthwise_conv_test_mbed_project`
3.  Go to the generated mbed folder: `cd
    tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/depthwise_conv_test/mbed`
4.  Follow the steps in README_MBED.md to setup the environment. Or simply do:
    `mbed config root . mbed deploy python -c 'import fileinput, glob; for
    filename in glob.glob("mbed-os/tools/profiles/*.json"): for line in
    fileinput.input(filename, inplace=True):
    print(line.replace("\"-std=gnu++98\"","\"-std=gnu++11\",
    \"-fpermissive\""))'`
5.  Compile and flash. The 'auto' flag requires your target to be plugged in.
    `mbed compile -m auto -t GCC_ARM -f --source . --source
    <CUSTOM_LOCATION>/CMSIS/NN/Include --source
    <CUSTOM_LOCATION>/CMSIS/NN/Source --source
    <CUSTOM_LOCATION>/CMSIS/DSP/Include --source
    <CUSTOM_LOCATION>/CMSIS/Core/Include -DARM_MATH_DSP -DARM_MATH_LOOPUNROLL
    -j8`

## Goals

The design goals are for the framework to be:

-   **Readable**: We want embedded software engineers to be able to understand
    what's required to run ML inference without having to study research papers.
    We've tried to keep the code base small, modular, and have reference
    implementations of all operations to help with this.

-   **Easy to modify**: We know that there are a lot of different platforms and
    requirements in the embedded world, and we don't expect to cover all of them
    in one framework. Instead, we're hoping that it can be a good starting point
    for developers to build on top of to meet their own needs. For example, we
    tried to make it easy to replace the implementations of key computational
    operators that are often crucial for performance, without having to touch
    the data flow and other runtime code. We want it to make more sense to use
    our workflow to handle things like model import and less-important
    operations, and customize the parts that matter, rather than having to
    reimplement everything in your own engine.

-   **Well-tested**: If you're modifying code, you need to know if your changes
    are correct. Having an easy way to test lets you develop much faster. To
    help there, we've written tests for all the components, and we've made sure
    that the tests can be run on almost any platform, with no dependencies apart
    from the ability to log text to a debug console somewhere. We also provide
    an easy way to run all the tests on-device as part of an automated test
    framework, and we use qemu/Renode emulation so that tests can be run even
    without physical devices present.

-   **Easy to integrate**: We want to be as open a system as possible, and use
    the best code available for each platform. To do that, we're going to rely
    on projects like
    [CMSIS-NN](https://www.keil.com/pack/doc/CMSIS/NN/html/index.html),
    [uTensor](https://github.com/uTensor/uTensor), and other vendor libraries to
    handle as much performance-critical code as possible. We know that there are
    an increasing number of options to accelerate neural networks on
    microcontrollers, so we're aiming to be a good host for deploying those
    hardware technologies too.

-   **Compatible**: We're using the same file schema, interpreter API, and
    kernel interface as regular TensorFlow Lite, so we leverage the large
    existing set of tools, documentation, and examples for the project. The
    biggest barrier to deploying ML models is getting them from a training
    environment into a form that's easy to run inference on, so we see reusing
    this rich ecosystem as being crucial to being easily usable. We also hope to
    integrate this experimental work back into the main codebase in the future.

To meet those goals, we've made some tradeoffs:

-   **Simple C++**: To help with readability, our code is written in a modern
    version of C++, but we generally treat it as a "better C", rather relying on
    more complex features such as template meta-programming. As mentioned
    earlier, we avoid any use of dynamic memory allocation (new/delete) or the
    standard C/C++ libraries, so we believe this should still be fairly
    portable. It does mean that some older devices with C-only toolchains won't
    be supported, but we're hoping that the reference operator implementations
    (which are simple C-like functions) can still be useful in those cases. The
    interfaces are also designed to be C-only, so it should be possible to
    integrate the resulting library with pure C projects.

-   **Interpreted**: Code generation is a popular pattern for embedded code,
    because it gives standalone code that's easy to modify and step through, but
    we've chosen to go with an interpreted approach. In our internal
    microcontroller work we've found that using an extremely stripped-down
    interpreter with almost no dependencies gives us a lot of the same
    advantages, but is easier to maintain. For example, when new updates come
    out for the underlying library, you can just merge your local modifications
    in a single step, rather than having to regenerate new code and then patch
    in any changes you subsequently made. The coarse granularity of the
    interpreted primitives means that each operation call typically takes
    hundreds of thousands of instruction cycles at least, so we don't see
    noticeable performance gains from avoiding what's essentially a single
    switch statement at the interpreter level to call each operation. We're
    still working on improving the packaging though, for example we're
    considering having the ability to snapshot all the source files and headers
    used for a particular model, being able to compile the code and data
    together as a library, and then access it through a minimal set of C
    interface calls which hide the underlying complexity.

-   **Flatbuffers**: We represent our models using
    [the standard flatbuffer schema used by the rest of TensorFlow Lite](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema.fbs),
    with the difference that we always keep it in read-only program memory
    (typically flash) rather than relying on having a file system to read it
    from. This is a good fit because flatbuffer's serialized format is designed
    to be mapped into memory without requiring any extra memory allocations or
    modifications to access it. All of the functions to read model values work
    directly on the serialized bytes, and large sections of data like weights
    are directly accessible as sequential C-style arrays of their data type,
    with no strides or unpacking needed. We do get a lot of value from using
    flatbuffers, but there is a cost in complexity. The flat buffer library code
    is all inline
    [inside the main headers](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema_generated.h),
    but it isn't straightforward to inspect their implementations, and the model
    data structures aren't easy to comprehend from the debugger. The header for
    the schema itself also has to be periodically updated when new information
    is added to the file format, though we try to handle that transparently for
    most developers by checking in a pre-generated version.

-   **Code Duplication**: Some of the code in this prototype largely duplicates
    the logic in other parts of the TensorFlow Lite code base, for example the
    operator wrappers. We've tried to keep share as much as we can between the
    two interpreters, but there are some assumptions built into the original
    runtime that make this difficult. We'll be working on modularizing the main
    interpreter so that we can move to an entirely shared system.

This initial preview release is designed to get early feedback, and is not
intended to be a final product. It only includes enough operations to run a
simple keyword recognition model, and the implementations are not optimized.
We're hoping this will be a good way to get feedback and collaborate to improve
the framework.

## Generating Project Files

It's not always easy or convenient to use a makefile-based build process,
especially if you're working on a product that uses a different IDE for the rest
of its code. To address that, it's possible to generate standalone project
folders for various popular build systems. These projects are self-contained,
with only the headers and source files needed by a particular binary, and
include project files to make loading them into an IDE easy. These can be
auto-generated for any target you can compile using the main Make system, using
a command like this:

'''
make -f tensorflow/lite/experimental/micro/tools/make/Makefile TARGET=mbed TAGS="disco_f746ng" generate_micro_speech_mbed_project
'''

This will create a folder in
`tensorflow/lite/experimental/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech_main_test/mbed`
that contains the source and header files, some Mbed configuration files, and a
README. You should then be able to copy this directory to another machine, and
use it just like any other Mbed project. There's more information about project
files [below](#working-with-generated-projects).

## Generating Arduino Libraries

It's possible to use the Arduino Desktop IDE to build TFL Micro targets for
Arduino devices. The source code is packaged as a .zip archive that you can add
in the IDE by going to Sketch->Include Library->Add .ZIP Library... Once you've
added the library, you can then go to File->Examples->TensorFlowLite to find a
simple sketches that you can use to build the examples.

You can generate the zip file from the source code here in git by running the
following command:

'''
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/tools/ci_build/test_arduino.sh
'''

The resulting library can be found in `tensorflow/lite/experimental/micro/tools/make/gen/arduino_x86_64/prj/tensorflow_lite.zip`.
This generates a library that includes all of the examples as sketches, along
with the framework code you need to run your own examples.

## How to Port TensorFlow Lite Micro to a New Platform

Are you a hardware or operating system provider looking to run machine learning
on your platform? We're keen to help, and we've had experience helping other
teams do the same thing, so here are our recommendations.

### Requirements

Since the core neural network operations are pure arithmetic, and don't require
any I/O or other system-specific functionality, the code doesn't have to have
many dependencies. We've tried to enforce this, so that it's as easy as possible
to get TensorFlow Lite Micro running even on 'bare metal' systems without an OS.
Here are the core requirements that a platform needs to run the framework:

-   C/C++ compiler capable of C++11 compatibility. This is probably the most
    restrictive of the requirements, since C++11 is not as widely adopted in the
    embedded world as it is elsewhere. We made the decision to require it since
    one of the main goals of TFL Micro is to share as much code as possible with
    the wider TensorFlow codebase, and since that relies on C++11 features, we
    need compatibility to achieve it. We only use a small, sane, subset of C++
    though, so don't worry about having to deal with template metaprogramming or
    similar challenges!

-   Debug logging. The core network operations don't need any I/O functions, but
    to be able to run tests and tell if they've worked as expected, the
    framework needs some way to write out a string to some kind of debug
    console. This will vary from system to system, for example on Linux it could
    just be `fprintf(stderr, debug_string)` whereas an embedded device might
    write the string out to a specified UART. As long as there's some mechanism
    for outputting debug strings, you should be able to use TFL Micro on that
    platform.

-   Math library. The C standard `libm.a` library is needed to handle some of
    the mathematical operations used to calculate neural network results.

-   Global variable initialization. We do use a pattern of relying on global
    variables being set before `main()` is run in some places, so you'll need to
    make sure your compiler toolchain

And that's it! You may be wondering about some other common requirements that
are needed by a lot of non-embedded software, so here's a brief list of things
that aren't necessary to get started with TFL Micro on a new platform:

-   Operating system. Since the only platform-specific function we need is
    `DebugLog()`, there's no requirement for any kind of Posix or similar
    functionality around files, processes, or threads.

-   C or C++ standard libraries. The framework tries to avoid relying on any
    standard library functions that require linker-time support. This includes
    things like string functions, but still allows us to use headers like
    `stdtypes.h` which typically just define constants and typedefs.
    Unfortunately this distinction isn't officially defined by any standard, so
    it's possible that different toolchains may decide to require linked code
    even for the subset we use, but in practice we've found it's usually a
    pretty obvious decision and stable over platforms and toolchains.

-   Dynamic memory allocation. All the TFL Micro code avoids dynamic memory
    allocation, instead relying on local variables on the stack in most cases,
    or global variables for a few situations. These are all fixed-size, which
    can mean some compile-time configuration to ensure there's enough space for
    particular networks, but does avoid any need for a heap and the
    implementation of `malloc\new` on a platform.

-   Floating point. Eight-bit integer arithmetic is enough for inference on many
    networks, so if a model sticks to these kind of quantized operations, no
    floating point instructions should be required or executed by the framework.

### Getting Started

We recommend that you start trying to compile and run one of the simplest tests
in the framework as your first step. The full TensorFlow codebase can seem
overwhelming to work with at first, so instead you can begin with a collection
of self-contained project folders that only include the source files needed for
a particular test or executable. You can find a set of pre-generated projects
[here](https://drive.google.com/open?id=1cawEQAkqquK_SO4crReDYqf_v7yAwOY8).

As mentioned above, the one function you will need to implement for a completely
new platform is debug logging. If your device is just a variation on an existing
platform you may be able to reuse code that's already been written. To
understand what's available, begin with the default reference implementation at
[tensorflow/lite/experimental/micro/debug_log.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/debug_log.cc),
which uses fprintf and stderr. If your platform has this level of support for
the C standard library in its toolchain, then you can just reuse this.
Otherwise, you'll need to do some research into how your platform and device can
communicate logging statements to the outside world. As another example, take a
look at
[the Mbed version of `DebugLog()`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/mbed/debug_log.cc),
which creates a UART object and uses it to output strings to the host's console
if it's connected.

Begin by navigating to the micro_error_reporter_test folder in the pregenerated
projects you downloaded. Inside here, you'll see a set of folders containing all
the source code you need. If you look through them, you should find a total of
around 60 C or C++ files that compiled together will create the test executable.
There's an example makefile in the directory that lists all of the source files
and include paths for the headers. If you're building on a Linux or MacOS host
system, you may just be able to reuse that same makefile to cross-compile for
your system, as long as you swap out the `CC` and `CXX` variables from their
defaults, to point to your cross compiler instead (for example
`arm-none-eabi-gcc` or `riscv64-unknown-elf-gcc`). Otherwise, set up a project
in the build system you are using. It should hopefully be fairly
straightforward, since all of the source files in the folder need to be
compiled, so on many IDEs you can just drag the whole lot in. Then you need to
make sure that C++11 compatibility is turned on, and that the right include
paths (as mentioned in the makefile) have been added.

You'll see the default `DebugLog()` implementation in
'tensorflow/lite/experimental/micro/debug_log.cc' inside the
micro_error_reporter_test folder. Modify that file to add the right
implementation for your platform, and then you should be able to build the set
of files into an executable. Transfer that executable to your target device (for
example by flashing it), and then try running it. You should see output that
looks something like this:

'''
Number: 42
Badly-formed format string
Another  badly-formed  format string
~~ALL TESTS PASSED~~~
'''

If not, you'll need to debug what went wrong, but hopefully with this small
starting project it should be manageable.

### Troubleshooting

When we've been porting to new platforms, it's often been hard to figure out
some of the fundamentals like linker settings and other toolchain setup flags.
If you are having trouble, see if you can find a simple example program for your
platform, like one that just blinks an LED. If you're able to build and run that
successfully, then start to swap in parts of the TF Lite Micro codebase to that
working project, taking it a step at a time and ensuring it's still working
after every change. For example, a first step might be to paste in your
`DebugLog()` implementation and call `DebugLog("Hello World!")` from the main
function.

Another common problem on embedded platforms is the stack size being too small.
Mbed defaults to 4KB for the main thread's stack, which is too small for most
models since TensorFlow Lite allocates buffers and other data structures that
require more memory. The exact size will depend on which model you're running,
but try increasing it if you are running into strange corruption issues that
might be related to stack overwriting.

### Optimizing for your Platform

The default reference implementations in TensorFlow Lite Micro are written to be
portable and easy to understand, not fast, so you'll want to replace performance
critical parts of the code with versions specifically tailored to your
architecture. The framework has been designed with this in mind, and we hope the
combination of small modules and many tests makes it as straightforward as
possible to swap in your own code a piece at a time, ensuring you have a working
version at every step. To write specialized implementations for a platform, it's
useful to understand how optional components are handled inside the build
system.

### Code Module Organization

We have adopted a system of small modules with platform-specific implementations
to help with portability. Every module is just a standard `.h` header file
containing the interface (either functions or a class), with an accompanying
reference implementation in a `.cc` with the same name. The source file
implements all of the code that's declared in the header. If you have a
specialized implementation, you can create a folder in the same directory as the
header and reference source, name it after your platform, and put your
implementation in a `.cc` file inside that folder. We've already seen one
example of this, where the Mbed and Bluepill versions of `DebugLog()` are inside
[mbed](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/mbed)
and
[bluepill](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/bluepill)
folders, children of the
[same directory](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro)
where the stdio-based
[`debug_log.cc`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/debug_log.cc)
reference implementation is found.

The advantage of this approach is that we can automatically pick specialized
implementations based on the current build target, without having to manually
edit build files for every new platform. It allows incremental optimizations
from a always-working foundation, without cluttering the reference
implementations with a lot of variants.

To see why we're doing this, it's worth looking at the alternatives. TensorFlow
Lite has traditionally used preprocessor macros to separate out some
platform-specific code within particular files, for example:

'''
#ifndef USE_NEON
#if defined(__ARM_NEON__) || defined(__ARM_NEON)
#define USE_NEON
#include <arm_neon.h>
#endif
'''

There’s also a tradition in gemmlowp of using file suffixes to indicate
platform-specific versions of particular headers, with kernel_neon.h being
included by kernel.h if `USE_NEON` is defined. As a third variation, kernels are
separated out using a directory structure, with
tensorflow/lite/kernels/internal/reference containing portable implementations,
and tensorflow/lite/kernels/internal/optimized holding versions optimized for
NEON on Arm platforms.

These approaches are hard to extend to multiple platforms. Using macros means
that platform-specific code is scattered throughout files in a hard-to-find way,
and can make following the control flow difficult since you need to understand
the macro state to trace it. For example, I temporarily introduced a bug that
disabled NEON optimizations for some kernels when I removed
tensorflow/lite/kernels/internal/common.h from their includes, without realizing
it was where USE_NEON was defined!

It’s also tough to port to different build systems, since figuring out the right
combination of macros to use can be hard, especially since some of them are
automatically defined by the compiler, and others are only set by build scripts,
often across multiple rules.

The approach we are using extends the file system approach that we use for
kernel implementations, but with some specific conventions:

-   For each module in TensorFlow Lite, there will be a parent directory that
    contains tests, interface headers used by other modules, and portable
    implementations of each part.
-   Portable means that the code doesn’t include code from any libraries except
    flatbuffers, or other TF Lite modules. You can include a limited subset of
    standard C or C++ headers, but you can’t use any functions that require
    linking against those libraries, including fprintf, etc. You can link
    against functions in the standard math library, in <math.h>.
-   Specialized implementations are held inside subfolders of the parent
    directory, named after the platform or library that they depend on. So, for
    example if you had my_module/foo.cc, a version that used RISC-V extensions
    would live in my_module/riscv/foo.cc. If you had a version that used the
    CMSIS library, it should be in my_module/cmsis/foo.cc.
-   These specialized implementations should completely replace the top-level
    implementations. If this involves too much code duplication, the top-level
    implementation should be split into smaller files, so only the
    platform-specific code needs to be replaced.
-   There is a convention about how build systems pick the right implementation
    file. There will be an ordered list of 'tags' defining the preferred
    implementations, and to generate the right list of source files, each module
    will be examined in turn. If a subfolder with a tag’s name contains a .cc
    file with the same base name as one in the parent folder, then it will
    replace the parent folder’s version in the list of build files. If there are
    multiple subfolders with matching tags and file names, then the tag that’s
    latest in the ordered list will be chosen. This allows us to express “I’d
    like generically-optimized fixed point if it’s available, but I’d prefer
    something using the CMSIS library” using the list 'fixed_point cmsis'. These
    tags are passed in as `TAGS="<foo>"` on the command line when you use the
    main Makefile to build.
-   There is an implicit “reference” tag at the start of every list, so that
    it’s possible to support directory structures like the current
    tensorflow/kernels/internal where portable implementations are held in a
    “reference” folder that’s a sibling to the NEON-optimized folder.
-   The headers for each unit in a module should remain platform-agnostic, and
    be the same for all implementations. Private headers inside a sub-folder can
    be used as needed, but shouldn’t be referred to by any portable code at the
    top level.
-   Tests should be at the parent level, with no platform-specific code.
-   No platform-specific macros or #ifdef’s should be used in any portable code.

The implementation of these rules is handled inside the Makefile, with a
[`specialize` function](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/tools/make/helper_functions.inc#L42)
that takes a list of reference source file paths as an input, and returns the
equivalent list with specialized versions of those files swapped in if they
exist.

### Working with Generated Projects

So far, I've recommended that you use the standalone generated projects for your
system. You might be wondering why you're not just checking out the full
[TensorFlow codebase from GitHub](https://github.com/tensorflow/tensorflow/)?
The main reason is that there is a lot more diversity of architectures, IDEs,
support libraries, and operating systems in the embedded world. Many of the
toolchains require their own copy of source files, or a list of sources to be
written to a project file. When a developer working on TensorFlow adds a new
source file or changes its location, we can't expect her to update multiple
different project files, many of which she may not have the right software to
verify the change was correct. That means we have to rely on a central listing
of source files (which in our case is held in the makefile), and then call a
tool to generate other project files from those. We could ask embedded
developers to do this process themselves after downloading the main source, but
running the makefile requires a Linux system which may not be available, takes
time, and involves downloading a lot of dependencies. That is why we've opted to
make regular snapshots of the results of generating these projects for popular
IDEs and platforms, so that embedded developers have a fast and friendly way to
start using TensorFlow Lite for Microcontrollers.

This does have the disadvantage that you're no longer working directly on the
main repository, instead you have a copy that's outside of source control. We've
tried to make the copy as similar to the main repo as possible, for example by
keeping the paths of all source files the same, and ensuring that there are no
changes between the copied files and the originals, but it still makes it
tougher to sync as the main repository is updated. There are also multiple
copies of the source tree, one for each target, so any change you make to one
copy has to be manually propagated across all the other projects you care about.
This doesn't matter so much if you're just using the projects as they are to
build products, but if you want to support a new platform and have the changes
reflected in the main code base, you'll have to do some extra work.

As an example, think about the `DebugLog()` implementation we discussed adding
for a new platform earlier. At this point, you have a new version of
`debug_log.cc` that does what's required, but how can you share that with the
wider community? The first step is to pick a tag name for your platform. This
can either be the operating system (for example 'mbed'), the name of a device
('bluepill'), or some other text that describes it. This should be a short
string with no spaces or special characters. Log in or create an account on
GitHub, fork the full
[TensorFlow codebase](https://github.com/tensorflow/tensorflow/) using the
'Fork' button on the top left, and then grab your fork by using a command like
`git clone https://github.com/<your user name>/tensorflow`.

You'll either need Linux, MacOS, or Windows with something like CygWin installed
to run the next steps, since they involve building a makefile. Run the following
commands from a terminal, inside the root of the source folder:

'''
tensorflow/lite/experimental/micro/tools/make/download_dependencies.sh
make -f tensorflow/lite/experimental/micro/tools/make/Makefile generate_projects
'''

This will take a few minutes, since it has to download some large toolchains for
the dependencies. Once it has finished, you should see some folders created
inside a path like
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/`. The exact
path depends on your host operating system, but you should be able to figure it
out from all the copy commands. These folders contain the generated project and
source files, with
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/keil`
containing the Keil uVision targets,
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/mbed` with
the Mbed versions, and so on.

If you've got this far, you've successfully set up the project generation flow.
Now you need to add your specialized implementation of `DebugLog()`. Start by
creating a folder inside `tensorflow/lite/experimental/micro/` named after the
tag you picked earlier. Put your `debug_log.cc` file inside this folder, and
then run this command, with '<your tag>' replaced by the actual folder name:

'''
make -f tensorflow/lite/experimental/micro/tools/make/Makefile TAGS="<your tag>" generate_projects
'''

If your tag name actually refers to a whole target architecture, then you'll use
TARGET or TARGET_ARCH instead. For example, here's how a simple RISC-V set of
projects is generated:

'''
make -f tensorflow/lite/experimental/micro/tools/make/Makefile TARGET="riscv32_mcu" generate_projects
'''

The way it works is the same as TAGS though, it just looks for specialized
implementations with the same containing folder name.

If you look inside the projects that have been created, you should see that the
default `DebugLog()` implementation is no longer present at
`tensorflow/lite/experimental/micro/debug_log.cc`, and instead
`tensorflow/lite/experimental/micro/<your tag>/debug_log.cc` is being used. Copy
over the generated project files and try building them in your own IDE. If
everything works, then you're ready to submit your change.

To do this, run something like:

'''
git add tensorflow/lite/experimental/micro/<your tag>/debug_log.cc
git commit -a -m "Added DebugLog() support for <your platform>"
git push origin master
'''

Then go back to `https://github.com/<your account>/tensorflow`, and choose "New
Pull Request" near the top. You should then be able to go through the standard
TensorFlow PR process to get your change added to the main repository, and
available to the rest of the community!

### Supporting a Platform with Makefiles

The changes you've made so far will enable other developers using the generated
projects to use your platform, but TensorFlow's continuous integration process
uses makefiles to build frequently and ensure changes haven't broken the build
process for different systems. If you are able to convert your build procedure
into something that can be expressed by a makefile, then we can integrate your
platform into our CI builds and make sure it continues to work.

Fully describing how to do this is beyond the scope of this documentation, but
the biggest needs are:

-   A command-line compiler that can be called for every source file.
-   A list of the arguments to pass into the compiler to build and link all
    files.
-   The correct linker map files and startup assembler to ensure `main()` gets
    called.

### Supporting a Platform with Emulation Testing

Integrating your platform into the makefile process should help us make sure
that it continues to build, but it doesn't guarantee that the results of the
build process will run correctly. Running tests is something we require to be
able to say that TensorFlow officially supports a platform, since otherwise we
can't guarantee that users will have a good experience when they try using it.
Since physically maintaining a full set of all supported hardware devices isn't
feasible, we rely on software emulation to run these tests. A good example is
our
[STM32F4 'Bluepill' support](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/testing/test_bluepill_binary.sh),
which uses [Docker](https://www.docker.com/) and [Renode](https://renode.io/) to
run built binaries in an emulator. You can use whatever technologies you want,
the only requirements are that they capture the debug log output of the tests
being run in the emulator, and parse them for the string that indicates the test
was successful. These scripts need to run on Ubuntu 18.04, in a bash
environment, though Docker is available if you need to install extra software or
have other dependencies.

### Implementing More Optimizations

Clearly, getting debug logging support is only the beginning of the work you'll
need to do on a particular platform. It's very likely that you'll want to
optimize the core deep learning operations that take up the most time when
running models you care about. The good news is that the process for providing
optimized implementations is the same as the one you just went through to
provide your own logging. You'll need to identify parts of the code that are
bottlenecks, and then add specialized implementations in their own folders.
These don't need to be platform specific, they can also be broken out by which
library they rely on for example. [Here's where we do that for the CMSIS
implementation of integer fast-fourier
transforms](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/simple_features/simple_features_generator.cc).
This more complex case shows that you can also add helper source files alongside
the main implementation, as long as you
[mention them in the platform-specific makefile](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/CMSIS/Makefile.inc).
You can also do things like update the list of libraries that need to be linked
in, or add include paths to required headers.
```
## _tensorflow_compiler_mlir_tensorflow_tests_tf_saved_model_README_md
```# SavedModel importer FileCheck tests.

## Debugging tests

While debugging tests, the following commands are handy.

Run FileCheck test:

'''
bazel run :foo.py.test
'''

Run just the Python file and look at the output:

'''
bazel run :foo
'''

Generate saved model to inspect proto:

'''
bazel run :foo -- --save_model_path=/tmp/my.saved_model
# Inspect /tmp/my.saved_model/saved_model.pb
'''

## Rationale for Python-based tests

For a SavedModel importer, the natural place to start is to feed in the
SavedModel format directly and test the output MLIR. We don't do that though.

The SavedModel format is a directory structure which contains a SavedModel proto
and some other stuff (mostly binary files of some sort) in it. That makes it not
suitable for use as a test input, since it is not human-readable. Even just the
text proto for the SavedModel proto is difficult to use as a test input, since a
small piece of Python code (e.g. just a tf.Add) generates thousands of lines of
text proto.

That points to a solution though: write our tests starting from the Python API's
that generate the SavedModel. That leads to very compact test inputs.

As the SavedModel work progresses, it's likely to be of interest to find a
shortcut between the Python `tf.Module` and the SavedModel MLIR representation
that doesn't involve serializing a SavedModel to disk and reading it back.

## Potential improvements

The test iteration cycle for these tests is very long (usually over a minute).
We need to find a way to improve this in the future.
```
## _tensorflow_lite_kernels_internal_reference_integer_ops_README_md
```This directory contains reference implementations for int8 fully integer kernels.

Weight filters of convs are expected to be symmetric per-channel quantized in
the range [-127, 127].
Inputs/activations are expected to be asymmetric per-layer quantized in the
range [-128, 127].

THESE ARE EXPERIMENTAL AND PRONE TO CHANGE.
```
# Inline
## _tensorflow_tools_test_upload_test_benchmarks_py
### Line 1-18
```
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Command to upload benchmark test results to a cloud datastore.

This uploader script is typically run periodically as a cron job.  It locates,
```
### Line 116-128
```
  """
  files = [f for f in os.listdir(dirpath) if is_real_file(dirpath, f)]
  return sorted(files, key=lambda f: get_mtime(dirpath, f))


# Note: The file locking code uses flock() instead of lockf() because benchmark
# files are only opened for reading (not writing) and we still want exclusive
# locks on them.  This imposes the limitation that the data directory must be
# local, not NFS-mounted.
def lock(fd):
  fcntl.flock(fd, fcntl.LOCK_EX)


```
### Line 154-164
```
  test_name = text_type(test_result["name"])
  start_time = datetime.datetime.utcfromtimestamp(
      float(test_result["startTime"]))
  batch = []

  # Create the Test Entity containing all the test information as a
  # non-indexed JSON blob.
  t_key = client.key("Test")
  t_val = datastore.Entity(t_key, exclude_from_indexes=["info"])
  t_val.update({
      "test": test_name,
```
### Line 165-176
```
      "start": start_time,
      "info": text_type(data)
  })
  batch.append(t_val)

  # Create one Entry Entity for each benchmark entry.  The wall-clock timing is
  # the attribute to be fetched and displayed.  The full entry information is
  # also stored as a non-indexed JSON blob.
  for ent in test_result["entries"].get("entry", []):
    ent_name = text_type(ent["name"])
    e_key = client.key("Entry")
    e_val = datastore.Entity(e_key, exclude_from_indexes=["info"])
```
### Line 181-190
```
        "timing": ent["wallTime"],
        "info": text_type(json.dumps(ent))
    })
    batch.append(e_val)

  # Put the whole batch of Entities in the datastore.
  client.put_multi(batch)


def upload_benchmark_files(opts):
```
### Line 211-220
```
    try:
      with open(fpath, "r") as fd:
        if trylock(fd):
          upload_benchmark_data(client, fd.read())
          shutil.move(fpath, os.path.join(opts.archivedir, fname))
          # unlock(fd) -- When "with open()" closes fd, the lock is released.
    except Exception as e:  # pylint: disable=broad-except
      print("Cannot process '%s', skipping. Error: %s" % (fpath, e))


```
### Line 240-249
```


def main():
  options = parse_cmd_line()

  # Check that credentials are specified to access the datastore.
  if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS env. var. is not set.")

  upload_benchmark_files(options)
```

## _tensorflow_python_data_benchmarks_from_tensor_slices_benchmark_py
### Line 1-18
```
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Benchmarks for `tf.data.Dataset.from_tensor_slices()`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```
### Line 21-30
```

from tensorflow.python.data.benchmarks import benchmark_base
from tensorflow.python.data.ops import dataset_ops


# TODO(b/119837791): Add eager benchmarks.
class FromTensorSlicesBenchmark(benchmark_base.DatasetBenchmarkBase):
  """Benchmarks for `tf.data.Dataset.from_tensor_slices()`."""

  def benchmark_slice_repeat_batch(self):
```

## _third_party_mlir_tools_mlir_tblgen_OpDocGen_cpp
### Line 1-51
```
//===- OpDocGen.cpp - MLIR operation documentation generator --------------===//
//
// Copyright 2019 The MLIR Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// =============================================================================
//
// OpDocGen uses the description of operations to generate documentation for the
// operations.
//
//===----------------------------------------------------------------------===//

#include "DocGenUtilities.h"
#include "mlir/TableGen/GenInfo.h"
#include "mlir/TableGen/Operator.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/StringExtras.h"
#include "llvm/Support/FormatVariadic.h"
#include "llvm/Support/Signals.h"
#include "llvm/TableGen/Error.h"
#include "llvm/TableGen/Record.h"
#include "llvm/TableGen/TableGenBackend.h"

using namespace llvm;
using namespace mlir;
using namespace mlir::tblgen;

using mlir::tblgen::Operator;

// Emit the description by aligning the text to the left per line (e.g.,
// removing the minimum indentation across the block).
//
// This expects that the description in the tablegen file is already formatted
// in a way the user wanted but has some additional indenting due to being
// nested in the op definition.
void mlir::tblgen::emitDescription(StringRef description, raw_ostream &os) {
  // Determine the minimum number of spaces in a line.
  size_t min_indent = -1;
  StringRef remaining = description;
  while (!remaining.empty()) {
    auto split = remaining.split('\n');
```
### Line 53-74
```
    if (indent != StringRef::npos)
      min_indent = std::min(indent, min_indent);
    remaining = split.second;
  }

  // Print out the description indented.
  os << "\n";
  remaining = description;
  bool printed = false;
  while (!remaining.empty()) {
    auto split = remaining.split('\n');
    if (split.second.empty()) {
      // Skip last line with just spaces.
      if (split.first.ltrim().empty())
        break;
    }
    // Print empty new line without spaces if line only has spaces, unless no
    // text has been emitted before.
    if (split.first.ltrim().empty()) {
      if (printed)
        os << "\n";
    } else {
```
### Line 77-86
```
    }
    remaining = split.second;
  }
}

// Emits `str` with trailing newline if not empty.
static void emitIfNotEmpty(StringRef str, raw_ostream &os) {
  if (!str.empty()) {
    emitDescription(str, os);
    os << "\n";
```
### Line 93-102
```
                                raw_ostream &os) {
  os << "# Dialect '" << dialect.getName() << "' definition\n";
  emitIfNotEmpty(dialect.getSummary(), os);
  emitIfNotEmpty(dialect.getDescription(), os);

  // TODO(antiagainst): Add link between use and def for types
  if (!types.empty())
    os << "## Type definition\n";
  for (auto type : types) {
    os << "### " << type.getDescription() << "\n";
```
### Line 108-125
```
    os << "## Operation definition\n";
  for (auto op : ops) {
    os << "### " << op.getOperationName() << " (" << op.getQualCppClassName()
       << ")";

    // Emit summary & description of operator.
    if (op.hasSummary())
      os << "\n" << op.getSummary() << "\n";
    os << "\n#### Description:\n";
    if (op.hasDescription())
      mlir::tblgen::emitDescription(op.getDescription(), os);

    // Emit operands & type of operand. All operands are numbered, some may be
    // named too.
    os << "\n#### Operands:\n";
    for (const auto &operand : op.getOperands()) {
      os << "1. ";
      if (!operand.name.empty())
```
### Line 127-138
```
      else
        os << "&laquo;unnamed&raquo;: ";
      os << operand.constraint.getDescription() << "\n";
    }

    // Emit attributes.
    // TODO: Attributes are only documented by TableGen name, with no further
    // info. This should be improved.
    os << "\n#### Attributes:\n";
    if (op.getNumAttributes() > 0) {
      os << "| Attribute | MLIR Type | Description |\n"
         << "| :-------: | :-------: | ----------- |\n";
```
### Line 141-150
```
      os << "| `" << namedAttr.name << "` | `"
         << namedAttr.attr.getStorageType() << "` | "
         << namedAttr.attr.getDescription() << " attribute |\n";
    }

    // Emit results.
    os << "\n#### Results:\n";
    for (unsigned i = 0, e = op.getNumResults(); i < e; ++i) {
      os << "1. ";
      auto name = op.getResultName(i);
```

## _tensorflow_lite_experimental_microfrontend_lib_noise_reduction_io_c
### Line 10-19
```
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
#include "tensorflow/lite/experimental/microfrontend/lib/noise_reduction_io.h"

void NoiseReductionWriteMemmapPreamble(
    FILE* fp, const struct NoiseReductionState* state) {
  fprintf(fp, "static uint32_t noise_reduction_estimate[%zu];\n",
```

## _third_party_mlir_lib_Dialect_QuantOps_IR_QuantTypes_cpp
### Line 1-29
```
//===- QuantOps.cpp - Quantization Type and Ops Implementation --*- C++ -*-===//
//
// Copyright 2019 The MLIR Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// =============================================================================

#include "mlir/Dialect/QuantOps/QuantTypes.h"
#include "TypeDetail.h"

#include "mlir/IR/MLIRContext.h"
#include "mlir/IR/StandardTypes.h"
#include "llvm/ADT/StringRef.h"
#include "llvm/ADT/Twine.h"
#include "llvm/Support/MathExtras.h"

using namespace mlir;
using namespace mlir::quant;
using namespace mlir::quant::detail;
```
### Line 34-45
```

LogicalResult QuantizedType::verifyConstructionInvariants(
    llvm::Optional<Location> loc, MLIRContext *context, unsigned flags,
    Type storageType, Type expressedType, int64_t storageTypeMin,
    int64_t storageTypeMax) {
  // Verify that the storage type is integral.
  // This restriction may be lifted at some point in favor of using bf16
  // or f16 as exact representations on hardware where that is advantageous.
  auto intStorageType = storageType.dyn_cast<IntegerType>();
  if (!intStorageType) {
    if (loc) {
      emitError(*loc, "storage type must be integral");
```
### Line 46-63
```
    }
    return failure();
  }
  unsigned integralWidth = intStorageType.getWidth();

  // Verify storage width.
  if (integralWidth == 0 || integralWidth > MaxStorageBits) {
    if (loc) {
      emitError(*loc, "illegal storage type size: ") << integralWidth;
    }
    return failure();
  }

  // Verify storageTypeMin and storageTypeMax.
  bool isSigned =
      (flags & QuantizationFlags::Signed) == QuantizationFlags::Signed;
  int64_t defaultIntegerMin =
      getDefaultMinimumForInteger(isSigned, integralWidth);
```
### Line 86-96
```
int64_t QuantizedType::getStorageTypeMax() const {
  return static_cast<ImplType *>(impl)->storageTypeMax;
}

unsigned QuantizedType::getStorageTypeIntegralWidth() const {
  // NOTE: If ever supporting non-integral storage types, some other scheme
  // for determining the width will be needed.
  return static_cast<ImplType *>(impl)->storageType.getIntOrFloatBitWidth();
}

Type QuantizedType::getExpressedType() const {
```
### Line 115-134
```
  return primitiveOrContainerType.dyn_cast<QuantizedType>();
}

Type QuantizedType::castFromStorageType(Type candidateType) {
  if (candidateType == getStorageType()) {
    // i.e. i32 -> quant<"uniform[i8:f32]{1.0}">
    return *this;
  } else if (candidateType.isa<RankedTensorType>()) {
    // i.e. tensor<4xi8> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
    return RankedTensorType::get(
        candidateType.cast<RankedTensorType>().getShape(), getStorageType());
  } else if (candidateType.isa<UnrankedTensorType>()) {
    // i.e. tensor<i8> -> tensor<!quant<"uniform[i8:f32]{1.0}">>
    return UnrankedTensorType::get(getStorageType());
  } else if (candidateType.isa<VectorType>()) {
    // i.e. tensor<4xi8> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
    return VectorType::get(candidateType.cast<VectorType>().getShape(),
                           getStorageType());
  }

```
### Line 135-147
```
  return nullptr;
}

Type QuantizedType::castToStorageType(Type quantizedType) {
  if (quantizedType.isa<QuantizedType>()) {
    // i.e. quant<"uniform[i8:f32]{1.0}"> -> i8
    return quantizedType.cast<QuantizedType>().getStorageType();
  } else if (quantizedType.isa<ShapedType>()) {
    // i.e. tensor<4xi8> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
    ShapedType sType = quantizedType.cast<ShapedType>();
    if (!sType.getElementType().isa<QuantizedType>()) {
      return nullptr;
    }
```
### Line 159-183
```
  return nullptr;
}

Type QuantizedType::castFromExpressedType(Type candidateType) {
  if (candidateType == getExpressedType()) {
    // i.e. f32 -> quant<"uniform[i8:f32]{1.0}">
    return *this;
  } else if (candidateType.isa<ShapedType>()) {
    ShapedType candidateShapedType = candidateType.cast<ShapedType>();
    if (candidateShapedType.getElementType() != getExpressedType()) {
      return nullptr;
    }

    if (candidateType.isa<RankedTensorType>()) {
      // i.e. tensor<4xf32> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
      return RankedTensorType::get(candidateShapedType.getShape(), *this);
    } else if (candidateType.isa<UnrankedTensorType>()) {
      // i.e. tensor<xf32> -> tensor<x!quant<"uniform[i8:f32]{1.0}">>
      return UnrankedTensorType::get(*this);
    } else if (candidateType.isa<VectorType>()) {
      // i.e. tensor<4xf32> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
      return VectorType::get(candidateShapedType.getShape(), *this);
    }
  }

```
### Line 184-196
```
  return nullptr;
}

Type QuantizedType::castToExpressedType(Type quantizedType) {
  if (quantizedType.isa<QuantizedType>()) {
    // i.e. quant<"uniform[i8:f32]{1.0}"> -> f32
    return quantizedType.cast<QuantizedType>().getExpressedType();
  } else if (quantizedType.isa<ShapedType>()) {
    // i.e. tensor<4xi8> -> tensor<4x!quant<"uniform[i8:f32]{1.0}">>
    ShapedType sType = quantizedType.cast<ShapedType>();
    if (!sType.getElementType().isa<QuantizedType>()) {
      return nullptr;
    }
```
### Line 242-253
```
          loc, context, flags, storageType, expressedType, storageTypeMin,
          storageTypeMax))) {
    return failure();
  }

  // Verify that the expressed type is floating point.
  // If this restriction is ever eliminated, the parser/printer must be
  // extended.
  if (expressedType && !expressedType.isa<FloatType>()) {
    if (loc) {
      emitError(*loc, "expressed type must be floating point");
    }
```
### Line 287-315
```
          loc, context, flags, storageType, expressedType, storageTypeMin,
          storageTypeMax))) {
    return failure();
  }

  // Uniform quantization requires fully expressed parameters, including
  // expressed type.
  if (!expressedType) {
    if (loc) {
      emitError(*loc, "uniform quantization requires expressed type");
    }
    return failure();
  }

  // Verify that the expressed type is floating point.
  // If this restriction is ever eliminated, the parser/printer must be
  // extended.
  if (!expressedType.isa<FloatType>()) {
    if (loc) {
      emitError(*loc, "expressed type must be floating point");
    }
    return failure();
  }

  // Verify scale.
  if (scale <= 0.0 || std::isinf(scale) || std::isnan(scale)) {
    if (loc) {
      emitError(*loc) << "illegal scale: " << scale;
    }
```
### Line 356-393
```
          loc, context, flags, storageType, expressedType, storageTypeMin,
          storageTypeMax))) {
    return failure();
  }

  // Uniform quantization requires fully expressed parameters, including
  // expressed type.
  if (!expressedType) {
    if (loc) {
      emitError(*loc, "uniform quantization requires expressed type");
    }
    return failure();
  }

  // Verify that the expressed type is floating point.
  // If this restriction is ever eliminated, the parser/printer must be
  // extended.
  if (!expressedType.isa<FloatType>()) {
    if (loc) {
      emitError(*loc, "expressed type must be floating point");
    }
    return failure();
  }

  // Ensure that the number of scales and zeroPoints match.
  if (scales.size() != zeroPoints.size()) {
    if (loc) {
      emitError(*loc, "illegal number of scales and zeroPoints: ")
          << scales.size() << ", " << zeroPoints.size();
    }
    return failure();
  }

  // Verify scale.
  for (double scale : scales) {
    if (scale <= 0.0 || std::isinf(scale) || std::isnan(scale)) {
      if (loc) {
        emitError(*loc) << "illegal scale: " << scale;
```

## _tensorflow_python_ops_check_ops_py
### Line 1-19
```
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# pylint: disable=g-short-docstring-punctuation
"""Asserts and Boolean Checks."""

from __future__ import absolute_import
from __future__ import division
```
### Line 231-250
```

  Returns:
    List of tensors and scalars that, when stringified and concatenated,
    will produce the error message string.
  """
  # Prepare a message with first elements of x and y.
  data = []

  data.append('Condition x %s y did not hold.' % sym)

  if summarize > 0:
    if x.shape == y.shape and x.shape.as_list():
      # If the shapes of x and y are the same (and not scalars),
      # Get the values that actually differed and their indices.
      # If shapes are different this information is more confusing
      # than useful.
      mask = math_ops.logical_not(test_op)
      indices = array_ops.where(mask)
      indices_np = indices.numpy()
      x_vals = array_ops.boolean_mask(x, mask)
```
### Line 255-264
```
      data.append('Corresponding x values:')
      data.append(x_vals.numpy().reshape((-1,))[:num_vals])
      data.append('Corresponding y values:')
      data.append(y_vals.numpy().reshape((-1,))[:num_vals])

    # reshape((-1,)) is the fastest way to get a flat array view.
    x_np = x.numpy().reshape((-1,))
    y_np = y.numpy().reshape((-1,))
    x_sum = min(x_np.size, summarize)
    y_sum = min(y_np.size, summarize)
```
### Line 282-291
```
    An appropriate string representation of data_item
  """
  if isinstance(data_item, ops.Tensor):
    arr = data_item.numpy()
    if np.isscalar(arr):
      # Tensor.numpy() returns a scalar for zero-dimensional tensors
      return str(arr)
    else:
      flat = arr.reshape((-1,))
      lst = [str(x) for x in flat[:summarize]]
```
### Line 331-343
```
      test_op = op_func(x, y)
      condition = math_ops.reduce_all(test_op)
      if condition:
        return

      # If we get here, the assertion has failed.
      # Default to printing 3 elements like control_flow_ops.Assert (used
      # by graph mode) does. Also treat negative values as "print
      # everything" for consistency with Tensor::SummarizeValue().
      if summarize is None:
        summarize = 3
      elif summarize < 0:
        summarize = 1e9  # Code below will find exact size of x and y.
```
### Line 649-658
```

@tf_export(v1=['debugging.assert_equal', 'assert_equal'])
@_binary_assert_doc('==')
def assert_equal(x, y, data=None, summarize=None, message=None, name=None):  # pylint: disable=missing-docstring
  with ops.name_scope(name, 'assert_equal', [x, y, data]):
    # Short-circuit if x and y are the same tensor.
    if x is y:
      return None if context.executing_eagerly() else control_flow_ops.no_op()
  return _binary_assert('==', 'assert_equal', math_ops.equal, np.equal, x, y,
                        data, summarize, message, name)
```
### Line 1033-1042
```
  Raises:
    ValueError:  If static checks determine `x` fails static_condition.
  """
  assert_type(rank, dtypes.int32)

  # Attempt to statically defined rank.
  rank_static = tensor_util.constant_value(rank)
  if rank_static is not None:
    if rank_static.ndim != 0:
      raise ValueError('Rank must be a scalar.')
```
### Line 1048-1058
```
            'Static rank condition failed', x_rank_static, rank_static)
      return control_flow_ops.no_op(name='static_checks_determined_all_ok')

  condition = dynamic_condition(array_ops.rank(x), rank)

  # Add the condition that `rank` must have rank zero.  Prevents the bug where
  # someone does assert_rank(x, [n]), rather than assert_rank(x, n).
  if rank_static is None:
    this_data = ['Rank must be a scalar. Received rank: ', rank]
    rank_check = assert_rank(rank, 0, data=this_data)
    condition = control_flow_ops.with_dependencies([rank_check], condition)
```
### Line 1291-1300
```
    ValueError:  If static checks determine `x` fails static_condition.
  """
  for rank in ranks:
    assert_type(rank, dtypes.int32)

  # Attempt to statically defined rank.
  ranks_static = tuple([tensor_util.constant_value(rank) for rank in ranks])
  if not any(r is None for r in ranks_static):
    for rank_static in ranks_static:
      if rank_static.ndim != 0:
```
### Line 1307-1317
```
            'Static rank condition failed', x_rank_static, ranks_static)
      return control_flow_ops.no_op(name='static_checks_determined_all_ok')

  condition = dynamic_condition(array_ops.rank(x), ranks)

  # Add the condition that `rank` must have rank zero.  Prevents the bug where
  # someone does assert_rank(x, [n]), rather than assert_rank(x, n).
  for rank, rank_static in zip(ranks, ranks_static):
    if rank_static is None:
      this_data = ['Rank must be a scalar. Received rank: ', rank]
      rank_check = assert_rank(rank, 0, data=this_data)
```
### Line 1554-1563
```
  return control_flow_ops.cond(
      has_rank_zero, lambda: array_ops.constant([1]), lambda: dynamic_shape)


def _symbolic_dimension_sizes(symbolic_shape):
  # If len(symbolic_shape) == 0 construct a tuple
  if not symbolic_shape:
    return tuple([1])

  return symbolic_shape
```
### Line 1694-1710
```
    returned.

  Raises:
    ValueError:  If static checks determine any shape constraint is violated.
  """
  # If the user manages to assemble a dict containing tensors (possible in
  # Graph mode only), make sure we still accept that.
  if isinstance(shapes, dict):
    shapes = shapes.items()

  message = message or ''
  with ops.name_scope(name, 'assert_shapes', [shapes, data]):
    # Shape specified as None implies no constraint
    shape_constraints = [
        (ops.convert_to_tensor(x), s) for x, s in shapes if s is not None
    ]

```
### Line 1727-1736
```
            'Tensor %s.  Specified shape must be an iterable.  '
            'An iterable has the attribute `__iter__` or `__getitem__`.  '
            'Received specified shape: %s' %
            (message, tensor_name(tensor), symbolic_shape))

      # We convert this into a tuple to handle strings, lists and numpy arrays
      symbolic_shape_tuple = tuple(symbolic_shape)

      tensors_specified_innermost = False
      for i, symbol in enumerate(symbolic_shape_tuple):
```
### Line 1745-1755
```
              'unspecified dimensions is only allowed as the first entry' %
              (message, tensor_name(tensor), i))

        tensors_specified_innermost = True

      # Only include the size of the specified dimensions since the 0th symbol
      # is either ellipsis or *
      tensor_dim_sizes.append(
          _TensorDimSizes(
              tensor, tensors_specified_innermost, _dimension_sizes(tensor),
              _symbolic_dimension_sizes(
```
### Line 1760-1770
```
    for sizes in tensor_dim_sizes:
      rank = len(sizes.symbolic_sizes)
      rank_zero_or_one = rank in [0, 1]
      if sizes.unspecified_dim:
        if rank_zero_or_one:
          # No assertion of rank needed as `x` only need to have rank at least
          # 0. See elif rank_zero_or_one case comment.
          continue
        assertion = assert_rank_at_least(
            x=sizes.x,
            rank=rank,
```
### Line 1771-1782
```
            data=data,
            summarize=summarize,
            message=message,
            name=name)
      elif rank_zero_or_one:
        # Rank 0 is treated as rank 1 size 1, i.e. there is
        # no distinction between the two in terms of rank.
        # See _dimension_sizes.
        assertion = assert_rank_in(
            x=sizes.x,
            ranks=[0, 1],
            data=data,
```
### Line 1797-1806
```
    size_specifications = {}
    for sizes in tensor_dim_sizes:
      for i, size_symbol in enumerate(sizes.symbolic_sizes):

        if _is_symbol_for_any_size(size_symbol):
          # Size specified as any implies no constraint
          continue

        if sizes.unspecified_dim:
          tensor_dim = i - len(sizes.symbolic_sizes)
```
### Line 1825-1834
```
                  '%s.  %s.  Tensor %s dimension %s must have size %d.  '
                  'Received size %d, shape %s' %
                  (message, size_check_message, tensor_name(sizes.x),
                   tensor_dim, specified_size, actual_size,
                   sizes.x.get_shape()))
            # No dynamic assertion needed
            continue

          condition = math_ops.equal(
              ops.convert_to_tensor(actual_size),
```
### Line 1850-1870
```
    with ops.control_dependencies(rank_assertions):
      shapes_assertion = control_flow_ops.group(size_assertions)
    return shapes_assertion


# pylint: disable=line-too-long
def _get_diff_for_monotonic_comparison(x):
  """Gets the difference x[1:] - x[:-1]."""
  x = array_ops.reshape(x, [-1])
  if not is_numeric_tensor(x):
    raise TypeError('Expected x to be numeric, instead found: %s' % x)

  # If x has less than 2 elements, there is nothing to compare.  So return [].
  is_shorter_than_two = math_ops.less(array_ops.size(x), 2)
  short_result = lambda: ops.convert_to_tensor([], dtype=x.dtype)

  # With 2 or more elements, return x[1:] - x[:-1]
  s_len = array_ops.shape(x) - 1
  diff = lambda: array_ops.strided_slice(x, [1], [1] + s_len)- array_ops.strided_slice(x, [0], s_len)
  return control_flow_ops.cond(is_shorter_than_two, short_result, diff)

```
### Line 1923-1932
```
  Raises:
    TypeError: if `x` is not a numeric tensor.
  """
  with ops.name_scope(name, 'is_non_decreasing', [x]):
    diff = _get_diff_for_monotonic_comparison(x)
    # When len(x) = 1, diff = [], less_equal = [], and reduce_all([]) = True.
    zero = ops.convert_to_tensor(0, dtype=diff.dtype)
    return math_ops.reduce_all(math_ops.less_equal(zero, diff))


```
### Line 1958-1967
```
  Raises:
    TypeError: if `x` is not a numeric tensor.
  """
  with ops.name_scope(name, 'is_strictly_increasing', [x]):
    diff = _get_diff_for_monotonic_comparison(x)
    # When len(x) = 1, diff = [], less = [], and reduce_all([]) = True.
    zero = ops.convert_to_tensor(0, dtype=diff.dtype)
    return math_ops.reduce_all(math_ops.less(zero, diff))


```
### Line 1990-2000
```
        expected_type = item_type
      elif expected_type != item_type:
        mismatch = True
        break
  if mismatch:
    # Loop back through and build up an informative error message (this is very
    # slow, so we don't do it unless we found an error above).
    expected_type = original_expected_type
    original_item_str = None
    for item in items:
      if item is not None:
```
### Line 2118-2128
```
  y = tf.ensure_shape(y, (None, 3, 3))
  print(y.shape)
  ==> TensorShape([Dimension(None), Dimension(3), Dimension(3)])

  with tf.compat.v1.Session() as sess:
    # Raises tf.errors.InvalidArgumentError, because the shape (3,) is not
    # compatible with the shape (None, 3, 3)
    sess.run(y, feed_dict={x: [1, 2, 3]})

  ```

```

## _tensorflow_python_grappler_memory_optimizer_test_py
### Line 1-18
```
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for the swig wrapper tf_optimizer."""

from __future__ import absolute_import
from __future__ import division
```
### Line 172-181
```
            layout_optimizer=rewriter_config_pb2.RewriterConfig.OFF,
            arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
            min_graph_nodes=-1,
            memory_optimization=rewriter_config_pb2.RewriterConfig
            .RECOMPUTATION_HEURISTICS,
            # Checks that name scope "gradients/" also match sub-scope.
            memory_optimizer_target_node_name_scope='gradients/'))
    rewritten_graph_def = tf_optimizer.OptimizeGraph(config, original_metagraph)
    self.assertGreater(
        len(rewritten_graph_def.node),
```
### Line 201-210
```
            dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
            layout_optimizer=rewriter_config_pb2.RewriterConfig.OFF,
            arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
            memory_optimization=rewriter_config_pb2.RewriterConfig
            .RECOMPUTATION_HEURISTICS,
            # This should not match anything.
            memory_optimizer_target_node_name_scope='r/gradients/'))
    rewritten_graph_def = tf_optimizer.OptimizeGraph(config, original_metagraph)
    self.assertEqual(
        len(rewritten_graph_def.node), len(original_metagraph.graph_def.node))
```
### Line 271-281
```
          after_conv = nn.conv2d(current_activation, conv_filter, [1, 1, 1, 1],
                                 'SAME')
          current_activation = 2. * after_conv
          current_activation.op._set_attr(
              '_recompute_hint',
              # The value of the attribute does not matter; just that the key
              # exists in the op's attributes.
              attr_value_pb2.AttrValue(i=1))
          current_activation += 5.
          current_activation.op._set_attr(
              '_recompute_hint', attr_value_pb2.AttrValue(i=0))
```
### Line 287-297
```
      train_op = optimizer.minimize(loss)
      init_op = variables.global_variables_initializer()
    return graph, init_op, train_op

  def testHintNoMetaGraph(self):
    # Closer to expected usage, but does not check that a re-write actually
    # happens; see testHintDoesRewrite.
    graph, init_op, train_op = self._annotated_graph()
    with graph.as_default():
      manual_memory_config = rewriter_config_pb2.RewriterConfig(
          memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL)
```

## _tensorflow_tools_ci_build_windows_gpu_bazel_run_cc_test_windows_sh
### Line 1-60
```
#!/bin/bash
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
# This script assumes the standard setup on tensorflow Jenkins windows machines.
# It is NOT guaranteed to work on any other machine. Use at your own risk!
#
# REQUIREMENTS:
# * All installed in standard locations:
#   - JDK8, and JAVA_HOME set.
#   - Microsoft Visual Studio 2015 Community Edition
#   - Msys2
#   - Anaconda3
# * Bazel windows executable copied as "bazel.exe" and included in PATH.

# All commands shall pass, and all should be visible.
set -x
set -e

# This script is under <repo_root>/tensorflow/tools/ci_build/windows/cpu/bazel
# Change into repository root.
script_dir=$(dirname $0)
cd ${script_dir%%tensorflow/tools/ci_build/windows/gpu/bazel}.

# Setting up the environment variables Bazel and ./configure needs
source "tensorflow/tools/ci_build/windows/bazel/common_env.sh" \
  || { echo "Failed to source common_env.sh" >&2; exit 1; }

# load bazel_test_lib.sh
source "tensorflow/tools/ci_build/windows/bazel/bazel_test_lib.sh" \
  || { echo "Failed to source bazel_test_lib.sh" >&2; exit 1; }

clean_output_base

run_configure_for_gpu_build

# Compiling the following test is extremely slow with -c opt
slow_compiling_test="//tensorflow/core/kernels:eigen_backward_spatial_convolutions_test"

# Find all the passing cc_tests on Windows and store them in a variable
passing_tests=$(bazel query "kind(cc_test, //tensorflow/cc/... + //tensorflow/core/...) - (${exclude_gpu_cc_tests}) - ($slow_compiling_test)" |
  # We need to strip \r so that the result could be store into a variable under MSYS
  tr '\r' ' ')

# TODO(pcloudy): There is a bug in Bazel preventing build with GPU support without -c opt
# Re-enable this test after it is fixed.
# bazel test --config=win-cuda -k $slow_compiling_test --test_output=errors
bazel test -c opt --config=win-cuda -k $passing_tests --test_output=errors
```

## _tensorflow_examples_adding_an_op_zero_out_op_1_py
### Line 1-18
```
# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""ZeroOut op Python library."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

## _tensorflow_python_kernel_tests_string_split_op_test_py
### Line 1-18
```
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for string_split_op."""

from __future__ import absolute_import
from __future__ import division
```
### Line 252-271
```
  def testSplitV2(self,
                  input,
                  expected,
                  input_is_ragged=False,
                  **kwargs):  # pylint: disable=redefined-builtin
    # Check that we are matching the behavior of Python's str.split:
    self.assertEqual(expected, self._py_split(input, **kwargs))

    # Prepare the input tensor.
    if input_is_ragged:
      input = ragged_factory_ops.constant(input, dtype=dtypes.string)
    else:
      input = constant_op.constant(input, dtype=dtypes.string)

    # Check that the public version (which returns a RaggedTensor) works
    # correctly.
    expected_ragged = ragged_factory_ops.constant(
        expected, ragged_rank=input.shape.ndims)
    actual_ragged_v1 = ragged_string_ops.strings_split_v1(
        input, result_type="RaggedTensor", **kwargs)
```
### Line 280-290
```
    self.assertAllEqual(expected_ragged, actual_ragged_v1_input_kwarg)
    self.assertAllEqual(expected_ragged, actual_ragged_v1_source_kwarg)
    self.assertAllEqual(expected_ragged, actual_ragged_v2)
    self.assertAllEqual(expected_ragged, actual_ragged_v2_input_kwarg)

    # Check that the internal version (which returns a SparseTensor) works
    # correctly.  Note: the internal version oly supports vector inputs.
    if input.shape.ndims == 1:
      expected_sparse = self.evaluate(expected_ragged.to_sparse())
      actual_sparse_v1 = ragged_string_ops.strings_split_v1(
          input, result_type="SparseTensor", **kwargs)
```
### Line 297-306
```
        self.assertEqual(expected_sparse.dense_shape.tolist(),
                         self.evaluate(actual_sparse.dense_shape).tolist())

  def _py_split(self, strings, **kwargs):
    if isinstance(strings, compat.bytes_or_text_types):
      # Note: str.split doesn't accept keyword args.
      if "maxsplit" in kwargs:
        return strings.split(kwargs.get("sep", None), kwargs["maxsplit"])
      else:
        return strings.split(kwargs.get("sep", None))
```

## _tensorflow_python_data_experimental_benchmarks_map_and_batch_benchmark_py
### Line 1-18
```
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Benchmarks for `tf.data.experimental.map_and_batch()`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```
### Line 65-85
```

        with session.Session() as sess:
          sess.run(iterator.initializer, feed_dict={
              shape_placeholder: shape, batch_size_placeholder: batch_size})

          # Use a C++ callable to minimize the Python overhead in the benchmark.
          callable_opts = config_pb2.CallableOptions()
          callable_opts.target.append(next_element.op.name)
          op_callable = sess._make_callable_from_options(callable_opts)  # pylint: disable=protected-access

          # Run five steps to warm up the session caches before taking the
          # first measurement.
          for _ in range(5):
            op_callable()
          deltas = []
          overall_start = time.time()
          # Run at least five repetitions and for at least five seconds.
          while len(deltas) < 5 or time.time() - overall_start < 5.0:
            start = time.time()
            for _ in range(100):
              op_callable()
```
### Line 100-113
```
    NOTE: It is recommended to build the benchmark with
    `-c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-gmlt`
    and execute it on a machine with at least 32 CPU cores.
    """

    # Sequential pipeline configurations.
    seq_elem_size_series = itertools.product([1], [1], [1, 2, 4, 8], [16])
    seq_batch_size_series = itertools.product([1], [1], [1], [8, 16, 32, 64])

    # Parallel pipeline configuration.
    par_elem_size_series = itertools.product([32], [32], [1, 2, 4, 8], [256])
    par_batch_size_series = itertools.product([32], [32], [1],
                                              [128, 256, 512, 1024])
    par_num_calls_series = itertools.product([8, 16, 32, 64], [32], [1], [512])
```
### Line 139-148
```
        return dataset.with_options(options)

      for num_calls, inter_op, element_size, batch_size in series:
        num_iters = 1024 // (
            (element_size * batch_size) // min(num_calls, inter_op))
        # By default the chained map().batch() calls will not be fused.
        chained_dataset = make_dataset(element_size, num_calls, batch_size)
        chained_iterator = dataset_ops.make_one_shot_iterator(chained_dataset)
        chained_get_next = chained_iterator.get_next()
        chained_deltas = []
```
### Line 162-171
```
            iters=num_iters,
            wall_time=np.median(chained_deltas),
            name=name("chained", label, num_calls, inter_op, element_size,
                      batch_size))

        # Apply an option to the default dataset that will fuse map().batch().
        options = dataset_ops.Options()
        options.experimental_optimization.map_and_batch_fusion = True
        fused_dataset = chained_dataset.with_options(options)
        fused_iterator = dataset_ops.make_one_shot_iterator(fused_dataset)
```

## _tensorflow_python_kernel_tests_linalg_init_py
### Line 1-18
```
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Kernel tests for tf.linalg."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

## _tensorflow_python_ops_parallel_for_pfor_py
### Line 1-20
```
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Compiled parallel-for loop."""
# pylint: disable=missing-docstring,g-direct-tensorflow-import

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```
### Line 74-90
```
  multiples = array_ops.concat([length, ones], 0)
  t = array_ops.tile(array_ops.expand_dims(t, 0), multiples)
  return wrap(t, True)


# The following stateful ops can be safely called once, and with the same
# signature as the unconverted version, if their inputs are loop invariant.
# TODO(agarwal): implement a strategy for converting Variable reads/writes. The
# plan is to map each read/write in the loop_fn to a corresponding merged
# read/write in the converted graph. Writes need to be mergeable (e.g.
# AssignAdd) to be used in `pfor`. Given a certain read/write order in the
# loop_fn, doing a one-to-one conversion will simulate executing such
# instructions in lock-step across all iterations.
passthrough_stateful_ops = set([
    "VariableV2",
    "VarHandleOp",
    "ReadVariableOp",
```
### Line 97-114
```

def _is_stateful_pfor_op(op):
  if isinstance(op, WhileOp):
    return op.is_stateful
  if op.type == "Const":
    # Const didn't have an op_def.
    return False
  if op.type in passthrough_stateful_ops:
    return False
  assert hasattr(op, "op_def") and op.op_def is not None, op
  return op.op_def.is_stateful


# pylint: disable=protected-access
class WhileOp(object):
  """Object for storing state for converting the outputs of a while_loop."""

  def __init__(self, exit_node, pfor_ops, pfor_config):
```
### Line 125-187
```
    assert isinstance(exit_node, ops.Tensor)
    self._while_context = exit_node.op._get_control_flow_context()
    assert isinstance(self._while_context, control_flow_ops.WhileContext)
    self._context_name = self._while_context.name
    self._condition = self._while_context.pivot.op.inputs[0]
    # Parts of an external while_loop could be created inside a pfor loop.
    # However for the purpose here, we declare such loops to be external. Also
    # note that we check if the condition was created inside or outside to
    # determine if the while_loop was first created inside or outside.
    # TODO(agarwal): check that the Enter and Exit of this loop are unstacked.
    self._is_inside_loop = self.op_is_inside_loop(self._condition.op)
    if self._is_inside_loop:
      for e in self._while_context.loop_exits:
        assert self.op_is_inside_loop(e.op)

    # Note the code below tries to reverse engineer an existing while_loop graph
    # by assuming the following pattern of nodes.
    #
    #          NextIteration <---- Body <--- Enter
    #              |                ^
    #              V             ___| Y
    #    Enter -> Merge -> Switch___
    #                       ^       | N
    #                       |       V
    #                  LoopCond    Exit

    # Node that elements in the list below correspond one-to-one with each
    # other. i.e. these lists are the same size, and the i_th entry corresponds
    # to different Operations/Tensors of a single cycle as illustrated above.
    # List of Switch ops (ops.Operation) that feed into an Exit Node.
    self._exit_switches = []
    # List of inputs (ops.Tensor) to NextIteration.
    self._body_outputs = []
    # List of list of control inputs of the NextIteration nodes.
    self._next_iter_control_inputs = []
    # List of Merge ops (ops.Operation).
    self._enter_merges = []
    # List of output (ops.Tensor) of Exit nodes.
    self._outputs = []

    # List of Enter Tensors.
    # There are two types of Enter nodes:
    # - The Enter nodes that are used in the `loop_vars` argument to
    # `while_loop` (see
    # https://www.tensorflow.org/api_docs/python/tf/while_loop). We collect
    # these Enter nodes immediately below by tracing backwards from the Exit
    # nodes via Exit <- Switch <- Merge <- Enter. You can see this chain in the
    # diagram above. This allows us to have a 1:1 correspondence between the
    # self._outputs and the first elements in self._enters.
    # - The Enter nodes that are used only by the body. They don't appear in the
    # `loop_vars` and are not returned from the `while_loop`. In Python code,
    # they are usually captured by the body lambda. We collect them below by
    # iterating over all the ops in the graph. They are appended to the end of
    # self._enters or self._direct_enters, and don't correspond to any outputs
    # in self._outputs. Note that we keep the resource/variant Enter nodes in
    # self._direct_enters and the constructed while_loop's body uses them
    # directly as opposed to passing them as loop variables. This is done
    # because the while_body cannot partition the resource/variant Tensors, so
    # it has to leave them unchanged.
    self._enters = []
    self._direct_enters = []

    for e in self._while_context.loop_exits:
```
### Line 198-212
```
      next_iter = merge.inputs[1].op
      assert next_iter.type == "NextIteration", next_iter
      self._body_outputs.append(next_iter.inputs[0])
      self._next_iter_control_inputs.append(next_iter.control_inputs)

    # Collect all the Enter nodes that are not part of `loop_vars`, the second
    # category described above.
    # Also track whether the loop body has any stateful ops.
    self._is_stateful = False
    for op in ops.get_default_graph().get_operations():
      # TODO(agarwal): make sure this works with nested case.
      control_flow_context = op._get_control_flow_context()
      if control_flow_context is None:
        continue
      if control_flow_context.name == self._context_name:
```
### Line 253-264
```
    return self._is_inside_loop

  def op_is_inside_loop(self, op):
    """True if op was created inside the pfor loop body."""
    assert isinstance(op, ops.Operation)
    # Note that we use self._pfor_op_ids for the check and not self._pfor_ops
    # since it appears there tensorflow API could return different python
    # objects representing the same Operation node.
    return op._id in self._pfor_op_ids

  @property
  def is_stateful(self):
```
### Line 300-338
```
        loop_len,
        pfor_ops=self._pfor_ops,
        all_indices=indices,
        all_indices_partitioned=cond_stacked,
        pfor_config=self._pfor_config)
    # Map all inputs of Enter nodes in self._direct_enters to their converted
    # values.
    for enter in self._direct_enters:
      enter_input = enter.op.inputs[0]
      converted_enter, stacked, is_sparse_stacked = parent_pfor._convert_helper(
          enter_input)
      # Since these are resources / variants, they should be unstacked.
      assert not stacked and not is_sparse_stacked, (enter, converted_enter)
      pfor._add_conversion(enter, wrap(converted_enter, False))

    # Map all Enter nodes to the inputs.
    for enter, inp, stacked in zip(self._enters, inputs, inputs_stacked):
      pfor._add_conversion(enter, wrap(inp, stacked))
    # Map outputs of Switch and Merge.
    for i in range(num_outputs):
      wrapped_inp = wrap(inputs[i], inputs_stacked[i])
      merge = self._enter_merges[i]
      pfor._add_conversion(merge.outputs[0], wrapped_inp)
      # Note that second output of Merge is typically not used, except possibly
      # as a control dependency. To avoid trying to output the correct value, we
      # employ a hack here. We output a dummy invalid value with an incorrect
      # dtype. This will allow control dependency to work but if using it as an
      # input, it should typically lead to errors during graph construction due
      # to dtype mismatch.
      # TODO(agarwal): Check in the original graph to see if there are any
      # consumers of this Tensor that use it as an input.
      pfor._add_conversion(merge.outputs[1],
                           wrap(constant_op.constant(-1.0), False))
      switch = self._exit_switches[i]
      # Don't need to worry about switch.output[0] which will feed to Exit node.
      pfor._add_conversion(switch.outputs[1], wrapped_inp)
    return pfor

  def _convert_enter(self, parent_pfor, enter):
```
### Line 376-388
```
        "TensorArrayV3",
        "TensorArraySizeV3",
    ]:
      output = False
    elif _is_stateful_pfor_op(op):
      # This may be fairly aggressive.
      output = True
    elif op.type == "Exit":
      # This may be fairly aggressive.
      output = True
    else:
      for t in op.inputs:
        if self._maybe_stacked(cache, t):
```
### Line 398-458
```
      loop_len = loop_len_vector[0]
      num_outputs = len(self._outputs)

      inputs = []
      maybe_stacked_cache = {}
      # Convert all the Enters. Need to do this before checking for stacking
      # below.
      for i, enter in enumerate(self._enters):
        inp, stacked = self._convert_enter(pfor_input.pfor, enter)
        inputs.append(inp)
        maybe_stacked_cache[enter] = stacked
        # Since this enter node is part of the `loop_vars`, it corresponds to an
        # output and its preceding switch. We mark this switch's output the same
        # stackness, to act at the base case for the logic below. Below, we will
        # be going through the body figuring out which inputs might need to be
        # stacked and which inputs can safely remain unstacked.
        if i < num_outputs:
          maybe_stacked_cache[self._exit_switches[i].outputs[1]] = stacked

      # Shape invariants for init_values corresponding to self._enters.
      input_shape_invariants = []
      # TensorArrays for outputs of converted while loop
      output_tas = []
      # Shape invariants for output TensorArrays.
      ta_shape_invariants = []
      # List of booleans indicating stackness of inputs, i.e. tensors
      # corresponding to self._enters.
      inputs_stacked = []
      for i, inp in enumerate(inputs):
        enter = self._enters[i]
        inp_stacked = self._maybe_stacked(maybe_stacked_cache, enter)
        # Note that even when an input is unstacked, the body could make it
        # stacked. we use a heuristic below to figure out if body may be making
        # it stacked.
        if i < num_outputs:
          body_output = self._body_outputs[i]
          if enter.op in self._pfor_ops:
            body_output_stacked = self._maybe_stacked(maybe_stacked_cache,
                                                      body_output)
          else:
            # If constructed outside of pfor loop, then the output would not be
            # stacked.
            body_output_stacked = False
          if body_output_stacked and not inp_stacked:
            inp = _stack(inp, loop_len_vector).t
            inputs[i] = inp
            inp_stacked = True
          # TODO(agarwal): other attributes for the TensorArray ?
          output_tas.append(tensor_array_ops.TensorArray(inp.dtype, loop_len))
          ta_shape_invariants.append(tensor_shape.TensorShape(None))

        inputs_stacked.append(inp_stacked)
        input_shape_invariants.append(tensor_shape.TensorShape(None))

      # See documentation for __call__ for the structure of init_values.
      init_values = [True, pfor_input.pfor.all_indices] + inputs + output_tas
      # TODO(agarwal): try stricter shape invariants
      shape_invariants = (
          [tensor_shape.TensorShape(None),
           tensor_shape.TensorShape(None)] + input_shape_invariants +
          ta_shape_invariants)
```
### Line 467-512
```
    TensorArrays. Note that we only write to index 0 of output_tas. Since all
    iterations end together, they can all be output together.
    """
    not_all_done = array_ops.reshape(conditions, [])
    new_output_tas = []
    # pylint: disable=cell-var-from-loop
    for i, out_ta in enumerate(output_tas):
      inp = inputs[i]
      new_output_tas.append(
          control_flow_ops.cond(not_all_done, lambda: out_ta,
                                lambda: out_ta.write(0, inp)))
    # pylint: enable=cell-var-from-loop
    return not_all_done, indices, inputs, new_output_tas

  def _process_cond_stacked(self, conditions, indices, inputs, inputs_stacked,
                            output_tas):
    num_outputs = len(self._outputs)
    # Compute if all iterations are done.
    not_all_done = math_ops.reduce_any(conditions)
    conditions_int = math_ops.cast(conditions, dtypes.int32)
    # Partition the indices.
    done_indices, new_indices = data_flow_ops.dynamic_partition(
        indices, conditions_int, 2)

    new_inputs = []
    new_output_tas = []
    for i, (inp, stacked) in enumerate(zip(inputs, inputs_stacked)):
      # Partition the inputs.
      if stacked:
        done_inp, new_inp = data_flow_ops.dynamic_partition(
            inp, conditions_int, 2)
      else:
        # TODO(agarwal): avoid this stacking. See TODO earlier in
        # _process_cond_unstacked.
        done_inp = _stack(inp, [array_ops.size(done_indices)]).t
        new_inp = inp
      new_inputs.append(new_inp)
      # For iterations that are done, write them to TensorArrays.
      if i < num_outputs:
        out_ta = output_tas[i]
        # Note that done_indices can be empty. done_inp should also be empty in
        # that case.
        new_output_tas.append(out_ta.scatter(done_indices, done_inp))
    return not_all_done, new_indices, new_inputs, new_output_tas

  def _process_body(self, pfor_input, inputs_stacked, new_indices, cond_stacked,
```
### Line 523-532
```
      converted_control_inp = []
      for x in control_inputs:
        for t in x.outputs:
          converted_control_inp.append(body_pfor._convert_helper(t).t)
      if stacked:
        # Note convert always does the stacking.
        output = body_pfor.convert(body_output)
      else:
        output, convert_stacked, _ = body_pfor._convert_helper(body_output)
        assert convert_stacked == stacked, body_output
```
### Line 539-557
```

    for i, (body_output,
            stacked) in enumerate(zip(self._body_outputs, inputs_stacked)):
      control_inp = self._next_iter_control_inputs[i]
      out_dtype = body_output.dtype
      # Note that we want to run the body only if not all pfor iterations are
      # done. If all are done, we return empty tensors since these values will
      # not be used. Notice that the value returned by the loop is based on
      # TensorArrays and not directly on these returned values.
      # pylint: disable=cell-var-from-loop
      new_output = control_flow_ops.cond(
          not_all_done,
          lambda: true_fn(control_inp, body_pfor, body_output, stacked),
          lambda: constant_op.constant([], dtype=out_dtype))
      # pylint: enable=cell-var-from-loop
      new_outputs.append(new_output)
    return new_outputs

  def __call__(self, pfor_input):
```
### Line 594-629
```
        node from this while loop.

    Returns:
      List of converted outputs.
    """
    # Create init_values that will be passed to the while_loop.
    init_values, inputs_stacked, shape_invariants = self._create_init_values(
        pfor_input)
    # Note that we use a list as a hack since we need the nested function body
    # to set the value of cond_is_stacked. python2.x doesn't support nonlocal
    # variables.
    cond_is_stacked = [None]

    def cond(not_all_done, *_):
      return not_all_done

    def body(not_all_done, indices, *args):
      # See documentatin for __call__ for the structure of *args.
      num_enters = len(self._enters)
      inputs = args[:num_enters]
      output_tas = args[num_enters:]
      # TODO(agarwal): see which outputs have consumers and only populate the
      # TensorArrays corresponding to those. Or do those paths get trimmed out
      # from inside the while_loop body?
      assert len(inputs) >= len(output_tas)
      assert len(inputs) == len(inputs_stacked)

      # Convert condition
      with ops.name_scope("while_cond"):
        # Note that we set cond_stacked to True here. At this point we don't
        # know if it could be loop invariant, hence the conservative value is
        # to assume stacked.
        cond_pfor = self._init_pfor(
            pfor_input.pfor,
            indices,
            cond_stacked=True,
```
### Line 630-640
```
            inputs=inputs,
            inputs_stacked=inputs_stacked)
        conditions, cond_stacked, _ = cond_pfor._convert_helper(self._condition)
        cond_is_stacked[0] = cond_stacked

      # Recompute the new condition, write outputs of done iterations, and
      # partition the inputs if needed.
      if not cond_stacked:
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_unstacked(conditions, indices,
                                                        inputs, output_tas)
```
### Line 642-660
```
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_stacked(conditions, indices,
                                                      inputs, inputs_stacked,
                                                      output_tas)

      # Convert body
      with ops.name_scope("while_body"):
        #  Compute the outputs from the body.
        new_outputs = self._process_body(pfor_input, inputs_stacked,
                                         new_indices, cond_stacked, new_inputs,
                                         not_all_done)

      # Note that the first num_outputs new values of inputs are computed using
      # the body. Rest of them were direct Enters into the condition/body and
      # the partitioning done earlier is sufficient to give the new value.
      num_outputs = len(self._outputs)
      new_args = ([not_all_done, new_indices] + new_outputs +
                  list(new_inputs[num_outputs:]) + new_output_tas)
      return tuple(new_args)
```
### Line 666-677
```
    assert cond_is_stacked[0] is not None
    for inp_stacked, ta in zip(inputs_stacked, output_tas):
      if cond_is_stacked[0]:
        outputs.append(wrap(ta.stack(), True))
      else:
        # Note that if while_loop condition is unstacked, all iterations exit at
        # the same time and we wrote those outputs in index 0 of the tensor
        # array.
        outputs.append(wrap(ta.read(0), inp_stacked))
    return outputs


```
### Line 715-724
```
    rank they will need to be broadcasted to.
    """
    if not self._inputs:
      return

    # Find max rank
    def _get_rank(x):
      rank = array_ops.rank(x.t)
      if not x.is_stacked:
        rank += 1
```
### Line 842-870
```
  node will have two inputs: the tensor to reshape, and the new shape.  The
  example here only handles the case where the shape is loop invariant.

  @RegisterPFor("Reshape")
  def _convert_reshape(pfor_input):
    # We assume that input is not loop invariant. Call to `stacked_input`
    # asserts that and returns the converted value. This value will have a rank
    # larger by 1 compared to the rank of the input in the loop body.
    t = pfor_input.stacked_input(0)

    # We assume that shape input is loop invariant. Call to `unstacked_input`
    # asserts that and returns the converted value.
    shape = pfor_input.unstacked_input(1)

    # We compute `new_shape` by prepending the number of iterations to the
    # original shape.
    new_shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape],
                                 axis=0)

    # The vectorized output involves reshaping the converted input `t` using
    # `new_shape`.
    new_output = array_ops.reshape(t, new_shape)

    # The converted output is marked as not loop invariant using the call to
    # wrap.
    return wrap(new_output, True)
  """

  def __init__(self, op_type):
```
### Line 903-912
```

    super(RegisterPForWithArgs, self).__call__(_f)
    return converter


# TODO(agarwal): call raw_ops instead of calling these low level routines.
def _create_op(op_type, inputs, op_dtypes, attrs=None):
  """Utility to create an op."""
  op = ops.get_default_graph().create_op(
      op_type, inputs, op_dtypes, attrs=attrs, compute_device=True)
```
### Line 980-992
```

class PForConfig(object):
  """A configuration object used to communicate with loop body function."""

  def __init__(self):
    # This may be set to the number of iterations.
    self._maybe_iters = None
    # Map from reduction node, created by `reduce`, to the bundle of reduction
    # function and arguments.
    self._reduce_map = {}

  def _has_reductions(self):
    """True if some reductions where performed by loop body."""
```
### Line 1014-1023
```
    Returns:
      The result of running `fn` on the vectorized versions of `*args`. These
      outputs will be available as loop invariant values to all the iterations.
    """
    assert not context.executing_eagerly()
    # Creates a concrete function that will be used for reduction.
    tensor_specs = []
    for arg in args:
      if not isinstance(arg, ops.Tensor):
        raise ValueError("Got a non-Tensor argument %s in reduce" % arg)
```
### Line 1026-1051
```
      tensor_specs.append(
          tensor_spec.TensorSpec(shape=batched_shape, dtype=arg.dtype))
    concrete_function = def_function.function(fn).get_concrete_function(
        *tensor_specs)

    # Creates PlaceholderWithDefault and IdentityN nodes corresponding the the
    # reduction.
    pl_outputs = []
    with ops.control_dependencies(args):
      for output in concrete_function.outputs:
        if not isinstance(output, ops.Tensor):
          raise ValueError("Got a non-Tensor output %s while running reduce" %
                           output)
        # Note that we use placeholder_with_default just to make XLA happy since
        # it does not like placeholder ops.
        if output.shape.is_fully_defined():
          dummy = array_ops.zeros(output.shape.as_list(), dtype=output.dtype)
          pl_outputs.append(
              array_ops.placeholder_with_default(dummy, shape=output.shape))
        else:
          # TODO(agarwal): support case when under XLA and output.shape is not
          # fully defined.
          pl_outputs.append(
              array_ops.placeholder(output.dtype, shape=output.shape))

      reduction_op = array_ops.identity_n(pl_outputs)[0].op
```
### Line 1053-1062
```
    if len(reduction_op.outputs) == 1:
      return reduction_op.outputs[0]
    else:
      return tuple(reduction_op.outputs)

  # TODO(agarwal): handle reductions inside control flow constructs.
  def reduce_concat(self, x):
    """Performs a concat reduction on `x` across pfor iterations.

    Note that this currently may not work inside a control flow construct.
```
### Line 1180-1191
```
    self._pfor_config = pfor_config

  def op_is_inside_loop(self, op):
    """True if op was created inside the pfor loop body."""
    assert isinstance(op, ops.Operation)
    # Note that we use self._pfor_op_ids for the check and not self._pfor_ops
    # since it appears there tensorflow API could return different python
    # objects representing the same Operation node.
    return op._id in self._pfor_op_ids

  def _convert_sparse(self, y):
    """Returns the converted value corresponding to SparseTensor y.
```
### Line 1227-1238
```

    assert not any(w.is_sparse_stacked for w in outputs), (
        "Error converting SparseTensor. All components should be logically "
        "stacked, or none.")

    # If component tensors were not sparsely stacked, they are either unstacked
    # or stacked without knowledge that they are components of sparse tensors.
    # In this case, we have to restack them.
    return self._restack_sparse_tensor_logically(
        *[self._unwrap_or_tile(w) for w in outputs])

  def _restack_sparse_tensor_logically(self, indices, values, shape):
```
### Line 1243-1255
```
    def fn(args):
      res = gen_sparse_ops.serialize_sparse(
          args[0], args[1], args[2], out_type=dtypes.variant)
      return res

    # Applies a map function to the component tensors to serialize each
    # sparse tensor element and batch them all, then deserializes the batch.
    # TODO(rachelim): Try to do this without map_fn -- add the right offsets
    # to shape and indices tensors instead.
    result = map_fn.map_fn(fn, [indices, values, shape], dtype=dtypes.variant)
    return sparse_ops.deserialize_sparse(
        result, dtype=values.dtype, rank=sparse_tensor_rank)

```
### Line 1296-1305
```
    assert isinstance(old_output, (ops.Tensor, ops.Operation)), old_output
    assert isinstance(new_output, (WrappedTensor, ops.Operation)), new_output
    self._conversion_map[old_output] = new_output

  def _convert_reduction(self, y):
    # Handle reductions.
    if self._pfor_config is None:
      return None
    reduction = self._pfor_config._lookup_reduction(y)
    if reduction is None:
```
### Line 1306-1320
```
      return None
    (reduction_fn, reduction_args) = reduction
    batched_args = []
    for reduction_arg in reduction_args:
      assert isinstance(reduction_arg, ops.Tensor), reduction_arg
      # Tensor being reduced should already be converted due to a control
      # dependency on the created placeholder.
      # Note that in cases where reduction_arg is in an outer context, one
      # needs to locate the corresponding Enter node and use that to lookup
      # the conversion.
      # TODO(agarwal): handle reductions inside control flow constructs.
      assert reduction_arg in self._conversion_map, (
          "Unable to handle reduction of %s, possibly as it was used "
          "inside a control flow construct. Note that reductions across "
          "pfor iterations are currently not supported inside control flow "
```
### Line 1345-1369
```
      is_while_loop = y_op.type == "Exit"
      if is_while_loop:
        while_op = WhileOp(
            y, pfor_ops=self._pfor_ops, pfor_config=self._pfor_config)
        is_inside_loop = while_op.is_inside_loop
        # If all nodes in the while_loop graph were created inside the pfor, we
        # treat the whole loop subgraph as a single op (y_op) and try to convert
        # it. For while_loops that are created completely or partially outside,
        # we treat them as external and should be able to simply return the Exit
        # node output as is without needing any conversion. Note that for
        # while_loops that are partially constructed inside, we assume they will
        # be loop invariant. If that is not the case, it will create runtime
        # errors since the converted graph would depend on the self._loop_var
        # placeholder.
        if is_inside_loop:
          y_op = while_op
      else:
        is_inside_loop = self.op_is_inside_loop(y_op)

      # If this op was not created inside the loop body, we will return as is.
      # 1. Convert inputs and control inputs.

      def _add_to_stack(x):
        if x not in self._conversion_map:
          stack.insert(0, x)
```
### Line 1409-1428
```
        converted_inputs = []
        converted_control_ops = []
      logging.vlog(3, "converting op:%s\ninputs:%s\ncontrol_inputs:%s", y_op,
                   converted_inputs, converted_control_ops)

      # 2. Convert y_op
      # If converting a while_loop, we let the while_loop convertor deal with
      # putting the control dependencies appropriately.
      control_dependencies = [] if is_while_loop else converted_control_ops
      with ops.control_dependencies(control_dependencies), ops.name_scope(
          y_op.name + "/pfor/"), ops.get_default_graph()._original_op(y_op):
        # Op is a placeholder for a reduction.
        reduce_output = self._convert_reduction(y)
        if reduce_output is not None:
          new_outputs = reduce_output
        # None of the inputs and control inputs were converted.
        elif ((not is_inside_loop or
               (not is_stateful and not some_input_converted and
                not some_control_input_converted)) and
              y.graph == ops.get_default_graph()):
```
### Line 1430-1451
```
            assert not isinstance(y_op, WhileOp)
            new_outputs = y_op
          else:
            new_outputs = [wrap(x, False) for x in y_op.outputs]
        elif not (is_stateful or is_while_loop or some_input_stacked):
          # All inputs are unstacked or uncoverted but some control inputs are
          # converted.
          # TODO(rachelim): Handle the case where some inputs are sparsely
          # stacked (i.e. any(x.is_sparse_stacked for x in converted_inputs))
          new_op = _create_op(y_op.type, [x.t for x in converted_inputs],
                              [x.dtype for x in y_op.outputs],
                              y_op.node_def.attr)
          if y is y_op:
            new_outputs = new_op
          else:
            new_outputs = [wrap(x, False) for x in new_op.outputs]
        else:
          # Either some inputs are not loop invariant or op is stateful.
          if hasattr(y_op, "pfor_converter"):
            converter = y_op.pfor_converter
          else:
            converter = _pfor_converter_registry.get(y_op.type, None)
```
### Line 1456-1467
```
              raise ValueError("No converter defined for %s\n%s\ninputs: %s. "
                               "\nEither add a converter or set "
                               "--op_conversion_fallback_to_while_loop=True, "
                               "which may run slower" %
                               (y_op.type, y_op, converted_inputs))
          # TODO(rachelim): Handle the case where some inputs are sparsely
          # stacked. We should only call the converter if it supports handling
          # those inputs.
          pfor_inputs = _PforInput(self, y_op, converted_inputs)
          try:
            new_outputs = converter(pfor_inputs)
          except Exception as e:  # pylint: disable=broad-except
```
### Line 1485-1494
```
            new_outputs = [new_outputs]
          assert isinstance(new_outputs,
                            (list, tuple, ops.Operation)), new_outputs
        logging.vlog(2, "converted %s %s", y_op, new_outputs)

        # Insert into self._conversion_map
        if y is y_op:
          assert isinstance(new_outputs, ops.Operation)
          self._add_conversion(y_op, new_outputs)
        else:
```
### Line 1495-1504
```
          assert len(y_op.outputs) == len(new_outputs), (y_op, y_op.outputs,
                                                         new_outputs)
          for old_output, new_output in zip(y_op.outputs, new_outputs):
            assert isinstance(new_output, WrappedTensor), (new_output, y, y_op)
            assert old_output.dtype == new_output.t.dtype, (new_output, y, y_op)
            # Set shape for converted output.
            output_shape = old_output.shape
            if not new_output.is_sparse_stacked:
              if new_output.is_stacked:
                loop_len = tensor_util.constant_value(self.loop_len_vector)
```
### Line 1540-1552
```
      may be active.
    """
    return self._all_indices_partitioned


# The code below defines converters for different operations. Please see comment
# for RegisterPFor to see how converters should be defined.

# nn_ops


def _flatten_first_two_dims(x):
  """Merges first two dimensions."""
```
### Line 1630-1675
```
      reverse_order = order
    else:
      order = [1, 2, 3, 0, 4]
      shape = array_ops.concat([x_shape[1:4], [-1]], axis=0)
      reverse_order = [3, 0, 1, 2, 4]
    # Move S dimension next to C dimension.
    x = array_ops.transpose(x, order)
    reverse_shape = array_ops.shape(x)
    # Reshape to merge the S and C dimension.
    x = array_ops.reshape(x, shape)
    outputs = x, reverse_order, reverse_shape
    _channel_flatten_input_cache[cache_key] = outputs
  else:
    outputs = _channel_flatten_input_cache[cache_key]
  return outputs


# Note that with training=True, running FusedBatchNormV3 on individual examples
# is very different from running FusedBatchNormV3 on a batch of those examples.
# This is because, for the latter case, the operation can be considered as first
# computing the mean and variance over all the examples and then using these
# to scale all those examples. This creates a data dependency between these
# different "iterations" since the inputs to the scaling step depends on the
# statistics coming from all these inputs.
# As with other kernels, the conversion here effectively runs the kernel
# independently for each iteration, and returns outputs by stacking outputs from
# each of those iterations.
@RegisterPFor("FusedBatchNormV3")
def _convert_fused_batch_norm(pfor_input):
  is_training = pfor_input.get_attr("is_training")
  # When BatchNorm is used with training=False, mean and variance are provided
  # externally and used as is by the op. Thus, we can merge the S and N
  # dimensions as we do for regular operations.
  # When BatchNorm is used with training=True, mean and variance are computed
  # for each channel across the batch dimension (first one). If we merge S and N
  # dimensions, mean and variances will be computed over a larger set. So, we
  # merge the S and C dimensions instead.
  if not is_training:
    # We return zeros for batch_mean and batch_variance output. Note that CPU
    # and GPU seem to have different behavior for those two outputs. CPU outputs
    # zero because these values are not used during inference. GPU outputs
    # something, probably real means and variances.
    inputs = _inputs_with_flattening(pfor_input, [0])
    outputs = _create_op(
        pfor_input.op_type,
        inputs, [x.dtype for x in pfor_input.outputs],
```
### Line 1681-1695
```
    zeros = array_ops.zeros_like(mean)
    return [wrap(y, True)] + [wrap(zeros, False)] * 5

  pfor_input.stack_inputs()
  data_format = pfor_input.get_attr("data_format")
  # We merge the first dimension with the "C" dimension, run FusedBatchNormV3,
  # and then transpose back.
  x = pfor_input.stacked_input(0)
  x, reverse_order, reverse_shape = _channel_flatten_input(x, data_format)
  # Note that we stack all the other inputs as well so that they are the same
  # size as the new size of the channel dimension.
  inputs = [x] + [
      array_ops.reshape(pfor_input.stacked_input(i), [-1])
      for i in range(1, pfor_input.num_inputs)
  ]
```
### Line 1736-1745
```
def _convert_flatten_batch_shape_input(pfor_input, op_type, flatten_dims,
                                       shape_dim):
  del op_type
  inputs = _inputs_with_flattening(pfor_input, flatten_dims)
  n = pfor_input.pfor.loop_len_vector
  # Adjust the `input_sizes` input.
  ones = array_ops.ones([array_ops.shape(inputs[shape_dim])[0] - 1],
                        dtype=n.dtype)
  inputs[shape_dim] *= array_ops.concat([n, ones], axis=0)
  outputs = _create_op(
```
### Line 1760-1769
```
  padding = pfor_input.get_attr("padding")
  use_cudnn_on_gpu = pfor_input.get_attr("use_cudnn_on_gpu")
  data_format = pfor_input.get_attr("data_format")
  dilations = pfor_input.get_attr("dilations")
  if inputs_stacked:
    # TODO(agarwal): Implement this efficiently.
    logging.warn("Conv2DBackpropFilter uses a while_loop. Fix that!")

    def while_body(i, ta):
      inp_i = inputs[i, ...]
```
### Line 1784-1796
```
        lambda i, ta: i < n, while_body,
        (0, tensor_array_ops.TensorArray(inputs.dtype, n)))
    output = ta.concat()
    return wrap(output, True)
  else:
    # We merge the stack dimension with the channel dimension of the gradients
    # and pretend we had a larger filter (see change to filter_sizes below).
    # Once the filter backprop is computed, we reshape and transpose back
    # appropriately.
    grads, _, _ = _channel_flatten_input(grads, data_format)
    n = pfor_input.pfor.loop_len_vector
    old_filter_sizes = filter_sizes
    filter_sizes *= array_ops.concat([[1, 1, 1], n], axis=0)
```
### Line 1814-1823
```
def _convert_softmax(pfor_input, op_type, op_func):
  del op_type
  return wrap(op_func(pfor_input.stacked_input(0)), True)


# array_ops


@RegisterPForWithArgs("Identity", array_ops.identity)
@RegisterPForWithArgs("StopGradient", array_ops.stop_gradient)
```
### Line 1848-1860
```
def _convert_broadcast_to(pfor_input):
  t = pfor_input.stacked_input(0)
  shape = pfor_input.unstacked_input(1)
  new_shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape], axis=0)

  # Expand dims of stacked t to broadcast against the new shape.
  # TODO(davmre): consider factoring out common code with
  # `expanddim_inputs_for_broadcast`, which has similar logic but with
  # implicit shapes (of input Tensors) rather than explicit shapes.
  rank_diff = array_ops.shape(new_shape)[0] - array_ops.rank(t)
  ones = array_ops.tile([1], array_ops.reshape(rank_diff, [1]))
  t_shape = array_ops.shape(t)
  t_expanded_shape = array_ops.concat([t_shape[:1], ones, t_shape[1:]], axis=0)
```
### Line 1900-1911
```
  t = pfor_input.stacked_input(0)
  diag = pfor_input.stacked_input(1)
  return wrap(array_ops.matrix_set_diag(t, diag), True)


# Registrations for MatrixDiagV2, MatrixDiagPartv2, and MatrixSetDiagV2.
# The input orders defined in the OpKernel and the actual python API are
# different (for compatibility with V1), so we cannot use _convert_identity.
@RegisterPFor("MatrixDiagV2")
def _convert_matrix_diag_v2(pfor_input):
  diagonal = pfor_input.stacked_input(0)
  k = pfor_input.unstacked_input(1)
```
### Line 1919-1928
```
          num_rows=num_rows,
          num_cols=num_cols,
          padding_value=padding_value), True)


# See notes for MatrixDiagV2
@RegisterPFor("MatrixDiagPartV2")
def _convert_matrix_diag_part_v2(pfor_input):
  input = pfor_input.stacked_input(0)  # pylint:disable=redefined-builtin
  k = pfor_input.unstacked_input(1)
```
### Line 1929-1938
```
  padding_value = pfor_input.unstacked_input(2)
  return wrap(
      array_ops.matrix_diag_part(input, k=k, padding_value=padding_value), True)


# See notes for MatrixDiagV2
@RegisterPFor("MatrixSetDiagV2")
def _convert_matrix_set_diag_v2(pfor_input):
  pfor_input.stack_inputs([0, 1])
  input = pfor_input.stacked_input(0)  # pylint:disable=redefined-builtin
```
### Line 2050-2059
```
  if op_type == "Gather":
    validate_indices = pfor_input.get_attr("validate_indices")
    axis = 0
  else:
    validate_indices = None
    # Assume we will never have a Tensor with rank > 2**32.
    axis = math_ops.cast(pfor_input.unstacked_input(2), dtypes.int32)
    axis_value = tensor_util.constant_value(axis)
    if axis_value is not None:
      axis = axis_value
```
### Line 2060-2073
```
  if indices_stacked and not param_stacked:
    if indices is pfor_input.pfor.all_indices and axis == 0:
      param_shape0 = tensor_shape.dimension_value(param.shape[0])
      indices_shape0 = tensor_shape.dimension_value(indices.shape[0])
      if param_shape0 is not None and indices_shape0 == param_shape0:
        # Note that with loops and conditionals, indices may not be contiguous.
        # However they will be sorted and unique. So if the shape matches, then
        # it must be picking up all the rows of param.
        return wrap(param, True)
      # TODO(agarwal): use array_ops.slice here.
    output = array_ops.gather(
        param, indices, validate_indices=validate_indices, axis=axis)
    if axis != 0:
      axis = control_flow_ops.cond(axis < 0,
```
### Line 2086-2106
```
    loop_len_vector = pfor_input.pfor.loop_len_vector
    pfor_input.stack_inputs(stack_indices=[1])
    indices = pfor_input.stacked_input(1)
    param_flat = _flatten_first_two_dims(param)

    # Recompute indices to handle stacked param.
    indices_offset = (math_ops.range(math_ops.cast(loop_len_vector[0],
                                                   dtype=indices.dtype)) *
                      math_ops.cast(array_ops.shape(param)[1], indices.dtype))
    # Reshape indices_offset to allow broadcast addition
    ones = array_ops.ones([array_ops.rank(indices) - 1], dtype=dtypes.int32)
    new_shape = array_ops.concat([loop_len_vector, ones], axis=0)
    indices_offset = array_ops.reshape(indices_offset, new_shape)
    indices += indices_offset

    # TODO(agarwal): handle axis != 0. May need to transpose param or
    # array_ops.gather_nd.
    if isinstance(axis, ops.Tensor):
      axis_value = tensor_util.constant_value(axis)
    else:
      try:
```
### Line 2118-2127
```
    return wrap(output, True)


@RegisterPFor("GatherNd")
def _convert_gather_nd(pfor_input):
  # TODO(jmenick): Add support for unstacked params.
  pfor_input.stack_inputs(stack_indices=[1])
  params = pfor_input.stacked_input(0)
  indices = pfor_input.stacked_input(1)
  stacked_result = array_ops.gather_nd(params, indices, batch_dims=1)
```
### Line 2206-2220
```
          ellipsis_mask=ellipsis_mask,
          new_axis_mask=new_axis_mask,
          shrink_axis_mask=shrink_axis_mask), True)


# math_ops


@RegisterPFor("MatMul")
def _convert_matmul(pfor_input):
  # TODO(agarwal): Check if tiling is faster than two transposes.
  a, a_stacked, _ = pfor_input.input(0)
  b, b_stacked, _ = pfor_input.input(1)
  tr_a = pfor_input.get_attr("transpose_a")
  tr_b = pfor_input.get_attr("transpose_b")
```
### Line 2238-2249
```
    assert b_stacked
    if tr_b:
      perm = [2, 0, 1]
      b = array_ops.transpose(b, perm)
    else:
      # As an optimization, if one of the first two dimensions is 1, then we can
      # reshape instead of transpose.
      # TODO(agarwal): This check can be done inside Transpose kernel.
      b_shape = array_ops.shape(b)
      min_dim = math_ops.minimum(b_shape[0], b_shape[1])
      perm = control_flow_ops.cond(
          math_ops.equal(min_dim, 1), lambda: [0, 1, 2], lambda: [1, 0, 2])
```
### Line 2263-2277
```
    prod = array_ops.reshape(prod, [-1, y, z])
    prod = array_ops.transpose(prod, [1, 0, 2])
    return wrap(prod, True)


# TODO(rmlarsen): Use the converter of BatchMatMulV2 once compatibility window
# is met.
@RegisterPFor("BatchMatMul")
def _convert_batch_mat_mul(pfor_input):
  # TODO(agarwal): There may be a more efficient way to do this instead of
  # stacking the inputs.
  pfor_input.stack_inputs()
  x = pfor_input.stacked_input(0)
  y = pfor_input.stacked_input(1)
  adj_x = pfor_input.get_attr("adj_x")
```
### Line 2304-2313
```
@RegisterPForWithArgs("All", math_ops.reduce_all)
@RegisterPForWithArgs("Any", math_ops.reduce_any)
def _convert_reduction(pfor_input, _, op_func):
  t = pfor_input.stacked_input(0)
  indices = pfor_input.unstacked_input(1)
  # Shift positive indices by one to account for the extra dimension.
  indices += math_ops.cast(indices >= 0, dtypes.int32)
  keep_dims = pfor_input.get_attr("keep_dims")
  return wrap(op_func(t, indices, keepdims=keep_dims), True)

```
### Line 2315-2324
```
@RegisterPForWithArgs("Cumsum", math_ops.cumsum)
@RegisterPForWithArgs("Cumprod", math_ops.cumprod)
def _convert_cumfoo(pfor_input, _, op_func):
  t = pfor_input.stacked_input(0)
  axis = pfor_input.unstacked_input(1)
  # Shift positive indices by one to account for the extra dimension.
  axis += math_ops.cast(axis >= 0, dtypes.int32)
  exclusive = pfor_input.get_attr("exclusive")
  reverse = pfor_input.get_attr("reverse")
  return wrap(op_func(t, axis, exclusive=exclusive, reverse=reverse), True)
```
### Line 2328-2337
```
def _convert_biasadd(pfor_input):
  t, t_stacked, _ = pfor_input.input(0)
  bias, bias_stacked, _ = pfor_input.input(1)
  data_format = pfor_input.get_attr("data_format").decode()
  if bias_stacked:
    # BiasAdd only supports 1-D biases, so cast bias to match value and use Add.
    pfor_input.expanddim_inputs_for_broadcast()
    t, _, _ = pfor_input.input(0)
    bias = math_ops.cast(pfor_input.stacked_input(1), t.dtype)
    if compat.as_bytes(data_format) == b"NCHW":
```
### Line 2355-2364
```
@RegisterPFor("UnsortedSegmentSum")
def _convert_unsortedsegmentsum(pfor_input):
  pfor_input.stack_inputs([0, 1])
  data = pfor_input.stacked_input(0)
  segment_ids = pfor_input.stacked_input(1)
  # TODO(agarwal): handle stacked?
  num_segments = pfor_input.unstacked_input(2)
  if segment_ids.dtype != num_segments.dtype:
    segment_ids = math_ops.cast(segment_ids, dtypes.int64)
    num_segments = math_ops.cast(num_segments, dtypes.int64)
```
### Line 2379-2388
```
  return wrap(output, True)


def _flatten_array_with_offset(ids, offset_delta, num_rows):
  """Flattens a rank 2 tensor, adding an offset to each row."""
  # Note that if `ids` is rank 1, it is broadcast to rank 2.
  offset_delta = math_ops.cast(offset_delta, ids.dtype)
  n = math_ops.cast(num_rows, dtype=ids.dtype)
  offsets = math_ops.range(
      start=0, limit=n * offset_delta, delta=offset_delta, dtype=ids.dtype)
```
### Line 2407-2417
```
  data, data_stacked, _ = pfor_input.input(0)
  indices, _, _ = pfor_input.input(1)
  num_inputs = len(pfor_input.inputs)
  assert num_inputs in (3, 4)
  if num_inputs == 3:
    # `segment_ids` needs to be unstacked since otherwise output sizes could
    # differ across pfor iterations.
    segment_ids = pfor_input.unstacked_input(2)
    num_segments = nn_ops.relu(math_ops.reduce_max(segment_ids) + 1)
  else:
    segment_ids, _, _ = pfor_input.input(2)
```
### Line 2552-2562
```
@RegisterPForWithArgs("TruncateMod", math_ops.truncate_mod)
@RegisterPForWithArgs("Xdivy", math_ops.xdivy)
@RegisterPForWithArgs("Xlogy", math_ops.xlogy)
@RegisterPForWithArgs("Zeta", math_ops.zeta)
def _convert_cwise(pfor_input, op_type, op_func):
  # Note that ops handled here do not have attributes except those listed below
  # and hence don't need extra arguments passed to the cwise_op call below.
  for attr in pfor_input.op.node_def.attr.keys():
    assert attr in [u"T", u"Tout", u"_xla_compile_id"], (op_type, attr)
  pfor_input.expanddim_inputs_for_broadcast()
  return wrap(op_func(*[x.t for x in pfor_input.inputs]), True)
```
### Line 2623-2632
```
  return wrap(array_ops.rank(pfor_input.stacked_input(0)) - 1, False)


@RegisterPFor("AddN")
def _convert_addn(pfor_input):
  # AddN does not support broadcasting.
  pfor_input.stack_inputs()
  return wrap(math_ops.add_n([x.t for x in pfor_input.inputs]), True)


```
### Line 2651-2661
```
    output = array_ops.reshape(grad, [first_dim_shape, -1, last_dim_shape])
    output = math_ops.reduce_sum(output, axis=[1], keepdims=False)
  return wrap(output, True)


# Some required ops are not exposed under the tf namespace. Hence relying on
# _create_op to create them.
@RegisterPForWithArgs("EluGrad")
@RegisterPForWithArgs("Relu6Grad")
@RegisterPForWithArgs("ReluGrad")
@RegisterPForWithArgs("SeluGrad")
```
### Line 2667-2677
```
@RegisterPForWithArgs("RsqrtGrad")
@RegisterPForWithArgs("ReciprocalGrad")
def _convert_grads(pfor_input, op_type, *args, **kw_args):
  del args
  del kw_args
  # TODO(agarwal): Looks like these ops don't support broadcasting. Hence we
  # have to use tiling here.
  pfor_input.stack_inputs()
  outputs = _create_op(
      op_type, [x.t for x in pfor_input.inputs],
      [x.dtype for x in pfor_input.outputs],
```
### Line 2707-2716
```
  e = pfor_input.input(2)[0]
  out = array_ops.where_v2(cond, t, e)
  return wrap(out, True)


# random_ops


def _transpose_dim_to_front(x, dim):
  rank = array_ops.rank(x)
```
### Line 2728-2737
```
@RegisterPForWithArgs("TruncatedNormal")
def _convert_random(pfor_input, op_type, *args, **kw_args):
  del args
  del kw_args
  inputs = [pfor_input.unstacked_input(i) for i in range(pfor_input.num_inputs)]
  # inputs[0] is "shape"
  inputs[0] = array_ops.concat([pfor_input.pfor.loop_len_vector, inputs[0]],
                               axis=0)
  logging.warning(
      "Note that %s inside pfor op may not give same output as "
```
### Line 2745-2754
```

@RegisterPFor("RandomGamma")
@RegisterPFor("RandomPoissonV2")
def _convert_random_with_param(pfor_input):
  shape = pfor_input.unstacked_input(0)
  # param is lam (Poisson rate) or alpha (Gamma shape).
  param, param_stacked, _ = pfor_input.input(1)
  logging.warning(
      "Note that %s inside pfor op may not give same output as "
      "inside a sequential loop.", pfor_input.op_type)
```
### Line 2804-2828
```
        array_ops.reshape(samples, [-1, n, num_samples]), [1, 0, 2])

  return wrap(stacked_samples, True)


# linalg_ops


# TODO(jmenick) - the same logic applies to other einsums. Generalize this
# in a future CL.
@RegisterPFor("XlaEinsum")
def _convert_einsum(pfor_input):
  first_input, first_input_stacked, _ = pfor_input.input(0)
  second_input, second_input_stacked, _ = pfor_input.input(1)

  # Parse the einsum equation.
  equation = pfor_input.get_attr("equation").decode("utf-8")
  input_expr, output_expr = equation.split("->")
  input_a_expr, input_b_expr = input_expr.split(",")

  # pick a placeholder symbol to use for the new axis
  chosen_symbol = None
  for s in string.ascii_letters:
    if s in equation:
      continue
```
### Line 2872-2885
```
@RegisterPFor("SelfAdjointEigV2")
def _convert_self_adjoint_eig(pfor_input):
  t = pfor_input.stacked_input(0)
  compute_v = pfor_input.get_attr("compute_v")
  e, v = gen_linalg_ops.self_adjoint_eig_v2(t, compute_v=compute_v)
  # If compute_v is False, v will have shape [0].
  return wrap(e, True), wrap(v, compute_v)


# logging_ops


@RegisterPFor("Assert")
def _convert_assert(pfor_input):
```
### Line 2892-2948
```
      "Assert", [cond] + data_list, [], attrs=pfor_input.op.node_def.attr)


@RegisterPFor("Print")
def _convert_print(pfor_input):
  # Note that we don't stack all the inputs. Hence unstacked values are printed
  # once here vs multiple times in a while_loop.
  pfor_input.stack_inputs([0])
  outputs = _create_op(
      "Print", [x.t for x in pfor_input.inputs],
      [x.dtype for x in pfor_input.outputs],
      attrs=pfor_input.op.node_def.attr).outputs
  return [wrap(x, True) for x in outputs]


# data_flow_ops

# TensorArray conversion is tricky since we don't support arrays of
# TensorArrays. For converting them, we consider two distinct cases:
#
# 1. The array is constructed outside the pfor call, and read/written inside the
# loop.
# This is an easier case since we don't need to make an array of TensorArrays.
# A correctness requirement is that these parallel iterations shouldn't attempt
# to write to the same location. Hence at conversion time we disallow indices to
# be loop-invariant as that would guarantee a collision. Even if the indices are
# not loop-invariant, they could conflict and that shall trigger runtime errors.
#
# 2. The array is constructed and used entirely inside each pfor iteration.
# For simplicity, here we require that the indices used for write/scatter are
# "unstacked". Otherwise it becomes hard to merge the TensorArrays created in
# different pfor iterations. We consider two sub_cases:
#
# 2a Elements written to the array are "stacked"
# To simulate multiple TensorArrays, we may increase the dimension of each
# element of the array. i.e. the i_th row of the j_th entry of the converted
# TensorArray corresponds to the j_th entry of the TensorArray in the i_th
# pfor iteration.
#
# 2b Elements written to the array are "unstacked"
# In this case we don't increase the dimensions to avoid redundant tiling. Each
# iteration is trying to write the same value. So we convert that to a single
# write.
#
# Here are some tricks used to implement the above:
# - TensorArrayV3 constructor encodes the element shape as an attr. Instead of
# trying to trace whether future writes are stacked or unstacked in order to set
# this attr, we set it to correspond to unknown shape.
# - We use the "flow" output of the different ops to track whether the array
# elements are stacked or unstacked. If a stacked write/scatter is done, we make
# the flow stacked as well.
# - We use some heuristic traversal of the graph to track whether the
# TensorArray handle was created inside or outside the pfor loop.


@RegisterPFor("TensorArrayV3")
def _convert_tensor_array_v3(pfor_input):
```
### Line 2953-2970
```
  identical_element_shapes = pfor_input.get_attr("identical_element_shapes")
  tensor_array_name = pfor_input.get_attr("tensor_array_name")
  handle, flow = data_flow_ops.tensor_array_v3(
      size,
      dtype=dtype,
      # We don't set element shape since we don't know if writes are stacked or
      # not yet.
      element_shape=None,
      dynamic_size=dynamic_size,
      clear_after_read=clear_after_read,
      identical_element_shapes=identical_element_shapes,
      tensor_array_name=tensor_array_name)
  # Note we keep flow unstacked for now since we don't know if writes will be
  # stacked or not.
  return wrap(handle, False), wrap(flow, False)


@RegisterPFor("TensorArraySizeV3")
```
### Line 2977-2990
```
  return wrap(size, False)


def _handle_inside_pfor(pfor_input, handle):
  """Returns True if handle was created inside the pfor loop."""
  # We use some heuristic to find the original TensorArray creation op.
  # The logic should handle the common cases (except cond based subgraphs).
  # In theory the user could perform different operations on the handle (like
  # Reshape, stack multiple handles, etc) which could break this logic.
  # TODO(agarwal): handle Switch/Merge.
  while handle.op.type in ("Enter", "Identity"):
    handle = handle.op.inputs[0]
  if handle.op.type not in [
      "TensorArrayV3", "TensorArrayGradV3", "TensorArrayGradWithShape"
```
### Line 2993-3003
```
  else:
    return pfor_input.pfor.op_is_inside_loop(handle.op)


def _unstack_flow(value):
  # TODO(agarwal): consider looking if this is a Tile op then get its input.
  # This may avoid running the Tile operations.
  return array_ops.gather(value, 0)


@RegisterPFor("TensorArrayReadV3")
```
### Line 3009-3029
```
  if flow_stacked:
    flow = _unstack_flow(flow)

  is_inside_pfor = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
  if is_inside_pfor:
    # Note that if we are inside a control flow construct inside the pfor, and
    # only some of the iterations are doing the read (i.e.
    # `all_indices_partitioned` is True), then the read operation should only
    # return values for the currently active pfor iterations (`all_indices`
    # below). Hence, whenever the returned value is stacked (i.e. `flow` is
    # stacked), we may need to do an extra gather after reading the values. Also
    # note that if `is_inside` is false, then values in the tensor array are
    # unstacked. So the check is only needed in this branch.
    all_indices = pfor_input.pfor.all_indices
    all_indices_partitioned = pfor_input.pfor.all_indices_partitioned
    # Note: flow_stacked indicates if values in the TensorArray are stacked or
    # not.
    if index_stacked:
      if flow_stacked:
        raise ValueError(
            "It looks like TensorArrayReadV3 was called on a TensorArray whose"
```
### Line 3034-3045
```
      return wrap(value, True)
    value = data_flow_ops.tensor_array_read_v3(handle, index, flow, dtype=dtype)
    if flow_stacked and all_indices_partitioned:
      value = array_ops.gather(value, all_indices)
    return wrap(value, flow_stacked)
  # Values in the TensorArray should be unstacked (since different iterations
  # couldn't write to the same location). So whether output is stacked or not
  # depends on index_stacked.
  if index_stacked:
    value = data_flow_ops.tensor_array_gather_v3(
        handle, index, flow, dtype=dtype)
  else:
```
### Line 3052-3063
```
  handle = pfor_input.unstacked_input(0)
  index, index_stacked, _ = pfor_input.input(1)
  value, value_stacked, _ = pfor_input.input(2)
  flow, flow_stacked, _ = pfor_input.input(3)
  if value_stacked and pfor_input.pfor.all_indices_partitioned:
    # Looks like we are in a control flow in a pfor where not all iterations are
    # active now. We don't allow that since that could lead to different indices
    # having different shapes which will be hard to merge later.
    raise ValueError("Writing non loop invariant values to TensorArray from "
                     "inside a while_loop/cond not supported.")
  if flow_stacked:
    flow = _unstack_flow(flow)
```
### Line 3069-3102
```
      flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)
      return wrap(flow_out, False)
    else:
      if not value_stacked:
        value = _stack(value, pfor_input.pfor.loop_len_vector).t
      # TODO(agarwal): Note that if flow is unstacked and value is stacked, then
      # this may or may not be a safe situation. flow is unstacked both for a
      # freshly created TensorArray, as well as after unstacked values are
      # written to it. If it is the latter, then we cannot write a stacked value
      # now since that may cause runtime errors due to different shapes in the
      # array. At the moment we are not able to handle this gracefully and
      # distinguish between the two cases. That would require some heuristic
      # traversal of the graph to figure out whether all the writes are
      # unstacked or not.
      flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)
      return _stack(flow_out, pfor_input.pfor.loop_len_vector)
  else:
    if not index_stacked:
      raise ValueError("Need indices for %s to be not loop invariant" % handle)
    # Note that even when index_stacked is true, actual values in index may
    # still not be unique. However that will cause runtime error when executing
    # the scatter operation below.
    if not value_stacked:
      value = _stack(value, pfor_input.pfor.loop_len_vector).t
    flow_out = data_flow_ops.tensor_array_scatter_v3(handle, index, value, flow)
    return _stack(flow_out, pfor_input.pfor.loop_len_vector)


def _transpose_first_two_dims(value):
  # TODO(agarwal): optimize if one of the dims == 1.
  value_shape = array_ops.shape(value)
  v0 = value_shape[0]
  v1 = value_shape[1]
  value = array_ops.reshape(value, [v0, v1, -1])
```
### Line 3112-3128
```
  indices = array_ops.reshape(indices, [-1])
  flow, flow_stacked, _ = pfor_input.input(2)
  if flow_stacked:
    flow = _unstack_flow(flow)
  dtype = pfor_input.get_attr("dtype")
  # TODO(agarwal): support element_shape attr?

  n = pfor_input.pfor.loop_len_vector
  value = data_flow_ops.tensor_array_gather_v3(
      handle, indices, flow, dtype=dtype)
  is_inside = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
  if is_inside:
    # flow_stacked indicates if values in the TensorArray are stacked or not.
    if indices_stacked:
      if flow_stacked:
        raise ValueError(
            "It looks like TensorArrayGatherV3 was called on a TensorArray "
```
### Line 3131-3148
```
      else:
        value = _unflatten_first_dim(value, n)
        return wrap(value, True)
    else:
      if flow_stacked:
        # Since elements in this array are stacked and `value` was produced by
        # gather, its first two dims are "gathered elements" and "stack
        # dimension". Our semantics require these two to be flipped.
        value = _transpose_first_two_dims(value)
      return wrap(value, flow_stacked)
  else:
    # Values in the TensorArray should be unstacked (since different iterations
    # couldn't write to the same location). So whether output is stacked or not
    # depends on indices_stacked.
    if indices_stacked:
      value = _unflatten_first_dim(value, n)
    return wrap(value, indices_stacked)

```
### Line 3160-3184
```

  is_inside = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
  if is_inside:
    if indices_stacked:
      raise ValueError("Need indices for %s to be loop invariant" % handle)
    # Note that flow_stacked indicates if existing values in the array are
    # stacked or not.
    if not flow_stacked and not value_stacked:
      flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                       flow)
      return wrap(flow_out, False)
    if not value_stacked:
      # TODO(agarwal): tile in the second dimension directly instead of
      # transposing below.
      value = _stack(value, pfor_input.pfor.loop_len_vector).t

    value = _transpose_first_two_dims(value)
    # TODO(agarwal): Note that if a previous write was unstacked, flow will be
    # unstacked, and a stacked value may be written here which may cause
    # runtime error due to different elements having different shape. We do
    # not try to prevent that.
    flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                     flow)
    return _stack(flow_out, pfor_input.pfor.loop_len_vector)
  if not indices_stacked:
```
### Line 3195-3209
```
  handle = pfor_input.unstacked_input(0)
  flow, flow_stacked, _ = pfor_input.input(1)
  if flow_stacked:
    flow = _unstack_flow(flow)
  source = pfor_input.get_attr("source")
  # TODO(agarwal): For now, we assume that gradients are stacked if the
  # TensorArrayGradV3 call is being done inside the pfor. Getting that wrong
  # will give runtime error due to incorrect shape being written to the
  # accumulator. It is difficult to know in advance if gradients written will be
  # stacked or not. Note that flow being stacked is not indicative of the
  # gradient being stacked or not. Revisit this later.
  shape_to_prepend = pfor_input.pfor.loop_len_vector
  grad_handle, flow_out = data_flow_ops.tensor_array_grad_with_shape(
      handle=handle,
      flow_in=flow,
```
### Line 3211-3253
```
      source=source)
  flow_out = _stack(flow_out, pfor_input.pfor.loop_len_vector).t
  return [wrap(grad_handle, False), wrap(flow_out, True)]


# StackV2 conversion is tricky since we don't have arrays of StackV2. So similar
# to TensorArrays, we convert them by changing the dimension of the elements
# inside the stack.
#
# We consider two cases:
#
# 1. StackV2 is constructed and used entirely inside the pfor loop.
# We keep a single Stack and perform the push/pop operations of all the
# iterations in lock-step. We also assume that all the iterations perform these
# operations. In case of dynamic control flow, if only some of the iterations
# try to perform a push/pop, then the conversion may not work correctly and may
# cause undefined behavior.
# TODO(agarwal): test StackV2 with dynamic control flow.
#
# 2. StackV2 is constructed outside the pfor loop.
# Performing stack push/pop in a parallel fashion is ill-defined. However given
# that reading stacks created externally is a common operation when computing
# jacobians, we provide some special semantics here as follows.
#  - disallow push operations to the stack
#  - pop operations are performed in lock step by all iterations, similar to the
#  case when the stack is created inside. A single value is popped during the
#  lock-step operation and broadcast to all the iterations. Values in the stack
#  are assumed to be loop-invariant.
#
# Some other implementation details:
# We use an ugly logic to find whether values in Stack data structure are
# loop invariant or not. When converting push/pop operations, we keep track of
# whether the last conversion used a stacked value or not (see _stack_cache
# below). As a result if an unstacked value is written first, subsequent stacked
# writes are disallowed when they could have been allowed in theory.

# Map from cache key based on StackV2 handle to a bool indicating whether values
# are stacked or not.
# TODO(agarwal): move _stack_cache inside pfor?
_stack_cache = {}


def _stack_cache_key(pfor_input):
```
### Line 3281-3290
```
  stacked = _stack_cache.get(stack_cache_key, None)
  if stacked is None:
    stacked = elem_stacked
    _stack_cache[stack_cache_key] = stacked
  else:
    # If we previously made it unstacked then we can't revert to being stacked.
    if not stacked and elem_stacked:
      raise ValueError(
          "It looks like the stack was previously determined to be loop"
          " invariant, but we are now trying to push a loop dependent value"
```
### Line 3293-3320
```
      elem = _stack(elem, pfor_input.pfor.loop_len_vector).t
  out = data_flow_ops.stack_push_v2(handle, elem, swap_memory=swap_memory)
  return wrap(out, stacked)


# Note that inputs to this convertor will be unstacked. However it should get
# called since it is a stateful op.
@RegisterPFor("StackPopV2")
def _convert_stack_pop_v2(pfor_input):
  handle = pfor_input.unstacked_input(0)
  stack_cache_key = _stack_cache_key(pfor_input)
  stacked = _stack_cache.get(stack_cache_key, None)
  # If a StackPushV2 has not been converted yet, we default to unstacked since
  # the push could be outside of pfor, or the covertor may not be called if the
  # inputs are unconverted.
  if stacked is None:
    stacked = False
    _stack_cache[stack_cache_key] = False
  elem_type = pfor_input.get_attr("elem_type")
  out = data_flow_ops.stack_pop_v2(handle, elem_type)
  return wrap(out, stacked)


# parsing_ops


@RegisterPFor("DecodeCSV")
def _convert_decode_csv(pfor_input):
```
### Line 3388-3397
```
      ragged_split_types=ragged_split_types,
      dense_shapes=dense_shapes)
  return [wrap(t, True, True) for t in nest.flatten(output)]


# functional_ops


@RegisterPFor("StatefulPartitionedCall")
@RegisterPFor("PartitionedCall")
```
### Line 3407-3424
```
      pfor_ops=func.graph.get_operations(),
      all_indices=pfor.all_indices,
      all_indices_partitioned=pfor.all_indices_partitioned,
      pfor_config=pfor.pfor_config)

  # TODO(agarwal): consider caching this function definition.
  @def_function.function
  def f(*args):
    assert all(isinstance(arg, WrappedTensor) for arg in args), args
    assert len(args) == len(func.graph.inputs), (args, func.graph.inputs)
    #  Map inputs to function arguments.
    for inp, arg in zip(func.graph.inputs, args):
      converter._add_conversion(inp, arg)
    # Convert output tensors.
    return tuple(
        [converter._convert_helper(x).t for x in func._func_graph_outputs])

  call_outputs = f(*pfor_input.inputs)
```

## _tensorflow_tools_ci_build_builds_cmake_sh
### Line 1-27
```
#!/usr/bin/env bash
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

set -e


# Determine the number of cores, for parallel make.
N_JOBS=$(grep -c ^processor /proc/cpuinfo)
if [[ -z ${N_JOBS} ]]; then
  # The Linux way didn't work. Try the Mac way.
  N_JOBS=$(sysctl -n hw.ncpu)
fi
if [[ -z ${N_JOBS} ]]; then
  N_JOBS=1
```
### Line 33-44
```
echo ""
echo "make will use ${N_JOBS} concurrent job(s)."
echo ""


# Run TensorFlow cmake build.
# Clean up, because certain modules, e.g., highwayhash, seem to be sensitive
# to state.
rm -rf build

mkdir -p build
pushd build
```

## _tensorflow_python_ops_matmul_benchmark_test_py
### Line 1-18
```
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for matmul_benchmark.py."""

from __future__ import absolute_import
from __future__ import division
```

## _tensorflow_tools_dockerfiles_tests_build_cpu_sh
### Line 1-33
```
```

## _tensorflow_python_keras_distribute_distributed_training_utils_test_py
### Line 1-18
```
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for distributed training utility functions."""

from __future__ import absolute_import
from __future__ import division
```

## _tensorflow_python_profiler_internal_flops_registry_py
### Line 1-18
```
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Register flops statistics for various TensorFlow operations.
"""
from __future__ import absolute_import
from __future__ import division
```
### Line 20-45
```

from tensorflow.python.framework import graph_util
from tensorflow.python.framework import ops


# List of all ops which have implemented flops statistics.
IMPLEMENTED_OPS = set([
    # Unary ops
    "Reciprocal", "Square", "Rsqrt", "Log", "Neg", "AssignSub", "AssignAdd",
    "L2Loss", "Softmax",
    # Binary ops
    "Add", "Sub", "Mul", "RealDiv", "Maximum", "Minimum", "Pow", "RsqrtGrad",
    "GreaterEqual", "Greater", "LessEqual", "Less", "Equal", "NotEqual",
    "SquaredDifference",
    # Reduction ops
    "Mean", "Sum", "ArgMax", "ArgMin", "BiasAddGrad",
    # Convolution and pooling
    "AvgPool", "MaxPool", "AvgPoolGrad", "MaxPoolGrad", "Conv2DBackpropInput",
    "Conv2DBackpropFilter",
    # Other ops
    "AddN",
    # Ops implemented in core tensorflow:
    "MatMul", "Conv2D", "DepthwiseConv2dNative", "BiasAdd", "Dilation2D",
])


```
### Line 54-65
```
  result = 1
  for item in lst:
    result *= item
  return result

################################################################################
# Unary operations
################################################################################


def _unary_op_flops(graph, node, ops_per_element=1):
  """Common code which compute flops for unary operations."""
```
### Line 81-90
```


@ops.RegisterStatistics("Rsqrt", "flops")
def _rsqrt_flops(graph, node):
  """Compute flops for Rsqrt operation."""
  # Rsqrt(x) = 1 / sqrt(x)
  return _unary_op_flops(graph, node, ops_per_element=2)


@ops.RegisterStatistics("Log", "flops")
```
### Line 114-141
```
@ops.RegisterStatistics("L2Loss", "flops")
def _l2_loss_flops(graph, node):
  """Compute flops for L2Loss operation."""
  in_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
  in_shape.assert_is_fully_defined()
  # Tensorflow uses inefficient implementation, with (3*N-1) flops:
  # Optimal implementation is 2*N flops
  return ops.OpStats("flops", in_shape.num_elements() * 3 - 1)


@ops.RegisterStatistics("Softmax", "flops")
def _softmax_flops(graph, node):
  """Compute flops for Softmax operation."""
  # Softmax implenetation:
  #
  # Approximate flops breakdown:
  #   2*n          -- compute shifted logits
  #   n            -- exp of shifted logits
  #   2*n          -- compute softmax from exp of shifted logits
  return _unary_op_flops(graph, node, ops_per_element=5)

################################################################################
# Binary operations
################################################################################


def _binary_per_element_op_flops(graph, node, ops_per_element=1):
  """Common code which compute flops for binary operations."""
```
### Line 231-242
```
@ops.RegisterStatistics("SquaredDifference", "flops")
def _squared_difference_flops(graph, node):
  """Compute flops for SquaredDifference operation."""
  return _binary_per_element_op_flops(graph, node, ops_per_element=2)

################################################################################
# Reduction ops
################################################################################


def _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0):
  """Common code which compute flops for reduction operations."""
```
### Line 250-320
```


@ops.RegisterStatistics("Mean", "flops")
def _mean_flops(graph, node):
  """Compute flops for Mean operation."""
  # reduction - sum, finalization - divide
  return _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=1)


@ops.RegisterStatistics("Sum", "flops")
def _sum_flops(graph, node):
  """Compute flops for Sum operation."""
  # reduction - sum, no finalization
  return _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0)


@ops.RegisterStatistics("ArgMax", "flops")
def _arg_max_flops(graph, node):
  """Compute flops for ArgMax operation."""
  # reduction - comparison, no finalization
  return _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0)


@ops.RegisterStatistics("ArgMin", "flops")
def _arg_min_flops(graph, node):
  """Compute flops for ArgMin operation."""
  # reduction - comparison, no finalization
  return _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0)


@ops.RegisterStatistics("BiasAddGrad", "flops")
def _bias_add_grad_flops(graph, node):
  """Compute flops for BiasAddGrad operation."""
  # Implementation of BiasAddGrad, essentially it's a reduce sum and reshaping:
  # So computing flops same way as for "Sum"
  return _reduction_op_flops(graph, node, reduce_flops=1, finalize_flops=0)

################################################################################
# Convolution and pooling
# Note: all flops statistics are implemented only for NHWC data format
################################################################################


def _verify_conv_data_format(node):
  """Verifies data format for pooling and convolutional operations."""
  # TODO(xpan): P1: Support NCHW
  if node.attr["data_format"].s != b"NHWC":
    raise ValueError("Only NHWC format is supported in flops computations")


def _pool_flops(graph, node):
  """Common code which compute flops for pooling operations."""
  # compute flops for average and max pooling
  _verify_conv_data_format(node)
  #
  # Pooling declaration:
  #   Inputs:
  #     - value
  #   Outputs:
  #     - output
  #   Attributes:
  #     - ksize
  #     - strides
  #     - padding
  #     - data_format
  #
  # Pooling implenetation:
  out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
  out_shape.assert_is_fully_defined()
  kernel_shape = list(node.attr["ksize"].list.i)
  kernel_area = _list_product(kernel_shape)
```
### Line 335-375
```

@ops.RegisterStatistics("AvgPoolGrad", "flops")
def _avg_pool_grad_flops(graph, node):
  """Compute flops for AvgPoolGrad operation."""
  _verify_conv_data_format(node)
  # Pooling gradient implementation:
  out_backprop_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                                  node.input[1])
  out_backprop_shape.assert_is_fully_defined()
  kernel_shape = list(node.attr["ksize"].list.i)
  kernel_area = _list_product(kernel_shape)
  # TensorFlow multiply each element of pooling window by coefficient,
  # then sum up all of them, thus we have 2 flops per element:
  # More optimal implementation - if division is done after.
  return ops.OpStats("flops",
                     kernel_area * out_backprop_shape.num_elements() * 2)


@ops.RegisterStatistics("MaxPoolGrad", "flops")
def _max_pool_grad_flops(graph, node):
  """Compute flops for MaxPoolGrad operation."""
  _verify_conv_data_format(node)
  #
  # MaxPoolGrad declaration:
  #   Inputs:
  #     - orig_input  -- original input tensor (of max_pool)
  #     - orig_output  -- original output tensor (of max_pool)
  #     - grad --  gradient with respect to output of max_pool
  #   Outputs:
  #     - output -- gradient with respect to input of max_pool
  #   Attributes:
  #     - ksize
  #     - strides
  #     - padding
  #     - data_format
  # It computes MaxPool first, then one flop per each element of original output
  #
  kernel_shape = list(node.attr["ksize"].list.i)
  kernel_area = _list_product(kernel_shape)
  orig_out_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                              node.input[1])
```
### Line 379-408
```


@ops.RegisterStatistics("Conv2DBackpropInput", "flops")
def _conv_2d_backprop_input_flops(graph, node):
  """Compute flops for Conv2DBackpropInput operation."""
  # Formula:
  #  batch_size * image_x_dim * image_y_dim * kernel_x_dim * kernel_y_dim
  #  * input_depth * output_depth * 2 / (image_x_stride * image_x_stride)
  #
  # Where:
  # image_x_dim, image_y_dim and input_depth --- size of input to source (no
  #   backprop) convolution, in other words they are sizes of backprop output.
  # output_depth --- number of filters in the original convolution, thus
  #   depth of backprop input.
  # kernel_x_dim and kernel_y_dim --- sizes of filter in spatial dimension
  # image_x_stride and image_x_stride --- strides of the convolution
  #
  _verify_conv_data_format(node)
  # out_shape = [batch_size, image_y_dim, image_x_dim, input_depth]
  out_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
  out_shape.assert_is_fully_defined()
  # kernel_shape = [kernel_y_dim, kernel_x_dim, input_depth, output_depth]
  kernel_shape = graph_util.tensor_shape_from_node_def_name(graph,
                                                            node.input[1])
  kernel_shape.assert_is_fully_defined()
  # strides
  strides_shape = list(node.attr["strides"].list.i)
  strides_product = strides_shape[1] * strides_shape[2]
  return ops.OpStats("flops",
                     (2 * out_shape.num_elements()
```
### Line 411-441
```


@ops.RegisterStatistics("Conv2DBackpropFilter", "flops")
def _conv_2d_backprop_filter_flops(graph, node):
  """Compute flops for Conv2DBackpropFilter operation."""
  # Formula same as for Conv2DBackpropInput:
  #  batch_size * image_x_dim * image_y_dim * kernel_x_dim * kernel_y_dim
  #  * input_depth * output_depth * 2 / (image_x_stride * image_x_stride)
  #
  _verify_conv_data_format(node)
  # image_shape = [batch_size, image_y_dim, image_x_dim, input_depth]
  image_shape = graph_util.tensor_shape_from_node_def_name(graph, node.input[0])
  image_shape.assert_is_fully_defined()
  # kernel_shape = [kernel_y_dim, kernel_x_dim, input_depth, output_depth]
  kernel_shape = graph_util.tensor_shape_from_node_def_name(graph, node.name)
  kernel_shape.assert_is_fully_defined()
  # strides
  strides_shape = list(node.attr["strides"].list.i)
  strides_product = strides_shape[1] * strides_shape[2]
  return ops.OpStats("flops",
                     (2 * image_shape.num_elements()
                      * kernel_shape.num_elements()
                      / (image_shape.dims[-1].value * strides_product)))

################################################################################
# Other ops
################################################################################


@ops.RegisterStatistics("AddN", "flops")
def _add_n_flops(graph, node):
```

## _tensorflow_python_keras_saving_saved_model_save_impl_py
### Line 1-18
```
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Keras SavedModel serialization.

TODO (kathywu): Move to layer_serialization.py. Some model-specific logic should
go to model_serialization.py.
```
### Line 43-57
```
from tensorflow.python.util import nest
from tensorflow.python.util import tf_decorator
from tensorflow.python.util import tf_inspect
from tensorflow.python.util.lazy_loader import LazyLoader

# To avoid circular dependencies between keras/engine and keras/saving,
# code in keras/saving must delay imports.

# TODO(b/134426265): Switch back to single-quotes to match the rest of the file
# once the issue with copybara is fixed.
# pylint:disable=g-inconsistent-quotes
base_layer = LazyLoader(
    "base_layer", globals(),
    "tensorflow.python.keras.engine.base_layer")
input_layer = LazyLoader(
```
### Line 61-85
```
    "training_lib", globals(),
    "tensorflow.python.keras.engine.training")
sequential_lib = LazyLoader(
    "sequential_lib", globals(),
    "tensorflow.python.keras.engine.sequential")
# pylint:enable=g-inconsistent-quotes


def should_skip_serialization(layer):
  """Skip serializing extra objects and functions if layer inputs aren't set."""
  if isinstance(layer, training_lib.Model):
    try:
      # pylint:disable=pointless-statement
      layer.inputs
      layer.input_names
      # pylint:enable=pointless-statement
    except AttributeError:
      # If the model does not have inputs set, because it was not called or its
      # input shapes were not recorded, we won't have a signature so can't trace
      # a function. But the user may still save an object with this Model
      # attached; we won't fail the whole tf.saved_model.save.
      logging.warning('Skipping full serialization of Keras model {}, because '
                      'its inputs are not defined.'.format(layer))
      return True
    else:
```
### Line 103-119
```
  Returns:
    A dictionary containing all checkpointable objects from a
    SerializedAttributes object. See LayerAttributes and ModelAttributes for
    entire list of objects
  """
  # Wrap all regularization losses as tf.functions.
  # First, generate list of all regularization losses in this layer and
  # sublayers.
  all_losses = layer._callable_losses[:]  # pylint: disable=protected-access
  for child_layer in _list_all_layers(layer):
    all_losses.extend(child_layer._callable_losses)  # pylint: disable=protected-access
  # Next, wrap all loss functions as tf.functions. Use the serialization cache
  # to store already-wrapped functions.
  keras_loss_cache = serialization_cache.setdefault('keras_losses', {})
  wrapped_loss_functions = []
  for loss_fn in all_losses:
    if loss_fn in keras_loss_cache:
```
### Line 148-172
```

  Returns:
    A dictionary containing all keras tf.functions to serialize. See
    LayerAttributes and ModelAttributes for the list of all attributes.
  """
  # Since Sequential models may be modified in place using model.add() or
  # model.pop(), don't use saved functions.
  if (isinstance(layer, keras_load.RevivedLayer) and
      not isinstance(layer, sequential_lib.Sequential)):
    return {fn_name: getattr(layer.keras_api, fn_name, None)
            for fn_name in serialized_attributes.LayerAttributes.all_functions}

  # Reset the losses of the layer and its children. The call function in each
  # child layer is replaced with tf.functions.
  original_fns = _replace_child_layer_functions(layer, serialization_cache)
  original_losses = _reset_layer_losses(layer)

  # Wrap all the layer call and activity regularizer functions.

  # Use LayerCallCollection to ensure that all layer call functions (__call__,
  # call with losses) are traced with the same inputs.
  call_collection = LayerCallCollection(layer)
  call_fn_with_losses = call_collection.add_function(
      _wrap_call_and_conditional_losses(layer),
      '{}_layer_call_and_return_conditional_losses'.format(layer.name))
```
### Line 188-206
```
            ))
  else:
    fns['activity_regularizer_fn'] = None
    fns['call_and_return_all_conditional_losses'] = call_fn_with_losses

  # Manually trigger traces before restoring the overwritten functions. The
  # functions are traced within the layer call context to ensure that layer
  # functions (e.g. add_loss) behave as though running in graph mode.
  with base_layer_utils.call_context().enter(
      layer, inputs=None, build_graph=True, training=None, saving=True):
    for fn in fns.values():
      if fn is not None and fn.input_signature is not None:
        fn.get_concrete_function()

  # Restore overwritten functions and losses
  _restore_child_layer_functions(original_fns)
  _restore_layer_losses(original_losses)

  return fns
```
### Line 244-253
```
          'call': Original call function
          'activity_regularizer': Original activity regularizer},
        Child layer 2: ...
      }
  """
  # pylint: disable=protected-access
  original_fns = {}
  for child_layer in _list_all_layers(layer):
    if isinstance(child_layer, input_layer.InputLayer):
      continue
```
### Line 258-272
```
              serialization_cache).functions)
    else:
      layer_fns = (
          serialization_cache[constants.KERAS_CACHE_KEY][child_layer].functions)
    if not layer_fns:
      # This indicates either:
      #   - circular dependency, which means the current layer's functions
      #     should be wrapped first.
      #   - Child layer's inputs are not defined, so its functions have not been
      #     wrapped. In this case, no replacement is necessary so move on to the
      #     next child.
      continue
    original_fns[child_layer] = {
        'call': child_layer.call,
        'activity_regularizer': child_layer.activity_regularizer
```
### Line 274-289
```
    with trackable.no_automatic_dependency_tracking_scope(child_layer):
      try:
        child_layer.activity_regularizer = layer_fns.get(
            'activity_regularizer_fn')
      except AttributeError:
        # Some layers have an unsettable activity regularizer.
        pass
      child_layer.call = utils.use_wrapped_call(
          child_layer, layer_fns['call_and_return_conditional_losses'],
          default_training_value=False)
  return original_fns
  # pylint: enable=protected-access


def _restore_child_layer_functions(original_fns):
  """Restores attributes replaced with `_replace_child_layer_functions`."""
```
### Line 294-303
```
        child_layer.activity_regularizer = fns['activity_regularizer']
      except AttributeError:
        pass


# pylint: disable=protected-access
def _reset_layer_losses(parent_layer):
  """Resets losses of layer and its sublayers, and returns original losses."""
  losses_dict = {}
  for layer in _list_all_layers(parent_layer) + [parent_layer]:
```
### Line 312-321
```
def _restore_layer_losses(losses_dict):
  for layer in losses_dict:
    with trackable.no_automatic_dependency_tracking_scope(layer):
      layer._losses = losses_dict[layer]['losses']
      layer._eager_losses = losses_dict[layer]['eager_losses']
# pylint: enable=protected-access


def layer_uses_training_bool(layer):
  """Returns whether this layer or any of its children uses the training arg."""
```
### Line 350-373
```
    self.layer_call_method = _get_layer_call_method(layer)
    self._expects_training_arg = layer_uses_training_bool(layer)
    self._training_arg_index = utils.get_training_arg_index(
        self.layer_call_method)

    # If the layer call function has kwargs, then the traced function cannot
    # have an input signature.
    arg_spec = tf_inspect.getfullargspec(self.layer_call_method)
    self._has_kwargs = bool(self._expects_training_arg or
                            arg_spec.defaults or
                            arg_spec.kwonlyargs or
                            arg_spec.varkw)

    self._input_signature = self._generate_input_signature(layer)
    self._functions = weakref.WeakValueDictionary()
    # Bool indicating whether this object is currently tracing the layer call
    # functions.
    self.tracing = False

    # Get the input argument name from the args.
    args = arg_spec.args
    if tf_inspect.ismethod(self.layer_call_method):
      args = args[1:]
    self._input_arg_name = args[0] if args else 'inputs'
```
### Line 390-402
```
        return saving_utils.model_input_signature(layer)
      elif layer.input_spec is not None:

        def to_tensor_spec_or_none(x):
          spec = input_spec.to_tensor_spec(x, layer.dtype)
          # If the shape is too general (e.g. multiple dimensions are allowed),
          # return None so that separate functions can be generated for each
          # inferred input signature.
          # TODO(b/134962016): currently partial signatures are not supported.
          if spec.shape == tensor_shape.TensorShape(None):
            return None
          return spec
        input_signature = [nest.map_structure(
```
### Line 415-425
```
    """
    args = list(args)
    kwargs = kwargs.copy()
    self.tracing = True
    for fn in self._functions.values():
      # TODO(kathywu): Replace arguments with broader shapes defined in the
      # input signature.
      if self._expects_training_arg:
        def trace_with_training(value, fn=fn):
          utils.set_training_arg(value, self._training_arg_index, args, kwargs)
          with K.learning_phase_scope(value):
```
### Line 433-446
```

  @property
  def fn_input_signature(self):
    """Returns input signature for the wrapped layer call function."""
    if self._has_kwargs:
      # Input signatures may only describe tensor arguments and kwargs are not
      # supported.
      return None
    if None in nest.flatten(self._input_signature):
      # TODO(b/134962016): If input signature cannot be partially defined.
      return None
    return self._input_signature

  def training_arg_was_passed(self, args, kwargs):
```
### Line 463-472
```
        self._input_arg_name, args, kwargs, inputs_in_args=True)

  def _maybe_wrap_with_training_arg(self, call_fn):
    """Wraps call function with added training argument if necessary."""
    if not self.layer._expects_training_arg and self._expects_training_arg:  # pylint: disable=protected-access
      # Add training arg to wrapper function.
      arg_spec = tf_inspect.getfullargspec(call_fn)
      args = arg_spec.args + ['training']
      defaults = list(arg_spec.defaults or [])
      defaults.append(False)
```
### Line 477-494
```
          defaults=defaults,
          kwonlyargs=arg_spec.kwonlyargs,
          kwonlydefaults=arg_spec.kwonlydefaults,
          annotations=arg_spec.annotations)

      # Set new training arg index
      self._training_arg_index = len(args) - 1
      if tf_inspect.ismethod(call_fn):
        self._training_arg_index -= 1

      def wrap_with_training_arg(*args, **kwargs):
        # Remove the training value, since the original call_fn does not expect
        # a training arg. Instead, the training value will be propagated using
        # the call context created in LayerCall.
        args = list(args)
        kwargs = kwargs.copy()
        utils.remove_training_arg(self._training_arg_index, args, kwargs)
        return call_fn(*args, **kwargs)
```
### Line 506-516
```
        self, self._maybe_wrap_with_training_arg(call_fn), name,
        input_signature=self.fn_input_signature)

    if (None not in nest.flatten(self._input_signature) and
        self._has_kwargs):
      # Manually add traces for layers that have keyword arguments and have
      # a fully defined input signature.
      self.add_trace(*self._input_signature)
    return fn


```
### Line 519-532
```
  def wrapper(*args, **kwargs):
    """Calls method within call context."""
    layer = call_collection.layer
    training = None
    inputs = call_collection.get_input_arg_value(args, kwargs)
    # pylint: disable=protected-access
    if (args or kwargs) and call_collection.training_arg_was_passed(
        args, kwargs):
      training = call_collection.get_training_arg_value(args, kwargs)
    # pylint: enable=protected-access
    original_losses = _reset_layer_losses(layer)
    with base_layer_utils.call_context().enter(
        layer, inputs=inputs, build_graph=False, training=training,
        saving=True):
```
### Line 568-577
```

  Returns:
    python call function that returns outputs and conditional losses -- excludes
    activity regularizer
  """
  # Create function that generates both outputs and losses
  layer_call = _get_layer_call_method(layer)
  def call_and_return_conditional_losses(inputs, *args, **kwargs):
    return layer_call(inputs, *args, **kwargs), layer.get_losses_for(inputs)
  return _create_call_fn_decorator(layer, call_and_return_conditional_losses)
```
### Line 607-616
```
      decorator_argspec=arg_spec)


def _wrap_unconditional_loss(loss_fn, index):
  """Wraps callable/unconditonal loss, returning a serializable function."""
  # Extract original loss function from partial function
  fn = loss_fn.args[0] if isinstance(loss_fn, functools.partial) else loss_fn
  if isinstance(fn, def_function.Function):
    return fn
  else:
```

## _tensorflow_python_compiler_tensorrt_test_reshape_transpose_test_py
### Line 1-18
```
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Basic tests for TF-TensorRT integration."""

from __future__ import absolute_import
from __future__ import division
```
### Line 27-48
```

class ReshapeTest(trt_test.TfTrtIntegrationTestBase):

  def GraphFn(self, inp):
    outputs = []
    # Here we test two types of reshapes, one changes the batch dimension and
    # the other does not. Note that we're not able to test reshaping to
    # scalar, since TRT requires input tensor to be of rank at least 2, so a
    # reshape with scalar input will be filtered out of the segment before
    # conversion.
    #
    # These reshapes happen at batch dimension, thus conversion should fail.
    for shape in [[2, 50, 24, 24, 2], [-1, 50, 24, 24, 2], [2, 50, -1, 24, 2]]:
      incompatible_reshape = array_ops.reshape(inp, shape)
      reshape_back = array_ops.reshape(incompatible_reshape, [-1, 24, 24, 2])
      outputs.append(self.trt_incompatible_op(reshape_back))
    # Add another block with many reshapes that don't change the batch
    # dimension.
    compatible_reshape = array_ops.reshape(
        inp, [-1, 24 * 24, 2], name="reshape-0")
    compatible_reshape = array_ops.reshape(
        compatible_reshape, [100, 24, -1], name="reshape-1")
```
### Line 77-86
```


class TransposeTest(trt_test.TfTrtIntegrationTestBase):

  def GraphFn(self, inp):
    # Add a block with compatible transposes.
    compatible_transpose = array_ops.transpose(
        inp, [0, 3, 1, 2], name="transpose-1")
    compatible_transpose = array_ops.transpose(
        compatible_transpose, [0, 2, 3, 1], name="transposeback")
```
### Line 106-115
```


class IncompatibleTransposeTest(TransposeTest):

  def GraphFn(self, inp):
    # Add a block with incompatible transposes.
    incompatible_transpose = array_ops.transpose(
        inp, [2, 1, 0, 3], name="transpose-2")
    excluded_transpose = array_ops.transpose(
        incompatible_transpose, [0, 2, 3, 1], name="transpose-3")
```

# Issues
## 20075
Title:
```

        error in running a LSTM programme
      
```
Author:
```
srinathdwivedi
```
Text:
```

i am writing a basic LSTM program for text generation. when i am writing line:
model.add(LSTM(256, input_shape=(x.shape[1], x.shape[2]), return_sequences=True))
following error occurring, may i know what is wrong with this:
python /home/srinath/char_gen.py
Using TensorFlow backend.
Total Characters 144413
Total Vocab 45
Total Patterns: 144313
Traceback (most recent call last):
File "/home/srinath/char_gen.py", line 63, in 
model.add(LSTM(256, input_shape=(x.shape[1], x.shape[2]), return_sequences=True))
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/engine/sequential.py", line 166, in add
layer(x)
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 500, in call
return super(RNN, self).call(inputs, **kwargs)
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/engine/base_layer.py", line 460, in call
output = self.call(inputs, **kwargs)
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 2112, in call
initial_state=initial_state)
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 609, in call
input_length=timesteps)
File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2957, in rnn
maximum_iterations=input_length)
TypeError: while_loop() got an unexpected keyword argument 'maximum_iterations'
ERROR:tensorflow:==================================
Object was never used (type <class 'tensorflow.python.ops.tensor_array_ops.TensorArray'>):
<tensorflow.python.ops.tensor_array_ops.TensorArray object at 0x7f75882d7da0>
If you want to mark it as used call its "mark_used()" method.
It was originally created here:
['File "/home/srinath/char_gen.py", line 63, in \n    model.add(LSTM(256, input_shape=(x.shape[1], x.shape[2]), return_sequences=True))', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/engine/sequential.py", line 166, in add\n    layer(x)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 500, in call\n    return super(RNN, self).call(inputs, **kwargs)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/engine/base_layer.py", line 460, in call\n    output = self.call(inputs, **kwargs)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 2112, in call\n    initial_state=initial_state)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/layers/recurrent.py", line 609, in call\n    input_length=timesteps)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2877, in rnn\n    input_ta = input_ta.unstack(inputs)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/tf_should_use.py", line 170, in wrapped\n    return _add_should_use_warning(fn(*args, **kwargs))', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/ops/tensor_array_ops.py", line 413, in unstack\n    indices=math_ops.range(0, num_elements), value=value, name=name)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/tf_should_use.py", line 170, in wrapped\n    return _add_should_use_warning(fn(*args, **kwargs))', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/tf_should_use.py", line 139, in _add_should_use_warning\n    wrapped = TFShouldUseWarningWrapper(x)', 'File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/tf_should_use.py", line 96, in init\n    stack = [s.strip() for s in traceback.format_stack()]']
please help me if possible.

```
Author:
```
tensorflowbutler
```
Text:
```

Thank you for your post. We noticed you have not filled out the following field in the issue template. Could you update them if they are relevant in your case, or leave them as N/A? Thanks.
Have I written custom code
OS Platform and Distribution
TensorFlow installed from
TensorFlow version
Bazel version
CUDA/cuDNN version
GPU model and memory
Exact command to reproduce

```
Author:
```
SidJain1412
```
Text:
```

Getting the same error. No idea why, please let me know if you find a solution

```
Author:
```
srinathdwivedi
```
Text:
```

Have I written custom code - i have written code as per the tutorial.
OS Platform and Distribution - Ubuntu -16.04
TensorFlow installed from - sources per tutorial.
TensorFlow version - 1.2 GPU
Bazel version - Not installed
CUDA/cuDNN version - 7.5
GPU model and memory - 16gb memory
Exact command to reproduce -  N/A
…
On Sun, Jun 17, 2018 at 6:17 AM, Alfred Sorten Wolf < ***@***.***> wrote:
 Thank you for your post. We noticed you have not filled out the following
 field in the issue template. Could you update them if they are relevant in
 your case, or leave them as N/A? Thanks.
 Have I written custom code
 OS Platform and Distribution
 TensorFlow installed from
 TensorFlow version
 Bazel version
 CUDA/cuDNN version
 GPU model and memory
 Exact command to reproduce

 —
 You are receiving this because you authored the thread.
 Reply to this email directly, view it on GitHub
 <#20075 (comment)>,
 or mute the thread
 <https://github.com/notifications/unsubscribe-auth/AXgS2sgOOJUTuozeMWM-2B-7Dli3xqT4ks5t9ac-gaJpZM4UqevE>
 .


-- 
Sri Nath Dwivedi
Asstt. Professor
(Computer Science & Engg.)
Dr. Ambedkar Institute of Technology for Handicapped, U.P. Kanpur


```
Author:
```
SidJain1412
```
Text:
```

Use tensorflow gpu 1.4.1 with keras 2.1.5, CUDA 8, CUDNN 7
If your GPU is not compatible with CUDA 8 just try using keras 2.1.5, it solved my problem!

```
Author:
```
srinathdwivedi
```
Text:
```

i don't have GPU but have a laptop with NVIDIA graphic card.
when i tried to upgrade tensorflow==1.4.1 from previous version 1.2.0 after that during running a programme following problem occurred:
python /home/srinath/practice_LSTM.py Traceback (most recent call last):
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in 
from tensorflow.python.pywrap_tensorflow_internal import *
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in 
_pywrap_tensorflow_internal = swig_import_helper()
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
_mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
File "/home/srinath/anaconda3/lib/python3.6/imp.py", line 242, in load_module
return load_dynamic(name, filename, file)
File "/home/srinath/anaconda3/lib/python3.6/imp.py", line 342, in load_dynamic
return _load(spec)
ImportError: libcudnn.so.6: cannot open shared object file: No such file or directory
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/home/srinath/practice_LSTM.py", line 3, in 
import tensorflow as tf
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/init.py", line 24, in 
from tensorflow.python import *
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/init.py", line 49, in 
from tensorflow.python import pywrap_tensorflow
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py", line 72, in 
raise ImportError(msg)
ImportError: Traceback (most recent call last):
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in 
from tensorflow.python.pywrap_tensorflow_internal import *
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in 
_pywrap_tensorflow_internal = swig_import_helper()
File "/home/srinath/anaconda3/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
_mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
File "/home/srinath/anaconda3/lib/python3.6/imp.py", line 242, in load_module
return load_dynamic(name, filename, file)
File "/home/srinath/anaconda3/lib/python3.6/imp.py", line 342, in load_dynamic
return _load(spec)
ImportError: libcudnn.so.6: cannot open shared object file: No such file or directory
Failed to load the native TensorFlow runtime.
See https://www.tensorflow.org/install/install_sources#common_installation_problems
for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.
srinath@srinath-HP-Pavilion-Notebook:~$ python /home/srinath/char_gen.py Traceback (most recent call last):

```
Author:
```
srinathdwivedi
```
Text:
```

in the mentioned site, i tried to understand the problem, but i am not getting what should i do. in that site following thing is relevant, so should i change all things means CUDA, CUDnn etc.



tensorflow_gpu-1.4.0
GPU
2.7, 3.3-3.6
GCC 4.8
Bazel 0.5.4
6
8




```
Author:
```
SidJain1412
```
Text:
```

Which nvidia graphics card do you have? A graphics card is a GPU.
You need to install tensorflow-gpu on your system to utilize it
According to your graphics card you must install a specific version of CUDA and CUDNN (cudnn version is wrong that's why the new error)

```
Author:
```
srinathdwivedi
```
Text:
```

i have installed tensorflow 1.2 and it is working well, CUDA8.0GA2 and CUDnn8.0
NVIDIA driver version: 384.130
NVIDIA server string:TheX.orgFoundation
NVIDIA serverversion:11.0

```
Author:
```
SidJain1412
```
Text:
```

It's working? Great

```
Author:
```
srinathdwivedi
```
Text:
```

now i installed following
tensorflow-gpu==1.4.0 /1.4.1
CUDA8.0
cuDNN6.08 because in cudann site there was no option of cuDNN7 with CUDA8.0, there were 2 options cuDNN5.1 with CUDA8 or 6 so i installed 6, then in running every programme following warning shows:
/home/snd/anaconda3/lib/python3.6/importlib/_bootstrap.py:205: RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.6
return f(*args, **kwds)
how to resolve this
this error does not appear in tensorflow-gpu==1.2

```
Author:
```
SidJain1412
```
Text:
```

Is this only a warning or an error? If it's a warning I think you could ignore it as you probably won't be using fast tensor utility

```
Author:
```
srinathdwivedi
```
Text:
```

okay thanks, it is only warning
thanks for support

```
Author:
```
SidJain1412
```
Text:
```

Happy to help!

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @shivaniag: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
srinathdwivedi
```
Text:
```

problem solved
…
On Mon, Jul 9, 2018 at 12:07 AM, Alfred Sorten Wolf < ***@***.***> wrote:
 Nagging Assignee @shivaniag <https://github.com/shivaniag>: It has been
 14 days with no activity and this issue has an assignee. Please update the
 label and/or status accordingly.

 —
 You are receiving this because you authored the thread.
 Reply to this email directly, view it on GitHub
 <#20075 (comment)>,
 or mute the thread
 <https://github.com/notifications/unsubscribe-auth/AXgS2h_KU87uv_D3ANqKflOl1Lc9VbwMks5uElFygaJpZM4UqevE>
 .


-- 
Sri Nath Dwivedi
Asstt. Professor
(Computer Science & Engg.)
Dr. Ambedkar Institute of Technology for Handicapped, U.P. Kanpur


```

## 2885
Title:
```

        Tensorflow import error despite correct installation
      
```
Author:
```
paul2254
```
Text:
```

Hi everyone!
Environment info
Operating System: Ubuntu 16.04 LTS
Graphics card: GTX 1080 Founders Edition
Installed version of CUDA: 8.0 RC
Installed version of cuDNN: v5 (May 27, 2016), for CUDA 8.0 RC
Output of ls -l /usr/local/cuda/lib64/libcud*:
-rw-r--r-- 1 root root   560184 juin  15 16:06 /usr/local/cuda/lib64/libcudadevrt.a
lrwxrwxrwx 1 root root       16 juin  15 16:06 /usr/local/cuda/lib64/libcudart.so -> libcudart.so.8.0
lrwxrwxrwx 1 root root       19 juin  15 16:06 /usr/local/cuda/lib64/libcudart.so.8.0 -> libcudart.so.8.0.27
-rwxr-xr-x 1 root root   394472 juin  15 16:06 /usr/local/cuda/lib64/libcudart.so.8.0.27
-rw-r--r-- 1 root root   737516 juin  15 16:06 /usr/local/cuda/lib64/libcudart_static.a
-rwxr-xr-x 1 root root 78065952 juin  15 16:10 /usr/local/cuda/lib64/libcudnn.so
-rwxr-xr-x 1 root root 78065952 juin  15 16:10 /usr/local/cuda/lib64/libcudnn.so.5
-rwxr-xr-x 1 root root 78065952 juin  15 16:10 /usr/local/cuda/lib64/libcudnn.so.5.0.5
-rw-r--r-- 1 root root 68709594 juin  15 16:10 /usr/local/cuda/lib64/libcudnn_static.a

Tensorflow installed from source, last commit hash: 7644b3d
Problem
When I open the terminal and type
$ python
and then
>>> import tensorflow
I get:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named tensorflow

Steps to reproduce
Perform 'installing from sources' tutorial step by step https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html#installing-from-sources for a GPU-enabled Tensorflow on Linux 64 bits
What have you tried?
1- Re-installing step by step: no change
2- Typing in terminal $ bazel-bin/tensorflow/cc/tutorials_example_trainer --use_gpu returns the correct output as indicated in the tutorial
3- Typing in terminal $ bazel test -c opt //tensorflow/python:graph_util_test --test_output=streamed returns
OK
Converted 1 variables to const ops.
Converted 1 variables to const ops.
Target //tensorflow/python:graph_util_test up-to-date:
  bazel-bin/tensorflow/python/graph_util_test
INFO: Elapsed time: 379.479s, Critical Path: 299.62s
//tensorflow/python:graph_util_test                                      PASSED in 1.1s

Executed 1 out of 1 test: 1 test passes.

4- Adding /home/paul/Downloads/tensorflow to PYTHONPATH and then retry import tensorflow. This time I get:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/paul/Downloads/tensorflow/tensorflow/__init__.py", line 23, in <module>
    from tensorflow.python import *
  File "/home/paul/Downloads/tensorflow/tensorflow/python/__init__.py", line 48, in <module>
    from tensorflow.python import pywrap_tensorflow
ImportError: cannot import name pywrap_tensorflow

I don't know what else to do to make this work. Would you have an idea?
Thanks a lot in advance,
Paul

```
Author:
```
mrry
```
Text:
```

Did you follow the instructions in Create the pip package and install? This step is necessary for your default Python installation to be able to import tensorflow.

```
Author:
```
paul2254
```
Text:
```

Thank you Derek for your message. It was precisely because of that. Now I feel bad. Next time I'll be more careful not to skip a part of the tutorial.
Now everything works fine, thanks to you!

```
Author:
```
mrry
```
Text:
```

That's no problem - I'm glad it's working, and don't feel bad!

```
Author:
```
vb2408
```
Text:
```

Hi guys, i am facing the same issue but in windows? Please help me to solve

```
Author:
```
wizardboy2010
```
Text:
```

im using ubuntu i followed the tflow doc and im still facing the same problem

```
Author:
```
jvdsidq
```
Text:
```

How can I install Keras after installing theano? I tried to install keras but after complitation when I am trying to import keras it shows me error: No module name tensorflow.
I also changed the default backend from tensorflow to theano but still I am facing the same problem. Could you people please help me to fix it. I am working on Jetson TK1 Embedded Board and the board has some limitations of tensorflow.

```

## 3069
Title:
```

        Installation issue with CUDA 8
      
```
Author:
```
bozhu5
```
Text:
```

Hi,
I've attempted to install Tensorflow with CUDA 8 on Ubuntu 14.04 by installing from source since it doesn't seem like there are binaries available (following https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html#installing-from-sources)
Everything installed well, but once I tried importing, I received this while trying to import tensorflow in python:
ImportError: libcudart.so.7.5: cannot open shared object file: No such file or directory.
I'm not sure where this is coming from, since I'm using CUDA 8.  I did have a previous installation of CUDA 7.5, but all those files got replaced, and there is no libcudart.so.7.5 (or anything 7.5) in the cuda lib64 folder.
Any thoughts? Many Thanks!
Environment info
Operating System: Ubuntu 14.04
Graphics Card: NVIDIA GTX 1080 Founders Edition
Installed version of CUDA and cuDNN: CUDA 8.0, cuDNN 5.0
-rw-r--r-- 1 root     root       560184 Jun 27 16:13 /usr/local/cuda/lib64/libcudadevrt.a
lrwxrwxrwx 1 root     root           16 Jun 27 16:13 /usr/local/cuda/lib64/libcudart.so -> libcudart.so.8.0
lrwxrwxrwx 1 root     root           19 Jun 27 16:13 /usr/local/cuda/lib64/libcudart.so.8.0 -> libcudart.so.8.0.27
-rwxr-xr-x 1 root     root       394472 Jun 27 16:13 /usr/local/cuda/lib64/libcudart.so.8.0.27
-rw-r--r-- 1 root     root       737516 Jun 27 16:13 /usr/local/cuda/lib64/libcudart_static.a
lrwxrwxrwx 1 lfibrain lfibrain       13 Jun 27 17:02 /usr/local/cuda/lib64/libcudnn.so -> libcudnn.so.5
lrwxrwxrwx 1 lfibrain lfibrain       17 Jun 27 17:02 /usr/local/cuda/lib64/libcudnn.so.5 -> libcudnn.so.5.0.5
lrwxrwxrwx 1 lfibrain lfibrain       17 Jun 27 17:46 /usr/local/cuda/lib64/libcudnn.so.5.0 -> libcudnn.so.5.0.5
-rwxr-xr-x 1 lfibrain lfibrain 78065952 Apr 22 15:17 /usr/local/cuda/lib64/libcudnn.so.5.0.5
-rw-r--r-- 1 lfibrain lfibrain 68709594 Apr 22 15:17 /usr/local/cuda/lib64/libcudnn_static.a
If installed from sources, provide the commit hash:
861644c
Steps to reproduce

Install NVIDIA 367 driver
Install CUDA 8.0
Install cuDNN 5.0
Reboot
Install tensorflow from source with bazel using the above configuration

What have you tried?

reconfiguring/reinstalling tensorflow with inputting the exact directory locations (instead of pressing ENTER for default), even if the default locations were already correct.


```
Author:
```
MInner
```
Text:
```

afaik, it requires and work just fine with cuda-7.5 and after you have it installed, you'd have all required .so files at /usr/local/cuda-7.5

```
Author:
```
zongyuange
```
Text:
```

Try to install with cuda7.5 instead. But i found weird results running the CIFAR 10 example under /models/imag/cifar10/cifar10_train.py
Let me know your results.

```
Author:
```
aselle
```
Text:
```

Closing for now, as we unfortunately do not yet support Cuda 8 as was mentioned by @zongyuange  and @MInner.

```
Author:
```
vrv
```
Text:
```

Others have been able to get it working with cuda 8.0, so I'd try a fresh clone of tensorflow in a different directory and use the latest bazel as well.

```
Author:
```
bozhu5
```
Text:
```

Yes indeed - a fresh clone worked out for me.  Thanks everyone.

```
Author:
```
aselle
```
Text:
```

Awesome. Glad you got it to work.

```
Author:
```
aselle
```
Text:
```

Also, there will be a Cuda 8.0 pre built binary when we are out of RC (see @vrv comment on #3052)

```
Author:
```
vrv
```
Text:
```

Our ./configure process unfortunately requires modifying the source code in the tree when you give it something other than the empty string, so re-cloning is probably the best thing to do in cases like these.
Alternatively, if you leave the defaults, it uses whatever is symlinked at libcudnn.so, and then there should be no source code rewriting going on.
@aselle , it's Nvidia we have to wait for, not us.

```
Author:
```
iqbalmohomed
```
Text:
```

@vrv I noticed that the official cuda 8 drivers are out. The tensorflow install instructions still indicate that source compilation is necessary for this version. Are the docs out of date or does the issue remain?

```
Author:
```
steven200796
```
Text:
```

@bozhu5 could you comment your process for working with a new clone? Many people, including myself, are having issues with cuda 8.0 and tf.

```
Author:
```
gokul-uf
```
Text:
```

@aselle Is TensorFlow binary for CUDA 8 ready?

```
Author:
```
andrenatal
```
Text:
```

I keep getting:
ImportError: dlopen(/usr/local/lib/python2.7/site-packages/tensorflow/python/_pywrap_tensorflow.so, 10): Library not loaded: @rpath/libcudart.7.5.dylib
Using CUDA 8 drivers on OSX.

```
Author:
```
aselle
```
Text:
```

Checked in with @gunan. We are aiming for CUDA 8 binaries in rc1.  @andrenatal, your error is because our binaries are for cuda 7.5, so if you want to use cuda 8 right now you have to build it yoruself.

```
Author:
```
gunan
```
Text:
```

@yifeif will keep track of the release of cuda8 binaries.
Yifei, could you close this issue once cuda8 binaries are released?

```
Author:
```
gokul-uf
```
Text:
```

@aselle @gunan What's the ETA of rc1?

```
Author:
```
gunan
```
Text:
```

It depends on the number of issues we see during the release, but at most 1
week.
On Oct 9, 2016 1:59 AM, "Gokula Krishnan" notifications@github.com wrote:

@aselle https://github.com/aselle @gunan https://github.com/gunan
What's the ETA of rc1?
—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub
#3069 (comment),
or mute the thread
https://github.com/notifications/unsubscribe-auth/AHlCOcK5QwccH7WUjZpPC-J46fOTzkyXks5qyKz9gaJpZM4I_rnJ
.


```
Author:
```
laventura
```
Text:
```

Hi @andrenatal --
I get the same error [ ImportError: dlopen(/usr/local/lib/python2.7/site-packages/tensorflow/python/_pywrap_tensorflow.so, 10): Library not loaded: @rpath/libcudart.7.5.dylib ]  on my MacbookPro (OS X 10.11.6) with
-- TensorFlow 0.10
-- Python 2.7.12
I installed CUDA 8.0.
Have you been able to make CUDA 8 and Tensor Flow work??
Thanks,
Atul
Here are the results from deviceQuery:
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GT 750M"
  CUDA Driver Version / Runtime Version          8.0 / 8.0
  CUDA Capability Major/Minor version number:    3.0
  Total amount of global memory:                 2048 MBytes (2147024896 bytes)
  ( 2) Multiprocessors, (192) CUDA Cores/MP:     384 CUDA Cores
  GPU Max Clock rate:                            926 MHz (0.93 GHz)
  Memory Clock rate:                             2508 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 262144 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(65536), 2D=(65536, 65536), 3D=(4096, 4096, 4096)
  Maximum Layered 1D Texture Size, (num) layers  1D=(16384), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(16384, 16384), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 1 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 8.0, CUDA Runtime Version = 8.0, NumDevs = 1, Device0 = GeForce GT 750M
Result = PASS


```
Author:
```
yaroslavvb
```
Text:
```

@laventura 11rc0 and before are only for CUDA 7.5, you have to wait for later version or build from source if you want CUDA 8

```
Author:
```
andrenatal
```
Text:
```

Building from source, at this step:
bazel build -c opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
I  get this error:
ERROR: /Users/anatal/projects/mozilla/tensorflow/tensorflow/core/kernels/BUILD:1020:1: error while parsing .d file: /private/var/tmp/_bazel_anatal/7c0501261859d426c184c23a4c9e36fa/execroot/tensorflow/bazel-out/local_darwin-opt/bin/tensorflow/core/kernels/_objs/adjust_contrast_op_gpu/tensorflow/core/kernels/adjust_contrast_op_gpu.cu.pic.d (No such file or directory). nvcc warning : option '--relaxed-constexpr' has been deprecated and replaced by option '--expt-relaxed-constexpr'. nvcc fatal   : The version ('80000') of the host compiler ('Apple clang') is not supported Target //tensorflow/tools/pip_package:build_pip_package failed to build Use --verbose_failures to see the command lines of failed build steps. INFO: Elapsed time: 262.184s, Critical Path: 250.97s

```
Author:
```
gunan
```
Text:
```

That particular error looks like a mismatch between your XCode version and Cuda.
On ubuntu, I was able to get the source code to compile successfully with cuda8.

```
Author:
```
yaroslavvb
```
Text:
```

Googling for error suggests that you need xcode 7.2
On Oct 11, 2016 12:10 AM, "gunan" notifications@github.com wrote:

That particular error looks like a mismatch between your XCode version and
Cuda.
On ubuntu, I was able to get the source code to compile successfully with
cuda8.
—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub
#3069 (comment),
or mute the thread
https://github.com/notifications/unsubscribe-auth/AABaHIMO77LlzvCp-GQxvlc8Ggh1uk9fks5qyzZUgaJpZM4I_rnJ
.


```

## 32351
Title:
```

        403 Forbidden error in 'Classify structured data' tutorial
      
```
Author:
```
kttn8769
```
Text:
```

Hi,
I got a 403 Forbidden error in the following tutorial section.
https://www.tensorflow.org/beta/tutorials/keras/feature_columns#use_pandas_to_create_a_dataframe
The code is as follows:
URL = 'https://storage.googleapis.com/applied-dl/heart.csv'
dataframe = pd.read_csv(URL)
dataframe.head()

The output:
---------------------------------------------------------------------------
HTTPError                                 Traceback (most recent call last)
<ipython-input-4-bbbf4ab1b496> in <module>()
      1 URL = 'https://storage.googleapis.com/applied-dl/heart.csv'
----> 2 dataframe = pd.read_csv(URL)
      3 dataframe.head()

8 frames
/usr/lib/python3.6/urllib/request.py in http_error_default(self, req, fp, code, msg, hdrs)
    648 class HTTPDefaultErrorHandler(BaseHandler):
    649     def http_error_default(self, req, fp, code, msg, hdrs):
--> 650         raise HTTPError(req.full_url, code, msg, hdrs, fp)
    651 
    652 class HTTPRedirectHandler(BaseHandler):

HTTPError: HTTP Error 403: Forbidden


```
Author:
```
divyanshu132
```
Text:
```

I think may be there is a problem with your internet connectivity.

```
Author:
```
kttn8769
```
Text:
```

@divyanshu132 Thank you. It was a temporary problem of my internet connectivity. Now I can download the csv. Sorry for this irrelevant post.

```
Author:
```
tensorflow-bot
```
Text:
```

Are you satisfied with the resolution of your issue?
Yes
No

```

## 1702
Title:
```

        Print operation flattens the tensors
      
```
Author:
```
pronobis
```
Text:
```

Environment info
Operating System: Linux
Using: pip, 0.7.1 for Python 3
Steps to reproduce
Run:
a=tf.constant([[1], [2]])
b=tf.Print(a, [a])

Output
I tensorflow/core/kernels/logging_ops.cc:79] [1 2]

while the tensor evalutes to:
array([[1],
       [2]], dtype=int32)

Expected output
I tensorflow/core/kernels/logging_ops.cc:79] [[1], [2]]


```
Author:
```
keveman
```
Text:
```

Thanks for filing this issue. tf.Print is primarily as a tool for debugging during graph execution. Making the output nicely formatted is not going to be high priority for us in the near future. But the code to print out the tensor is here [1]. I am marking this issue as 'Contributions welcome' :)
[1] https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor.cc#L628

```
Author:
```
guotong1988
```
Text:
```

If anyone haven't fix this issue , I want to work on it . I have submitted the contribution license today.

```
Author:
```
guotong1988
```
Text:
```

@mrry @keveman
My solution is , cut the total array into the format , in the SummarizeArray method.
For example, cut a tensor of shape (2,2) with the total-array data 1,2,3,4 to print [[1,2][3,4]]
Wondering if there exists a method that do the same?

```
Author:
```
zffchen78
```
Text:
```

This might be easier. tf.Print was created before we have convenient ways to calling python runtime:
def Print(inp, data):
  def np_print(*args):
    for x in args:
      print(x)
  return tf.with_dependencies([tf.py_func(np_print, data, [])], inp)

g = tf.Graph()
with g.as_default():
  x = tf.random_uniform([2, 2])
  y = tf.random_uniform([2, 2])
  z = tf.random_uniform([2, 2])
  x = Print(x, [x, y, z])

with tf.Session(graph=g) as sess:
  x.eval()


```
Author:
```
Mistobaan
```
Text:
```

Is this issue fixed?

```
Author:
```
guotong1988
```
Text:
```

@Mistobaan  Yes, fixed

```
Author:
```
DomenicD
```
Text:
```

So now I get this error when I try and print some gradients:
ValueError: Shapes must be equal rank, but are 3 and 2
From merging shape 10 with other shapes. for 'Print/packed' (op: 'Pack') with input shapes: [2,1,2], [2,2], [2,1,2], [2,2], [2,2,2], [2,2], [2,2,2], [2,2], [2,2,1], [2,1], [2,2,1], [2,1].

```

## 10712
Title:
```

        GPU Error with tf.losses.sparse_softmax_cross_entropy
      
```
Author:
```
rmkemker
```
Text:
```

System information

Have I written custom code (as opposed to using a stock example script provided in TensorFlow): See below
OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Ubuntu 16.04
TensorFlow installed from (source or binary): Binary (PIP)
TensorFlow version (use command below): v1.1.0-rc0-61-g1ec6ed5 1.1.0
Bazel version (if compiling from source): n/a
CUDA/cuDNN version: 8.0/5.1.5
GPU model and memory: NVIDIA Titan X - 12GB
Exact command to reproduce:

import tensorflow as tf
import numpy as np

y = np.random.randint(0, 10, size=40, dtype=np.int32)
logits = np.float32(np.random.rand(40, 10))
weights = np.ones(40, dtype=np.float32)

y_t = tf.placeholder(tf.int32)
logits_t = tf.placeholder(tf.float32)

cost = tf.losses.sparse_softmax_cross_entropy(labels=y,logits=logits, weights=tf.ones(40,dtype=tf.float32))
sess = tf.Session()
sess.run(cost, feed_dict={y_t: y, logits_t: logits})

Describe the problem
Am I doing something wrong or does this function not have a GPU implementation yet?  I guess I can do this on the CPU, but I thought I would check.  It does work on the CPU, I did check that.
Source code / logs
The error message is attached.
error_message.txt

```
Author:
```
aselle
```
Text:
```

cost = tf.losses.sparse_softmax_cross_entropy(labels=y,logits=logits, weights=tf.ones(40,dtype=tf.float32))

labels should be y_t in this line I think. y is type int32, which is causing the error.

```
Author:
```
tensorflowbutler
```
Text:
```

This issue is automatically closed due to lack of activity. Please re-open if this is still an issue for you. Thanks!

```

## 3593
Title:
```

        How to run custom encoder-decoder in Tensorflow using available APIs?
      
```
Author:
```
krayush07
```
Text:
```

I need to run a encoder-decoder model in Tensorflow. I see that using the available APIs basic_rnn_seq2seq(encoder_input_data, decoder_input_data, lstm_cell) etc., an encoder-decoder system can be created. However, few pertaining issues are:

How can we enter the embeddings such as word2vec in such model? I am
aware that we can do embedding lookup but as per the API
encoder_input_data is a list of 2D Tensor of size batch_size x
input_size. How can each word be represented using its respective word embedding in this setup? Even embedding_rnn_seq2seq internally extracts the embeddings. How to give pre-calculated word embeddings as input?
How can we get the cost and perplexity through the API?
In case of test instances, we may not know the corresponding decoder inputs. How to handle such case?


```
Author:
```
michaelisard
```
Text:
```

This kind of usage question is better asked on StackOverflow. GitHub issues are for TensorFlow bugs and installation issues. Thanks!

```

## 7956
Title:
```

        Method log_prob_with_logits() for Dirichlet
      
```
Author:
```
akuz
```
Text:
```

It would be useful to have a log_prob_with_logits() method for the Dirichlet distribution.
The reason being is that it is often useful to model the discrete posterior distribution in log space, which doesn't let all probabilities to go exactly to zero. Then the Dirichlet prior can be applied to the data in log space. Note, that if the posterior is converted to the normalised distribution, then some of the discrete probabilities may actually go to zero due to the rounding errors. Then the Dirichlet prior cannot be applied to this distribution because it doesn't allow zero probabilities.
The log_prob_with_logits() calculation would be very simple to implement. The log(x_i) would need to be replaced with just x_i, and an additional term with LogSumExp(x) added.
This would actually enable the possibility to use the Dirichlet prior on the discrete viariables in log space (can also be part of a neural network).

```
Author:
```
akuz
```
Text:
```

Namely, the formula for log_prob_with_logits(x) would be as follows (where x are logits, and L is the log of the Dirichlet normalisation constant):

Note: formula contains a mistake of using alpha instead of alpha - 1

```
Author:
```
tatatodd
```
Text:
```

@langmore Can you comment on this?  Thanks!

```
Author:
```
langmore
```
Text:
```

Good point akuz.  Rather than adding a new method, I think it would be better to allow the Dirichlet to be initialized either with concentration (as it currently is) OR log_concentration.  See e.g. the Categorical distribution for an example.
I'm choosing log_concentration rather than logits, since to me, logits are something that is intended to be fed through a softmax, and therefore they are only defined up to an additive constant.  Whereas here, the absolute value matters.
Does this sound like something you would want to do?

```
Author:
```
akuz
```
Text:
```

Hi Ian, I guess this could also accept log_concentration in parameter (although I don't have a use case for that). This still doesn't solve the problem I was talking about. The Dirichlet distribution is defined over the categorical distributions. These are the concrete distributions that can be passed as x to log_prob(x). They have to be valid distributions, I.e. sum up to one, and all numbers must be > 0 and < 1. The Dirichlet doesn't allow any of the components to be exactly 0 or 1, and will output NAN in such case. Now imagine that the input to log_prob(x) is such that x = softmax(y). This can easily result in the output like x = [0, 0, 1, ..., 0, 0], for which the Dirichlet log_prob(x) will output NAN. So what I am suggesting is to pass logits directly to log_prob() without applying softmax first. We can do it like Dirichlet.log_prob_with_logits(), which would be similar to cross_entropy_with_logits(). With cross entropy they don't apply softmax before passing to the function for exactly the same reason of potential rounding of the output of softmax to x = [0, 0, 1, ..., 0, 0]. (Aternatively, instead of making a new method, we could add a new parameter to log_prob(x, logits) such that only one of x or logits can be specified. What do you think?

```
Author:
```
langmore
```
Text:
```

You're right, I was mistaken.  The problem with zeros or ones in x needs some sort of log_prob_with_logits function.  I suppose there is another problem if concentration has any zeros in it, but that would require a new version of the Gamma function.
So the solution suggested by @tatatodd is to add a log_prob_with_logits function for distributions defined on the interior of the simplex, {(x_1,...,x_K) :  x_i \in (0, 1), \sum_i x_i = 1}.  This would be Dirichlet, and Beta.
Note however that Gamma.log_prob(x) will fail for the exact same reason if x = 0 (both compute log(x)).  In fact, all of our distributions defined on (0, inf) have this issue.  In my work, I've avoided this by careful use of priors, but before I had this down it was a pain.  It would be good if the solution worked for these distributions as well.  Or, @tatatodd do you think that Dirichlet is more prone to this issue?
@ebrevdo What do you think?

```
Author:
```
akuz
```
Text:
```

I agree about Dirichlet and Beta. Not sure about Gamma, maybe log/exp is not the best transform in that case.

```
Author:
```
ebrevdo
```
Text:
```

I'd prefer a new Dirichlet distribution defined over the logits space,
rather than adding a new method to all distributions.  wdyt?
…
On Sat, Mar 4, 2017 at 11:06 AM, AK ***@***.***> wrote:
 I agree about Dirichlet and Beta. Not sure about Gamma, maybe log is not
 the best transform in that case.

 —
 You are receiving this because you were mentioned.
 Reply to this email directly, view it on GitHub
 <#7956 (comment)>,
 or mute the thread
 <https://github.com/notifications/unsubscribe-auth/ABtim50BEpuZ8vjUzgbvJuk1ohHMweDOks5ribZBgaJpZM4MPGnM>
 .




```
Author:
```
akuz
```
Text:
```

Actually, sounds good, abrevdo. I haven't worked with probabilistic inference much in TensorFlow yet, but I see there is a bunch of distributions already following your suggestion.

```
Author:
```
langmore
```
Text:
```

@ebrevdo , If we simply use the formula above then we do not have the log of a probability density over R^k, so we can't call it log_prob(x).  To see that the above formula is not a log_prob, note that it doesn't go to negative infinity as |x| \to \inf, so the corresponding prob(x) := exp(log_prob(x)) will not go to zero.  You can see also that the above formula is constant if all the x_i are equal.  The reason being that whenever all the x_i are equal, Softmax(x) = [1/k,...., 1/k].  So the entire line {x : x_1 = x_2 = ... = x_k} is mapped by Softmax to a single point.
I believe @akuz wants the standard Dirichlet distribution over k-simplex of probabilities, but wants to evaluate it on an intermediate state of data (before the probabilities are probabilities).
Note @akuz that since this doesn't give you a valid prior on logits, it may be better to create the distribution over logits that corresponds to a specified Dirichlet distribution over probabilities.  After all, your network produces logits.  This can be done as follows:
ds = tf.contrib.distributions
bijectors = tf.contrib.distributions.bijectors  # you'll have to search for this...depending on version.

# The dirichlet is a distribution over the k-1 dimensional k-simplex
dirichlet = ds.Dirichlet(concentration=[1., 2., 3.])
softmax_centered = bijectors.SoftmaxCentered(event_ndims=1)

# dist_over_logits is a distribution over R^{k-1}
dist_over_logits = ds.TransformedDistribution(
    dirichlet,
    bijector=bijectors.Invert(softmax_centered))

logits = [-1., 1.]
probs = softmax_centered.forward(logits)

# These two are equal
probs
==> [ 0.09003057  0.66524088  0.24472845]
tf.nn.softmax(logits + [0.])  # Note implicit appending of [0]
==> [ 0.09003057  0.66524088  0.24472845]

# These two are not equal
dirichlet.log_prob(probs)
==> 0.871526
dist_over_logits.log_prob(logits)
==> -3.35129
The last two lines above are not equal because the Dirichlet is a distribution over the (k-1 dimensional) k-simplex, which is very different (in particular, it is much smaller) than R^{k-1} in which logits live.  The probability density over R^{k-1} must be much smaller at the point logits that corresponds to probs

```
Author:
```
langmore
```
Text:
```

....in the above example, dirichlet is the distribution for a random variable Z = Dirichlet([1, 2, 3]), and dist_over_logits is the distribution of the random variable X = InverseSoftmaxCentered(Z), i.e. Z = SoftmaxCentered(X).  In other words, Z is the correct distribution for your logits.

```
Author:
```
akuz
```
Text:
```

@langmore you're right that the above formula doesn't define a proper density on the k-D space of logits, due to the reasons you mentioned, so it would not make sense to call it log_prob(x)... The transformed distribution trick you suggested looks great, but I just looked through the documentation, and it seems SoftmaxCentered only supports low dimensionality inputs. What I have is a 4D tensor, the last dimension of which would be the logits, so I'm afraid the transformed distribution might not work in this case? Also would that be efficient?
On the other side, if you ask yourself the following question: "Does the above formula calculate log probability of softmax(x) under the specified Dirichlet prior?" - the answer is yes. So, it does not provide the density in the space of logits, but rather in the space of discrete distributions resulting from softmax(x). So, all I'm trying to do is: 1) y = softmax(x), 2) Dirichlet(concentrations).log_prob(y). But because softmax has a tendency to collapse to [0, 0, ..., 1, 0] due to rounding, the Dirichlet log_prob fails to work properly. The above formula would provide a shortcut to compute steps 1) and 2) in one go, without actually computing softmax. Yes, it would not define a valid density on x, and therefore maybe should not be implemented as a Distribution. Maybe it would be better if implemented as some sort of function on tensors? dirichlet_log_prior_on_softmax(concentrations, logits)? Well, maybe a better name would be needed :)
So, it short, I'm not looking to define any new types of Distributions, but an efficient way to compute steps 1) and 2) above in one go, without actually computing the softmax in between. Similar concept to cross_entropy_with_logits().

```
Author:
```
akuz
```
Text:
```

In fact, if we ignore the normalisation constant for now, the above formula can be implemented using the convolution (where concentrations would be used as weights for the last dimension) for the first part, and reduce_logsumexp() for the second part (you would also need to compute and multiply it by the negative of the sum of concentrations). But this implementation has two drawbacks 1) you need to configure the convolution in a special way, and it is only implemented for some specific shapes of tensors, whereas here we always need to convolve along the last dimension only, and 2) it produces two intermediate tensors, which are the summed up. Therefore, a specific implementation would be much more efficient.
Also, the dirichlet_prior_on_softmax() could just sum up the numbers along all dimensions above the last one, because all that is usually needed is the total log probability (user may need to specify the axis for the computation, and whether to reduce all the others axes). In case when everything is reduced to one number, a sum of log probabilities along all remaining dimensions, this function would not produce any intermediate tensors at all, and would just output a scalar.

```
Author:
```
langmore
```
Text:
```

@akuz , I agree that your original suggestion does provide an alternative method to compute the log_prob on the space of probabilities by intercepting an intermediate step of computation of an input.
So.... we can't call this log_prob since it isn't one.  akuz's original suggestion of log_prob_with_logits(x) would work (although I think the alpha in the formula should be alpha - 1).  @ebrevdo I think the options are:

Do nothing, let users build their own (Dirichlet._log_unnormalized_prob will help BTW)
Write a helper function, e.g. dirichlet_log_prob_with_logits(dirichlet_dist, logits).
Create a Dirichlet.log_prob_with_logits(logits) method.

BTW, the dimensionality restriction on SoftmaxCentered is that it works for batch scalars and vectors (event_ndims = 0 or 1), not batch matrices (event_ndims = 2).  So it would work well for a Tensor of shape [2, 3, 4, 5], representing a shape [2, 3, 4] batch of length [5] logits.  But, it seems this is not what you need.

```
Author:
```
akuz
```
Text:
```

@langmore , I think that option 3 from your list of suggestions would be most convenient to use in practice. Sorry about the mistake missing -1 in the formula. The computation of the "L" part in the formula should be possible to do easily too (I've done it with lngamma function in C++ previously). I think I would not be the only one to need this, hopefully.
P.S. Thanks for explaining about the SoftmaxCentered, I didn't understand before what was the event_ndim.

```
Author:
```
akuz
```
Text:
```

@langmore I was looking more into prior distributions defined on R+, such as Gamma, InverseGamma, etc. I think these would benefit from something like log_prob_with_softplus(). I've made a simple model of clustering using expectation maximisation. In it, the latent variables (cluster assignments) and the parameters of the clusters (cluster probs, means, stdevs) are estimated using a single optimizer loop (all together). If I put the stdevs directly as the variables to optimize, this leads to problems, because optimizers don't allow specifying the bounds. So what I ended up doing is:
stdevs_raw = tf.Variable(...)
stdevs = tf.nn.softplus(stdevs_raw) - this makes the stdevs always positive
stdevs_prior = tf.constrib.distributions.InverseGamma(100, 10).log_prob(tf.pow(stdevs, 2))
However, this still has a problem if one of the stdevs collapses to zero (which is possible if stdevs_raw becomes a large negative number).
Therefore, it would be useful to have something like InverseGamma.log_prob_with_softplus(x) which would compute the log probability for softplus(x) without actually computing the softplus.
Maybe this can be done with some variable transformations? I am not sure

```
Author:
```
langmore
```
Text:
```

Question:  Why did you feed stdevs ** 2 to log_prob rather than stdevs?
I see this as a good features request.  We have to figure out if there is a solution that will work across different distributions.  Building upon your previous suggestion, what about log_prob_pre_X, where X is softmax, softplus, exp, etc...  ?
I don't think this will be resolved immediately.  So for the moment I recommend writing helper functions.  This will actually be better since you can see what works and give us feedback.  If you want, you could add a helper function to the same file that contains the class and submit a pull request.  E.g. add log_prob_pre_softmax(dist, logits) to dirichlet.py, along with some tests.  For the moment, keep it hidden, i.e. don't add it to the __all__ list at the top of the file.  If this helper function works well, we can either un-hide it, or add it as a method.
Also, and I realize every use case is different, let me tell you how I've been able to solve this issue.  So far, I've been able to avoid the collapse to zero (with 32 bit tensors) by using AdamOptimizer with a small step size of around 0.01 and making sure that the prior's log-prob was included in my loss (you're already doing this I assume, but just in case...).  So in your case above I make sure my loss is -1 * log_likelihood - 1 * stdevs_prior.  In theory, the penalty from the prior should prevent collapse to zero, but in practice of course many crazy things can happen, especially when you have hidden layers.

```
Author:
```
akuz
```
Text:
```

@langmore , I fed stdevs ** 2 to InverseGamma, because inverse gamma is a conjugate prior for the variance of Normal with known mean. The conjugacy doesn't play much role here, but there is another benefit. The conjugate prior hyperparameters have interpretation that is easy for me to use to set a specific prior, see here: https://en.m.wikipedia.org/wiki/Conjugate_prior#Continuous_distributions (see "Interpretation of hyperparameters" column).
I agree that would be a useful feature (partially because I've created this request :)), because of the collapse of the values (resulting from softmax or softplus) to zeroes, which renders many useful priors invalid, if not calculated in log space directly. As you say, it's not clear what would be the best way to implement it in conjunction with what already exists. When I have time, I will try to follow your suggestion, but I have to spend most of my time on my full time job. Hopefully I can find some time on lunch breaks / evenings soon.

```
Author:
```
akuz
```
Text:
```

@ebrevdo - just saw the new paper that came out "Deep Probabilistic Programming" - how do you deal with the problem described in this ticket within the Edward lib?

```
Author:
```
tensorflowbutler
```
Text:
```

It has been 14 days with no activity and this issue has an assignee.Please update the label and/or status accordingly.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assigneee: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
langmore
```
Text:
```

I'll bring this up to the team.  I think the way to think of this is that we would offer a version of Dirichlet (and others) that has been "pre-transformed" (in a stable manner) to unconstrained space using some Bijector.  E.g. DiricheletUnconstrained would be a stable equivalent to
tfd = tf.contrib.distributions
tfb = tfd.bijectors
dist = tfd.Dirchlet([0.5, 0.5])
dist_uc = tfd.TransformedDistribution(
    dist,
    bijector=tfb.Invert(tfb.SoftmaxCentered()))

```
Author:
```
dustinvtran
```
Text:
```

I like your solution @langmore to use transformed distribution. Among other things, a canned implementation could be useful for Dirichlet priors on Categorical/Multinomial logits.
How do you propose handling the fact that the desired function doesn't normalize? If I understand the discussion correctly, dist_uc.log_prob does not return the same as "log_prob_pre_softmax"?

@akuz: @ebrevdo - just saw the new paper that came out "Deep Probabilistic Programming" - how do you deal with the problem described in this ticket within the Edward lib?

This is actually a problem in Edward's mixture models. We just work in the probs space and it can be unstable.
Examples:

examples/stochastic_block_model.py
examples/mixture_gaussian_gibbs.py


```
Author:
```
langmore
```
Text:
```

Note that I'm not suggesting we use transformed distribution (since what I wrote above would be no more stable than Dirichlet.  I'm suggesting we pre-bake an equivalent distribution.
I don't understand the normalization issue.  Perhaps tell me what the args are above to log_prob and log_prob_pre_softmax?

```
Author:
```
dustinvtran
```
Text:
```

Oh I see. I'm only for a canned distribution over logits space;  so I still agree :)
I don't understand the normalization issue either. The above conversation is rather involved—something about log_prob_with_logits(x) in the latex formula not defining a proper density? Maybe you can summarize how that relates to your "implement a canned distribution" proposal?

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```

## 16979
Title:
```

        [Critical some questions] Tensorflow-lite, Neural Networks API
      
```
Author:
```
Nanamare
```
Text:
```

Hi.
Some question.
1.

Current i use  tensorflow library   compile 'org.tensorflow:tensorflow-lite:+'
and i want to use Neural Networks Api, to reduce inference time.
but wrapper function is not existing in Interpreter.java class
  private static native void useNNAPI(long var0, boolean var2);
so i can't use it..
If I create a wrapper function, can I use Neural Networks API? (my device level >  8.1)

What is https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/java/src/testhelper/java/org/tensorflow/lite/TestHelper.java
?
2.

i'm converting pb to tflite. mobilenet_v1_224.pb (17 mb) mobilenet_v1_224_uint8.tflite (4 mb)
inference speed about 290 ms -> 73ms decreased


Command line(mobileNet)


bazel run -c opt --copt=-msse4.1 --copt=-msse4.2 --config=opt \
  //tensorflow/contrib/lite/toco:toco -- \
  --input_file=/home/danshin/tensorflow_lite/lite_model/frozen_graph.pb \
  --output_file=/home/danshin/tensorflow_lite/lite_model/frozen_uint_graph.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --inference_type=QUANTIZED_UINT8 \
  --input_shape=1,224,224,3 \
  --input_array=input \
  --output_array=MobilenetV1/Predictions/Reshape_1 \
  --default_ranges_min=0 \
  --default_ranges_max=6 \
  --mean_value=127.5 \
  --std_value=127.5


In a similar way,
But frozen_cpm.pb(120 mb) convert to frozen_cpm_uint8.tflite(30 mb)
inference speed about 11000 ms -> 11000ms.
If the model size is reduced, does not the inference time generally decrease?


```
Author:
```
tensorflowbutler
```
Text:
```

Thank you for your post. We noticed you have not filled out the following field in the issue template. Could you update them if they are relevant in your case, or leave them as N/A? Thanks.
Have I written custom code
OS Platform and Distribution
TensorFlow installed from
TensorFlow version
Bazel version
CUDA/cuDNN version
GPU model and memory
Exact command to reproduce

```
Author:
```
Nanamare
```
Text:
```

@tensorflowbutler
OS Platform and Distribution :  Ubuntu 16.04 LTS
TensorFlow installed from : official
TensorFlow version : 1.5 version
Bazel version : 0.9.0
CUDA/cuDNN version : V 8.0.61 (8.0)
GPU model and memory : GeForce GTX 1060 / 3G
Exact command to reproduce :
bazel run -c opt --copt=-msse4.1 --copt=-msse4.2 --config=opt \
  //tensorflow/contrib/lite/toco:toco -- \
  --input_file=/home/danshin/tensorflow_lite/lite_model/frozen_cpm.pb \
  --output_file=/home/danshin/tensorflow_lite/lite_model/frozen_uint8_cpm.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --input_shape=1,368,368,3 \
  --inference_type=QUANTIZED_UINT8 \
  --input_array=inference_images/Placeholder \
  --output_array=stage6/confidence_maps/BiasAdd \
  --logtostderr


```
Author:
```
Nanamare
```
Text:
```

@cy89 , @aselle

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Awaiting TensorFlower: It has been 14 days with no activity and the awaiting tensorflower label was assigned. Please update the label and/or status accordingly.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging TensorFlower: It has been 14 days with no activity and the awaiting tensorflower label was assigned. Please update the label and/or status accordingly.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @tatatodd: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
andrehentz
```
Text:
```

I think there's already an official way to turn on the NNAPI in the JAVA Api of TF Lite. It will not make much of a difference unless your device provides NNAPI acceleration.

```

## 10819
Title:
```

        Tensorflow Android API version 1.2 not in JCenter
      
```
Author:
```
andreas-eberle
```
Text:
```

The freshly released version 1.2 of the tensorflow APIs is not yet fully available in JCenter ( https://bintray.com/google/tensorflow/tensorflow-android/1.2.0). There is a version 1.2.0 but it does not contain any files.
Can you push these files to the repository?

```
Author:
```
aselle
```
Text:
```

@petewarden, I have no idea if we support this or about JCenter in general. Could you point me to the right direction or right person?

```
Author:
```
andrewharp
```
Text:
```

Shawn has created the listing
<https://bintray.com/google/tensorflow/tensorflow-android/1.2.0> for it, so
I believe he just needs to upload the AAR and pull the switch to make it
the latest version now.
…
On Jun 19, 2017 12:51 PM, "Andrew Selle" ***@***.***> wrote:
 @petewarden <https://github.com/petewarden>, I have no idea if we support
 this or about JCenter in general. Could you point me to the right direction
 or right person?

 —
 You are receiving this because you are subscribed to this thread.
 Reply to this email directly, view it on GitHub
 <#10819 (comment)>,
 or mute the thread
 <https://github.com/notifications/unsubscribe-auth/ADOGsRvLhxtp_0jvY6A5LAPKuyVmIcOtks5sFqcdgaJpZM4N-BBe>
 .




```
Author:
```
andrewharp
```
Text:
```

1.2.0 files for TF Android are now available on JCenter!

```

## 24919
Title:
```

        About the MFCC feature in input_data.py
      
```
Author:
```
ucasiggcas
```
Text:
```

Dear,
In the script,
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/speech_commands/input_data.py
is there any related pdf or other file about the mfcc feature extraction,
Could U help me about this, please?
Any advice or suggestion will be okey.
Thx.

```
Author:
```
ucasiggcas
```
Text:
```

Second,
What's the meaning of the func get_features_range in input_data.py ?
  # TODO(petewarden): These values have been derived from the observed ranges of spectrogram and MFCC inputs. If the preprocessing pipeline changes, they may need to be updated.
and also the up words ?
If the sample_rate change, need change the range?
Any help will be good.
Thx

```
Author:
```
jvishnuvardhan
```
Text:
```

@ucasiggcas Please post this kind of support questions at Stackoverflow. There is a big community to support. Github is mainly for addressing bugs in installation and performance. I found this paper and there are several resources covering advanced MFCC. Thanks!

```
Author:
```
ucasiggcas
```
Text:
```


@ucasiggcas Please post this kind of support questions at Stackoverflow. There is a big community to support. Github is mainly for addressing bugs in installation and performance. I found this paper and there are several resources covering advanced MFCC. Thanks!

Thanks,
I have another question,
in the rows of 420,437,443
 tf.summary.image( 'spectrogram', tf.expand_dims(spectrogram, -1), max_outputs=1)
What does it mean?No Variable?Is it useful?
Thx

```
Author:
```
jvishnuvardhan
```
Text:
```

@ucasiggcas -1 refers to expanding dimensions in the end of the tensor. Please take a look at here for more details. If max_outputs is 1, the summary value tag is 'name/image'. please check here. Thanks!
I am closing the issue but please post this kind of support questions at Stackoverflow. Thanks!

```

## 25314
Title:
```

        label_image segmentation issue for operator code 25 which is softmax
      
```
Author:
```
praveen-dn
```
Text:
```

When using the standard label_image to test the mobilenet tflite file in the default P OS android NN.
we are facing the segmentation issue for the softmax operation with the default command as specified in the readme.md.
We are using latest Android NN on P Os, for Arm64-v8a series soc.
The following is the crash snippet:
01-24 15:28:12.701 I/ExecutionBuilder( 4787): ExecutionBuilder::startCompute (from plan, iteratively)
01-24 15:28:12.701 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:12.702 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 0
01-24 15:28:12.702 I/ExecutionBuilder( 4787): input[0] = POINTER(0x7bfcf4ac00)
01-24 15:28:12.702 I/ExecutionBuilder( 4787): output[0] = POINTER(0x7bfce00fc0)
01-24 15:28:12.707 I/CpuExecutor( 4787): CpuExecutor::run() with request({.inputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 0, .offset = 0, .length = 602112}, .dimensions = [4]{1, 224, 224, 3}}}, .outputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 1, .offset = 0, .length = 4004}, .dimensions = [2]{1, 1001}}}, .pools = [0]{}})
01-24 15:28:12.707 I/CpuExecutor( 4787): CpuExecutor::initializeRunTimeInfo
01-24 15:28:12.763 D/SDHMS:ComponentLevelSetter(22281): mWifiTotalUsage = 0, throughput = 0.0
01-24 15:28:12.928 I/CpuExecutor( 4787): Completed run normally
01-24 15:28:12.932 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:12.932 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 1
01-24 15:28:12.934 I/ExecutionBuilder( 4787): ExecutionBuilder::ExecutionBuilder
01-24 15:28:12.936 I/ExecutionBuilder( 4787): ExecutionBuilder::startCompute (from plan, iteratively)
01-24 15:28:12.936 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:12.936 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 0
01-24 15:28:12.936 I/ExecutionBuilder( 4787): input[0] = POINTER(0x7bfcf4ac00)
01-24 15:28:12.936 I/ExecutionBuilder( 4787): output[0] = POINTER(0x7bfce00fc0)
01-24 15:28:12.940 I/CpuExecutor( 4787): CpuExecutor::run() with request({.inputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 0, .offset = 0, .length = 602112}, .dimensions = [4]{1, 224, 224, 3}}}, .outputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 1, .offset = 0, .length = 4004}, .dimensions = [2]{1, 1001}}}, .pools = [0]{}})
01-24 15:28:12.941 I/CpuExecutor( 4787): CpuExecutor::initializeRunTimeInfo
01-24 15:28:13.295 I/UiThreadMonitor(20720): setAwake 103 5001
01-24 15:28:13.301 I/CpuExecutor( 4787): Completed run normally
01-24 15:28:13.305 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:13.305 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 1
01-24 15:28:13.306 I/ExecutionBuilder( 4787): ExecutionBuilder::ExecutionBuilder
01-24 15:28:13.307 I/ExecutionBuilder( 4787): ExecutionBuilder::startCompute (from plan, iteratively)
01-24 15:28:13.307 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:13.307 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 0
01-24 15:28:13.307 I/ExecutionBuilder( 4787): input[0] = POINTER(0x7bfcf4ac00)
01-24 15:28:13.307 I/ExecutionBuilder( 4787): output[0] = POINTER(0x7bfce00fc0)
01-24 15:28:13.308 I/CpuExecutor( 4787): CpuExecutor::run() with request({.inputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 0, .offset = 0, .length = 602112}, .dimensions = [4]{1, 224, 224, 3}}}, .outputs = [1]{{.hasNoValue = 0, .location = {.poolIndex = 1, .offset = 0, .length = 4004}, .dimensions = [2]{1, 1001}}}, .pools = [0]{}})
01-24 15:28:13.308 I/CpuExecutor( 4787): CpuExecutor::initializeRunTimeInfo
01-24 15:28:13.547 I/CpuExecutor( 4787): Completed run normally
01-24 15:28:13.551 I/ExecutionBuilder( 4787): looking for next StepExecutor
01-24 15:28:13.551 I/ExecutionPlan( 4787): ExecutionPlan::next(0x7c00830460, 0x7bfe80c308): mNextStepIndex = 1
--------- beginning of crash
01-24 15:28:13.554 F/libc    ( 4787): Fatal signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x3d38 in tid 4787 (label_image), pid 4787 (label_image)
01-24 15:28:13.636 I/crash_dump64( 5086): obtaining output fd from tombstoned, type: kDebuggerdTombstone
01-24 15:28:13.639 I//system/bin/tombstoned( 5616): received crash request for pid 4787
01-24 15:28:13.641 I/crash_dump64( 5086): performing dump of process 4787 (target tid = 4787)
01-24 15:28:13.644 F/DEBUG   ( 5086): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
01-24 15:28:13.645 F/DEBUG   ( 5086): Build fingerprint: 'samsung/beyond2ltexx/beyond2:9/PPR1.180610.011/G975FXXE1ASAM:eng/test-keys'
01-24 15:28:13.645 F/DEBUG   ( 5086): Revision: '20'
01-24 15:28:13.645 F/DEBUG   ( 5086): ABI: 'arm64'
01-24 15:28:13.645 F/DEBUG   ( 5086): pid: 4787, tid: 4787, name: label_image  >>> ./label_image <<<
01-24 15:28:13.645 F/DEBUG   ( 5086): signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x3d38
01-24 15:28:13.646 F/DEBUG   ( 5086):     x0  0000005dc122ebf8  x1  0000000000000000  x2  0000000000000000  x3  0000007c00ef33c8
01-24 15:28:13.646 F/DEBUG   ( 5086):     x4  0000007fd73faad8  x5  0000000000000020  x6  0000007fd73faaa8  x7  0000000000000010
01-24 15:28:13.646 F/DEBUG   ( 5086):     x8  0000000000003d38  x9  385838b172084ce5  x10 00000000000012b3  x11 00000000000012b3
01-24 15:28:13.646 F/DEBUG   ( 5086):     x12 0000000000000003  x13 00000000ffffffff  x14 0000007fd73fa6a4  x15 0000007fd73fa23c
01-24 15:28:13.646 F/DEBUG   ( 5086):     x16 0000007c00ef11b0  x17 0000007c00e87120  x18 0000007fd73fa23a  x19 0000007c0082d2c0
01-24 15:28:13.646 F/DEBUG   ( 5086):     x20 0000005dc122ebf8  x21 0000007c0082b0b0  x22 0000007c0082b0a0  x23 0000005dc11cf6ff
01-24 15:28:13.647 F/DEBUG   ( 5086):     x24 0000005dc11dbf2a  x25 0000005dc11cf78e  x26 000000000000028d  x27 0000007c00831480
01-24 15:28:13.647 F/DEBUG   ( 5086):     x28 0000007c008314a8  x29 0000000000000018
01-24 15:28:13.647 F/DEBUG   ( 5086):     sp  0000007fd73fab90  lr  0000005dc105c084  pc  0000005dc105c090
01-24 15:28:13.648 I/unwind  ( 5086): Malformed section header found, ignoring...
01-24 15:28:13.651 F/DEBUG   ( 5086): 
01-24 15:28:13.651 F/DEBUG   ( 5086): backtrace:
01-24 15:28:13.651 F/DEBUG   ( 5086):     #00 pc 0000000000017090  /data/local/tmp/androidnn/label_image
01-24 15:28:13.651 F/DEBUG   ( 5086):     #01 pc 00000000000179e0  /data/local/tmp/androidnn/label_image
01-24 15:28:13.651 F/DEBUG   ( 5086):     #02 pc 0000000000017a88  /data/local/tmp/androidnn/label_image
01-24 15:28:13.652 F/DEBUG   ( 5086):     #03 pc 00000000000aeeb4  /system/lib64/libc.so (__libc_init+88)
01-24 15:28:14.039 I/crash_dump64( 5086): Start dumpstate
01-24 15:28:14.054 W/NativeCrashListener( 5488): Couldn't find ProcessRecord for pid 4787
01-24 15:28:14.057 E//system/bin/tombstoned( 5616): Tombstone written to: /data/tombstones/tombstone_01
01-24 15:28:14.062 E/audit   ( 5261): type=1701 audit(1548323894.051:192): auid=4294967295 uid=0 gid=0 ses=4294967295 subj=u:r:su:s0 pid=4787 comm="label_image" exe="/data/local/tmp/androidnn/label_image" sig=11 res=1
01-24 15:28:14.071 I/BootReceiver( 5488): Copying /data/tombstones/tombstone_01 to DropBox (SYSTEM_TOMBSTONE)
01-24 15:28:14.117 I/HqmInfo::LogAnalyzer( 5488): ContextBroadcastReceiver : received DropBoxManager "SYSTEM_TOMBSTONE" event
01-24 15:28:14.118 I/HqmInfo::LogAnalyzer( 5488): MSG_TYPE:MSG_APP_CRASH_CHECK_REQ
01-24 15:28:14.120 W/BroadcastQueue( 5488): Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.stats.service.DropBoxEntryAddedReceiver
01-24 15:28:14.121 I/HqmInfo::AppCrashAnalyzer( 5488): checkAppError: list is null
01-24 15:28:14.123 D/dumpstate( 5093): Loading stats from /data/log/dumpstate-stats.txt
01-24 15:28:14.124 I/dumpstate( 5093): Average max progress: 1492 in 1 runs; estimated max: 1492
01-24 15:28:14.132 I/dumpstate( 5093): begin
01-24 15:28:14.133 I/dumpstate( 5093): dumpstate info: id=2, args='/system/bin/dumpstate -k -z', extra_options= app_native)
01-24 15:28:14.133 I/dumpstate( 5093): bugreport format version: 2.0
01-24 15:28:14.134 D/dumpstate( 5093): Bugreport dir: /data/log
01-24 15:28:14.134 D/dumpstate( 5093): Base name: dumpstate_app_native
01-24 15:28:14.134 D/dumpstate( 5093): Suffix: 2019-01-24-15-28-14
01-24 15:28:14.134 D/dumpstate( 5093): Log path: /data/log/dumpstate_app_native-2019-01-24-15-28-14-dumpstate_log-5093.txt
01-24 15:28:14.134 D/dumpstate( 5093): Temporary path: /data/log/dumpstate_app_native-2019-01-24-15-28-14.tmp
01-24 15:28:14.134 D/dumpstate( 5093): Screenshot path: 
01-24 15:28:14.134 D/dumpstate( 5093): Creating initial .zip file (/data/log/dumpstate_app_native-2019-01-24-15-28-14.zip)
01-24 15:28:14.135 D/dumpstate( 5093): Adding zip text entry version.txt
01-24 15:28:14.136 I/dumpstate( 5093): Vibrate: 'cmd vibrator vibrate 150 dumpstate'
01-24 15:28:14.143 I/ActivityManager( 5488): Killing 3567:com.samsung.android.bixby.agent/5018 (adj 906): empty #31
01-24 15:28:14.146 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.154 W/BroadcastQueue( 5488): Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.chimera.GmsIntentOperationService$PersistentTrustedReceiver
01-24 15:28:14.196 I/chatty  ( 5488): uid=1000(system) ActivityManager identical 5 lines
01-24 15:28:14.202 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.206 V/VibratorService( 5488): vibrate - package: dumpstate, token: com.android.server.VibratorService@62e6ba4, usage: 0, effect: OneShot{mDuration=150, mAmplitude=-1, mMagnitude=-1, mMagnitudeType=TYPE_EXTRA}, mag: 10000, TYPE_EXTRA
01-24 15:28:14.206 D/VibratorService( 5488): Turning vibrator off
01-24 15:28:14.207 D/SecVibrator-HAL( 5296): writeNode node:/sys/class/timed_output/vibrator/enable val:0
01-24 15:28:14.211 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.213 D/VibratorService( 5488): vibratorOn() : 150ms, amplitude :-1, mag :10000, f : 0
01-24 15:28:14.215 D/SecVibrator-HAL( 5296): writeNode node:/sys/class/timed_output/vibrator/multi_freq val:0
01-24 15:28:14.217 D/SecVibrator-HAL( 5296): writeNode node:/sys/class/timed_output/vibrator/intensity val:10000
01-24 15:28:14.217 D/SecVibrator-HAL( 5296): writeNode node:/sys/class/timed_output/vibrator/enable val:150
01-24 15:28:14.219 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.293 I/chatty  ( 5488): uid=1000(system) ActivityManager identical 9 lines
01-24 15:28:14.301 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.305 V/[DMS]SemDesktopModeStateNotifier( 5488): binderDied(): DesktopModeListenerInfo(name=com.samsung.android.bixby.agent.app.BixbyApplication$$Lambda$1@bfd57fd, pid=3567, uid=5018)
01-24 15:28:14.307 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.309 D/ForegroundUtils(21076): Process died; UID 5018 PID 3567
01-24 15:28:14.309 D/ForegroundUtils(21076): could not check pending caller
01-24 15:28:14.309 D/ForegroundUtils(21076): Foreground changed, PID: 3567 UID: 5018 foreground: false
01-24 15:28:14.309 D/ForegroundUtils(21076): Foreground UID/PID combinations:
01-24 15:28:14.310 D/ForegroundUtils(21076): UID: 10110 PID: 23150
01-24 15:28:14.323 W/libprocessgroup( 5488): kill(-3567, 9) failed: No such process
01-24 15:28:14.323 I/libprocessgroup( 5488): Successfully killed process cgroup uid 5018 pid 3567 in 177ms
01-24 15:28:14.328 I/Zygote  ( 5267): Process 3567 exited due to signal (9)
01-24 15:28:14.369 D/VibratorService( 5488): Turning vibrator off
01-24 15:28:14.370 D/SecVibrator-HAL( 5296): writeNode node:/sys/class/timed_output/vibrator/enable val:0
01-24 15:28:14.376 D/[a11y]  ( 5488): getUserAccounts0
01-24 15:28:14.379 I/chatty  ( 5488): uid=1000(system) Binder:5488_11 identical 1 line
01-24 15:28:14.381 D/[a11y]  ( 5488): getUserAccounts0
01-24 15:28:14.401 E/dumpstate( 5093): can't find the pid
01-24 15:28:14.402 E/dumpstate( 5093): Failed to find: /data/misc/anrd/
01-24 15:28:14.402 D/dumpstate( 5093): Skipping systrace because '/sys/kernel/debug/tracing/tracing_on' content is '0'
01-24 15:28:14.402 D/dumpstate( 5093): /data/misc/raft does not exist or is not a directory
01-24 15:28:14.403 D/dumpstate( 5093): Adding dir /cache/recovery (recursive: 1)
01-24 15:28:14.406 D/[a11y]  ( 5488): getUserAccounts0
01-24 15:28:14.649 D/dumpstate( 5093): Duration of '/cache/recovery': 0.246s
01-24 15:28:14.649 D/dumpstate( 5093): Adding dir /data/misc/recovery (recursive: 1)
01-24 15:28:14.650 D/dumpstate( 5093): Duration of '/data/misc/recovery': 0.001s
01-24 15:28:14.650 D/dumpstate( 5093): Adding dir /data/misc/update_engine_log (recursive: 1)
01-24 15:28:14.650 D/dumpstate( 5093): Duration of '/data/misc/update_engine_log': 0.000s
01-24 15:28:14.650 D/dumpstate( 5093): Adding dir /data/misc/logd (recursive: 0)
01-24 15:28:14.651 D/dumpstate( 5093): Duration of '/data/misc/logd': 0.000s
01-24 15:28:14.651 D/dumpstate( 5093): Adding dir /data/misc/profiles/cur (recursive: 1)
01-24 15:28:14.765 D/dumpstate( 5093): Duration of '/data/misc/profiles/cur': 0.114s
01-24 15:28:14.765 D/dumpstate( 5093): Adding dir /data/misc/profiles/ref (recursive: 1)
01-24 15:28:14.815 D/dumpstate( 5093): Duration of '/data/misc/profiles/ref': 0.050s
01-24 15:28:14.858 D/dumpstate( 5093): Adding zip text entry systemserver_fileinfo.txt
01-24 15:28:14.858 D/dumpstate( 5093): Duration of 'FILE INFO': 0.043s  ```

The default AI Benchmark successfully runs all the models which definitely has softmax operation also.
Is there any known reason for softmax failure via lable_image.



```
Author:
```
freedomtan
```
Text:
```

It seems it's caused by NNAPI stuff not TFLite.

```
Author:
```
shashishekhar
```
Text:
```

@praveen-dn : @freedomtan is correct.
@praveen-dn : Which label example were you testing and how did you enable NNAPI?

```
Author:
```
shashishekhar
```
Text:
```

@praveen-dn: Please reopen if you are still seeing the issue.

```

## 12546
Title:
```

        Simple release note typo.
      
```
Author:
```
papower1
```
Text:
```

Simple typo on 1.3.0 release note.


```
Author:
```
printdhruv
```
Text:
```

I initiated pull request based on your suggestion, link

```

# Pull
## 18846
Title:
```

        Enable int8 support for FloorDiv
      
```
Author:
```
yongtang
```
Text:
```

int8 is enabled for FloorDiv in math_ops.cc though the kernel was not registered.
This fix register the int8 kernel for FloorDiv, and enables the test case for it.
Signed-off-by: Yong Tang yong.tang.github@outlook.com

```

## 1302
Title:
```

        Corrected unbalanced parentheses in docs.
      
```
Author:
```
KonradMagnusson
```
Text:
```

Fixed small typo in the python API-docs for class tf.train.Optimizer.

```
Author:
```
tensorflow-jenkins
```
Text:
```

Can one of the admins verify this patch?

```
Author:
```
vrv
```
Text:
```

I think I merged this a few days back.

```

## 19999
Title:
```

        r1.9-rc1 cherry-pick request: bugfix/memory leak fix
      
```
Author:
```
akshaym
```
Text:
```


No description provided.


```

## 15901
Title:
```

        Branch 180993147
      
```
Author:
```
raghuraman-k
```
Text:
```


No description provided.


```
Author:
```
tensorflow-jenkins
```
Text:
```

Can one of the admins verify this patch?

```
Author:
```
raghuraman-k
```
Text:
```

@tensorflow-jenkins
"test this please"

```
Author:
```
raghuraman-k
```
Text:
```

All tests pass except interleave_op_test, which timesout (same as seen in previous CLs)

```
Author:
```
caisq
```
Text:
```

@tensorflow-jenkins test this please

```

## 2110
Title:
```

        update configuration in os_setup.md
      
```
Author:
```
fayeshine
```
Text:
```

update configuration in os_setup.md according to master branch

```
Author:
```
tensorflow-jenkins
```
Text:
```

Can one of the admins verify this patch?

```

## 14298
Title:
```

        Updating the bazel version in the install from sources page.
      
```
Author:
```
av8ramit
```
Text:
```


No description provided.


```

## 24983
Title:
```

        TF Keras vis_utils_test introducing test cases
      
```
Author:
```
Dayananda-V
```
Text:
```

Test case introducing for vis_utils.py file under keras package.

```
Author:
```
Dayananda-V
```
Text:
```

@tanzhenyu
Please help to review the test case

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Reviewer @tanzhenyu: You have been added as a reviewer to this pull request. Please add your review or reassign. It has been 14 days with no activity and the awaiting review label has been applied.

```
Author:
```
rthadur
```
Text:
```

@Dayananda-V please check failed tests

```
Author:
```
tanzhenyu
```
Text:
```

This is been failing unit test -- can you investigate?

```
Author:
```
Dayananda-V
```
Text:
```

@tanzhenyu
fixed compilation problem and please review once again, TIA!......

```

