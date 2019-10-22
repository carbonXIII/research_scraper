# tensorflow/tensorflow
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_tensorflow_lite_g3doc_guide_ios_md](#_tensorflow_lite_g3doc_guide_ios_md)

* [_tensorflow_lite_experimental_micro_examples_micro_speech_CMSIS_README_md](#_tensorflow_lite_experimental_micro_examples_micro_speech_CMSIS_README_md)

* [_tensorflow_core_distributed_runtime_README_md](#_tensorflow_core_distributed_runtime_README_md)

* [_tensorflow_compiler_mlir_lite_README_md](#_tensorflow_compiler_mlir_lite_README_md)

* [_tensorflow_lite_g3doc_convert_rnn_md](#_tensorflow_lite_g3doc_convert_rnn_md)

* [_tensorflow_examples_tutorials_deepdream_README_md](#_tensorflow_examples_tutorials_deepdream_README_md)

* [_tensorflow_compiler_xla_service_g3doc_hlo_parser_md](#_tensorflow_compiler_xla_service_g3doc_hlo_parser_md)

* [_tensorflow_lite_tools_evaluation_tasks_imagenet_image_classification_README_md](#_tensorflow_lite_tools_evaluation_tasks_imagenet_image_classification_README_md)

* [_github_ISSUE_TEMPLATE_10_build_installation_issue_md](#_github_ISSUE_TEMPLATE_10_build_installation_issue_md)

* [_tensorflow_lite_g3doc_guide_build_rpi_md](#_tensorflow_lite_g3doc_guide_build_rpi_md)

* [_tensorflow_python_autograph_g3doc_reference_common_errors_md](#_tensorflow_python_autograph_g3doc_reference_common_errors_md)

* [_tensorflow_lite_g3doc_r1_convert_cmdline_reference_md](#_tensorflow_lite_g3doc_r1_convert_cmdline_reference_md)

* [_tensorflow_tools_benchmark_README_md](#_tensorflow_tools_benchmark_README_md)

* [_tensorflow_lite_g3doc_guide_get_started_md](#_tensorflow_lite_g3doc_guide_get_started_md)

* [_tensorflow_compiler_xla_g3doc_tfcompile_md](#_tensorflow_compiler_xla_g3doc_tfcompile_md)

* [_tensorflow_python_autograph_g3doc_reference_error_handling_md](#_tensorflow_python_autograph_g3doc_reference_error_handling_md)

* [_tensorflow_python_autograph_STYLE_GUIDE_md](#_tensorflow_python_autograph_STYLE_GUIDE_md)

* [_tensorflow_python_autograph_g3doc_reference_control_flow_md](#_tensorflow_python_autograph_g3doc_reference_control_flow_md)

* [_tensorflow_lite_nnapi_README_md](#_tensorflow_lite_nnapi_README_md)

* [_tensorflow_tools_dockerfiles_readme_for_jupyter_md](#_tensorflow_tools_dockerfiles_readme_for_jupyter_md)

* [_README_md](#_README_md)

[- Inline](#Inline)

* [_third_party_mlir_lib_Transforms_SimplifyAffineStructures_cpp](#_third_party_mlir_lib_Transforms_SimplifyAffineStructures_cpp)

* [_tensorflow_lite_testing_op_tests_constant_py](#_tensorflow_lite_testing_op_tests_constant_py)

* [_tensorflow_python_distribute_multi_worker_test_base_py](#_tensorflow_python_distribute_multi_worker_test_base_py)

* [_tensorflow_python_eager_test_py](#_tensorflow_python_eager_test_py)

* [_tensorflow_python_data_experimental_kernel_tests_optimization_choose_fastest_dataset_test_py](#_tensorflow_python_data_experimental_kernel_tests_optimization_choose_fastest_dataset_test_py)

* [_tensorflow_python_data_kernel_tests_test_base_py](#_tensorflow_python_data_kernel_tests_test_base_py)

* [_tensorflow_examples_speech_commands_label_wav_test_py](#_tensorflow_examples_speech_commands_label_wav_test_py)

* [_tensorflow_python_kernel_tests_random_multinomial_op_test_py](#_tensorflow_python_kernel_tests_random_multinomial_op_test_py)

* [_tensorflow_compiler_tests_lrn_ops_test_py](#_tensorflow_compiler_tests_lrn_ops_test_py)

* [_tensorflow_python_feature_column_feature_column_v2_test_py](#_tensorflow_python_feature_column_feature_column_v2_test_py)

* [_tensorflow_tools_ci_build_release_ubuntu_16_cpu_py2_full_nightly_release_sh](#_tensorflow_tools_ci_build_release_ubuntu_16_cpu_py2_full_nightly_release_sh)

* [_tensorflow_python_autograph_lang_special_functions_test_py](#_tensorflow_python_autograph_lang_special_functions_test_py)

* [_tensorflow_python_ops_ragged_ragged_const_op_test_py](#_tensorflow_python_ops_ragged_ragged_const_op_test_py)

* [_tensorflow_python_distribute_multi_process_runner_test_py](#_tensorflow_python_distribute_multi_process_runner_test_py)

* [_tensorflow_lite_experimental_micro_examples_micro_speech_apollo3_compare_1k_py](#_tensorflow_lite_experimental_micro_examples_micro_speech_apollo3_compare_1k_py)

* [_tensorflow_python_training_tracking_benchmarks_test_py](#_tensorflow_python_training_tracking_benchmarks_test_py)

* [_tensorflow_tools_ci_build_devtoolset_rpm_patch_sh](#_tensorflow_tools_ci_build_devtoolset_rpm_patch_sh)

* [_tensorflow_python_distribute_cluster_resolver_gce_cluster_resolver_test_py](#_tensorflow_python_distribute_cluster_resolver_gce_cluster_resolver_test_py)

* [_third_party_mlir_lib_Transforms_LoopFusion_cpp](#_third_party_mlir_lib_Transforms_LoopFusion_cpp)

* [_tensorflow_python_framework_composite_tensor_test_py](#_tensorflow_python_framework_composite_tensor_test_py)

[- Issues](#Issues)

* [27789](#27789)

* [15238](#15238)

* [17910](#17910)

* [5250](#5250)

* [20092](#20092)

* [548](#548)

* [7621](#7621)

* [30874](#30874)

* [842](#842)

* [23290](#23290)

* [13090](#13090)

* [7684](#7684)

* [18980](#18980)

* [2286](#2286)

[- Pull](#Pull)

* [9510](#9510)

* [3398](#3398)

* [27359](#27359)

* [6051](#6051)

* [17005](#17005)

* [15787](#15787)

<!-- toc -->

# Info
## description
An Open Source Machine Learning Framework for Everyone

# Markdown
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
## _tensorflow_lite_experimental_micro_examples_micro_speech_CMSIS_README_md
```# Description of files

*   **create_constants.py**: Python file used to create hanning.cc, hanning.h,
    sin_1k.cc, and sin_1k.h
*   **hanning.cc**: Precomputed
    [Hann window](https://en.wikipedia.org/wiki/Hann_function) for use in the
    preprocessor. This file is created in ../create_constants.py
*   **hanning.h**: Header file for hanning.cc
*   **preprocessor.cc**: CMSIS version of the preprocessor
*   **sin_1k.cc**: A 1 kHZ sinusoid used for comparing the CMSIS preprocessor
    with the Micro-Lite fixed_point preprocessor
*   **sin_1k.h**: Header file for sin_1k.cc

# Description of externally downloaded files in ../CMSIS_ext

*   **arm_cmplx_mag_squared_q10p6.c**: Modified version of the ARM CMSIS
    function
    [arm_cmplx_mag_squared.c](http://arm-software.github.io/CMSIS_5/DSP/html/group__cmplx__mag__squared.html#ga45537f576102d960d467eb722b8431f2).
    The modification is that we have changed the amount of right-shift to make
    sure our data is in the correct range. We redistribute because the original
    content was created with the Apache 2.0 license.
*   **arm_cmplx_mag_squared_q10p6.h**: Header file for
    arm_cmplx_mag_squared_q10p6.c
```
## _tensorflow_core_distributed_runtime_README_md
```# Distributed TensorFlow

This directory contains the initial open-source implementation of the
distributed TensorFlow runtime, using [gRPC](http://grpc.io) for inter-process
communication.

To learn how to use the distributed runtime to create a TensorFlow cluster,
see the [Distributed TensorFlow](https://www.tensorflow.org/deploy/distributed) How-To.
```
## _tensorflow_compiler_mlir_lite_README_md
```# Experimental code for the new TF-Lite convertor, and MLIR dialects and utilities for TensorFlow Lite.

This directory contains:

1. Experimental code for the new TF-Lite convertor.
2. Code for the TF-lite dialect [MLIR](https://github.com/tensorflow/mlir).

## API:

The API for converting TensorFlow models to TensorFlow Lite will be through
`tf.lite.TFLiteConverter`. All the conversion code is open sourced, and
the API will be integrated soon.

### The conversion process from TensorFlow to TensorFlow Lite includes the following major passes:

- Import from GraphDef, in .pb or .pbtxt  format, into MLIR.
- Raise to Control-flow-graph. Converts TF Control Flow dialect to TF dialect.
- The Canonicalization pass iteratively applies canonicalization
transformations in a greedy way until no further changes occur.
Canonicalization includes constant folding.
- The Legalize pass converts TensorFlow operations to TensorFlow Lite
ones. The operations that cannot be mapped to TensorFlow Lite dialect
are left as TensorFlow operations. Unsupported op handling follows the
proposed TFLite mechanism.
- Optimizations are performed in both the TF & TFLite dialect; aiming for small
size and high performance (among the core value proposition of
TensorFlow Lite models).
- The Export pass writes out TensorFlow Lite FlatBuffer format. This pass
operates on MLIR TensorFlow Lite dialect and is simple/direct translation.

```
## _tensorflow_lite_g3doc_convert_rnn_md
```# Convert RNN models

The TensorFlow Lite interpreter currently implements a subset of TensorFlow
operations, meaning some model architectures cannot immediately be converted due
to missing operations.

Some RNN-based architectures are affected by this. The following document
outlines the current state of play and provides strategies for converting RNN
models.

## Currently supported

Currently, RNN models using
[`tf.compat.v1.nn.static_rnn`](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn)
can be converted successfully as long as no `sequence_length` is specified.

The following `tf.compat.v1.nn.rnn_cell` operations work with
`tf.compat.v1.nn.static_rnn`:

*   [tf.compat.v1.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)
*   [tf.compat.v1.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.compat.v1.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell)
*   [tf.compat.v1.nn.rnn_cell.BasicLSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicLSTMCell)
*   [tf.compat.v1.nn.rnn_cell.BasicRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicRNNCell)

In addition, TensorFlow Lite provides some experimental drop-in replacements for
RNN operations that enable dynamic RNN architectures with TensorFlow Lite.

Drop-in replacements are available for the following:

*   [tf.compat.v1.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.compat.v1.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)
*   [tf.compat.v1.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.compat.v1.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)

## Not currently supported

TensorFlow Lite does not currently support
[Control Flow](https://www.tensorflow.org/api_docs/cc/group/control-flow-ops)
operations. This means that, unless one of the conversion strategies discussed
in the next section are employed, models built with the following TensorFlow
functions will not convert successfully:

*   [tf.compat.v1.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn)
    where a `sequence_length` is specified
*   [tf.compat.v1.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.compat.v1.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)

Note: TensorFlow Lite plans to implement all required Control Flow operations by
the end of 2019. At this point, all RNN architectures will convert successfully.

## Conversion strategies

To convert an RNN model that uses the functions specified above, you will have
to modify its architecture and retrain it. The following strategies can be used.

### 1. Refactoring

The simplest approach, if possible, is to refactor the model architecture to use
[tf.compat.v1.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn)
without `sequence_length`.

### 2. Drop-in replacements that use op hints and fused ops

TensorFlow Lite provides the some experimental drop-in replacements for RNN
operations that enable dynamic RNN architectures with TensorFlow Lite. Using
[OpHints](https://www.tensorflow.org/lite/guide/ops_custom#converting_tensorflow_models_to_convert_graphs),
they run normally during training, but are substituted with special fused ops
when run by the Lite interpreter.

The following drop-in replacements are available:

*   [tf.compat.v1.lite.experimental.nn.dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L41)
    *   replacement for tf.nn.dynamic_rnn
*   [tf.compat.v1.lite.experimental.nn.bidirectional_dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L279)
    *   replacement for tf.nn.bidirectional_dynamic_rnn
*   [tf.compat.v1.lite.experimental.nn.TfLiteRNNCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L39)
    *   replacement for tf.nn.rnn_cell.RNNCell
*   [tf.compat.v1.lite.experimental.nn.TfLiteLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L159)
    *   replacement for tf.nn.rnn_cell.LSTMCell

Note: These replacements must be used together. For example, if you are using
`tf.compat.v1.lite.experimental.nn.dynamic_rnn`, you must combine it with
`tf.compat.v1.lite.experimental.nn.TfLiteRNNCell` instead of using
`tf.compat.v1.nn.rnn_cell.RNNCell`.

Instead of
[tf.compat.v1.nn.rnn_cell.MultiRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/MultiRNNCell),
you should use
[tf.compat.v1.keras.layers.StackedRNNCells](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells).

For a tutorial on using these replacements, see
[TensorFlow Lite LSTM ops API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/g3doc/README.md).

For a Colab demonstrating these classes, refer to
[TensorFlowLite_LSTM_Keras_Tutorial](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/TensorFlowLite_LSTM_Keras_Tutorial.ipynb).

Note: There is no replacement available for
[tf.compat.v1.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell).
```
## _tensorflow_examples_tutorials_deepdream_README_md
```# Deepdream

This example has moved.

[A TensorFlow 2 version is available](https://tensorflow.org/tutorials/generative/deepdream)
[The original is in the TensorFlow examples Repository](https://github.com/tensorflow/examples/tree/master/community/en/r1/deepdream.ipynb)
```
## _tensorflow_compiler_xla_service_g3doc_hlo_parser_md
```# HLO Text Syntax

'''yacc
hlo_module
  : 'HloModule' name computations
  ;

/* If no computation is marked as ENTRY, the last computation will be the entry
computation of the module.*/
computations
  : computation
  | computation computations
  ;

computation
  : 'ENTRY' name param_list_to_shape instruction_list
  | name param_list_to_shape instruction_list
  | 'ENTRY' name instruction_list
  | name instruction_list
  ;

/* If no instruction is marked as ROOT, the last instruction will be the root of
its computation. */
instruction_list
  : '{' instruction_list1 '}'
  ;
instruction_list1
  : instruction
  | instruction_list1 instruction
  ;
instruction
  : 'ROOT' name '=' shape opcode operands extra_attributes
  | name '=' shape opcode operands extra_attributes
  ;

operands
  : '(' operands1 ')'
  ;
operands1
  : /*empty*/
  | operand
  | operands1 ',' operand
  ;
operand
  : shape name
  | name
  ;

attributes
  : /*empty*/
  | ',' attribute
  | ',' attribute attributes
  ;
attribute
  : attribute_name attribute_value
  ;
attribute_value
  : kInt
  | kName
  | [0-9bf]{2,}_[0-9io]{2,}->[0-9bf]{2,}                /*dim_labels_pattern*/
  | [0-9]+(x[0-9]+)+                                    /*dxd_pattern*/
  | [0-9]+_[0-9]+(_[0-9]+)?(x[0-9]+_[0-9]+(_[0-9]+)?)*  /*pad_pattern*/
  | '{' sub_attributes '}'
  ;

param_list_to_shape
  : param_list '->' shape
  ;

param_list
  : '(' param_list1 ')'
  ;
param_list1
  : /*empty*/
  | param
  | param_list1 ',' param
  ;
param
  : name shape
  ;

shape
  : shape_val_
  | '(' tuple_elements ')'
  ;
tuple_elements
  : /*empty*/
  | shape (',' shape)*
  ;

name
  : identifier ':'
  | '%' identifier
  | identifier
  ;

identifier
  : [a-zA-Z_][a-zA-Z0-9_.-]*
  ;

/* literal is in the right hand side of a constant instruction. */
literal
  : tuple
  | non_tuple
  ;
tuple
  : shape '(' literal_list ')'
  ;
literal_list
  : /*empty*/
  : literal
  | literal_list ',' literal
  ;
non_tuple
  : rank01
  | rank2345
  ;
rank2345
  : shape sparse_or_nested_array
  ;
sparse_or_nested_array
  : sparse_array
  | nested_array
  ;
sparse_array
  : '{' sparse_array1 '}'
  ;
sparse_array1
  : sparse_array_item
  | sparse_array1 ',' sparse_array_item
  ;
sparse_array_item
  : multi_index ':' scalar
  ;
multi_index
  : kInt
  | '[' multi_index1 ']'
  ;
multi_index1
  : kInt
  | multi_index1 ',' kInt
  ;

'''
```
## _tensorflow_lite_tools_evaluation_tasks_imagenet_image_classification_README_md
```## Image Classification evaluation based on ILSVRC 2012 task

This binary evaluates the following parameters of TFLite models trained for the
[ILSVRC 2012 image classification task](http://www.image-net.org/challenges/LSVRC/2012/):

*   Native pre-processing latency
*   Inference latency
*   Top-K (1 to 10) accuracy values

The binary takes the path to validation images and labels as inputs, along with
the model and inference-specific parameters such as delegate and number of
threads. It outputs the metrics as a text proto to a file, similar to the
following:

'''
num_runs: 300 # Total images evaluated
process_metrics {
  image_classification_metrics {
    pre_processing_latency {
      last_us: 8641
      max_us: 42357
      min_us: 2811
      sum_us: 2449340
      avg_us: 8164.4666666666662 # Avg Pre-processing latency in micro-seconds
    }
    inference_latency {
      last_us: 27979
      max_us: 40696
      min_us: 27811
      sum_us: 9142187
      avg_us: 30473.956666666665 # Avg Inference latency in micro-seconds
    }
    inference_metrics {
      num_inferences: 300
    }
    topk_accuracy_metrics {
      topk_accuracies: 0.7033333 # Top-1 accuracy
      topk_accuracies: 0.78
      topk_accuracies: 0.8333333
      topk_accuracies: 0.86
      topk_accuracies: 0.88
      topk_accuracies: 0.89
      topk_accuracies: 0.9033333
      topk_accuracies: 0.9033333
      topk_accuracies: 0.92
      topk_accuracies: 0.9266667 # Top-10 accuracy
    }
  }
}
'''

To run the binary download the ILSVRC 2012 devkit
[see instructions](#downloading-ilsvrc) and run the
[`generate_validation_ground_truth` script](#ground-truth-label-generation) to
generate the ground truth labels.

## Parameters

The binary takes the following parameters:

*   `model_file` : `string` \
    Path to the TFlite model file.

*   `ground_truth_images_path`: `string` \
    The path to the directory containing ground truth images.

*   `ground_truth_labels`: `string` \
    Path to ground truth labels file. This file should contain the same number
    of labels as the number images in the ground truth directory. The labels are
    assumed to be in the same order as the sorted filename of images. See
    [ground truth label generation](#ground-truth-label-generation) section for
    more information about how to generate labels for images.

*   `model_output_labels`: `string` \
    Path to the file containing labels, that is used to interpret the output of
    the model. E.g. in case of mobilenets, this is the path to
    `mobilenet_labels.txt` where each label is in the same order as the output
    1001 dimension tensor.

*   `output_file_path`: `string` \
    The final metrics are dumped into `output_file_path` as a string-serialized
    instance of `tflite::evaluation::EvaluationStageMetrics`.

and the following optional parameters:

*   `blacklist_file_path`: `string` \
    Path to blacklist file. This file contains the indices of images that are
    blacklisted for evaluation. 1762 images are blacklisted in ILSVRC dataset.
    For details please refer to readme.txt of ILSVRC2014 devkit.

*   `num_images`: `int` (default=0) \
    The number of images to process, if 0, all images in the directory are
    processed otherwise only num_images will be processed.

*   `num_threads`: `int` (default=4) \
    The number of threads to use for evaluation. Note: This does not change the
    number of TFLite Interpreter threads, but shards the dataset to speed up
    evaluation.

The following optional parameters can be used to modify the inference runtime:

*   `num_interpreter_threads`: `int` (default=1) \
    This modifies the number of threads used by the TFLite Interpreter for
    inference.

*   `delegate`: `string` \
    If provided, tries to use the specified delegate for accuracy evaluation.
    Valid values: "nnapi", "gpu".

## Downloading ILSVRC

In order to use this tool to run evaluation on the full 50K ImageNet dataset,
download the data set from http://image-net.org/request.

## Ground truth label generation

The ILSVRC 2012 devkit `validation_ground_truth.txt` contains IDs that
correspond to synset of the image. The accuracy binary however expects the
ground truth labels to contain the actual name of category instead of synset
ids. A conversion script has been provided to convert the validation ground
truth to category labels. The `validation_ground_truth.txt` can be converted by
the following steps:

'''
ILSVRC_2012_DEVKIT_DIR=[set to path to ILSVRC 2012 devkit]
VALIDATION_LABELS=[set to  path to output]

python third_party/tensorflow/lite/tools/accuracy/ilsvrc/generate_validation_labels.py \
--ilsvrc_devkit_dir=${ILSVRC_2012_DEVKIT_DIR} \
--validation_labels_output=${VALIDATION_LABELS}
'''

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
  //tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification:run_eval
'''

(2) Connect your phone. Push the binary to your phone with adb push (make the
directory if required):

'''
adb push bazel-bin/third_party/tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification/run_eval /data/local/tmp
'''

(3) Make the binary executable.

'''
adb shell chmod +x /data/local/tmp/run_eval
'''

(4) Push the TFLite model that you need to test. For example:

'''
adb push mobilenet_quant_v1_224.tflite /data/local/tmp
'''

(5) Push the imagenet images to device, make sure device has sufficient storage
available before pushing the dataset:

'''
adb shell mkdir /data/local/tmp/ilsvrc_images && \
adb push ${IMAGENET_IMAGES_DIR} /data/local/tmp/ilsvrc_images
'''

(6) Push the generated validation ground labels to device.

'''
adb push ${VALIDATION_LABELS} /data/local/tmp/ilsvrc_validation_labels.txt
'''

(7) Push the model labels text file to device.

'''
adb push ${MODEL_LABELS_TXT} /data/local/tmp/model_output_labels.txt
'''

(8) Run the binary.

'''
adb shell /data/local/tmp/run_eval \
  --model_file=/data/local/tmp/mobilenet_quant_v1_224.tflite \
  --ground_truth_images_path=/data/local/tmp/ilsvrc_images \
  --ground_truth_labels=/data/local/tmp/ilsvrc_validation_labels.txt \
  --model_output_labels=/data/local/tmp/model_output_labels.txt \
  --output_file_path=/data/local/tmp/accuracy_output.txt \
  --num_images=0 # Run on all images.
'''

### On Desktop

(1) Build and run using the following command:

'''
bazel run -c opt \
  --cxxopt='--std=c++11' \
  -- \
  //tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification:run_eval \
  --model_file=mobilenet_quant_v1_224.tflite \
  --ground_truth_images_path=${IMAGENET_IMAGES_DIR} \
  --ground_truth_labels=${VALIDATION_LABELS} \
  --model_output_labels=${MODEL_LABELS_TXT} \
  --output_file_path=/tmp/accuracy_output.txt \
  --num_images=0 # Run on all images.
'''
```
## _github_ISSUE_TEMPLATE_10_build_installation_issue_md
```---
name: Build/Installation Issue
about: Use this template for build/installation issues

---

<em>Please make sure that this is a build/installation issue. As per our [GitHub Policy](https://github.com/tensorflow/tensorflow/blob/master/ISSUES.md), we only address code/doc bugs, performance issues, feature requests and build/installation issues on GitHub. tag:build_template</em>

**System information**
- OS Platform and Distribution (e.g., Linux Ubuntu 16.04):
- Mobile device (e.g. iPhone 8, Pixel 2, Samsung Galaxy) if the issue happens on mobile device:
- TensorFlow installed from (source or binary):
- TensorFlow version:
- Python version:
- Installed using virtualenv? pip? conda?:
- Bazel version (if compiling from source):
- GCC/Compiler version (if compiling from source):
- CUDA/cuDNN version:
- GPU model and memory:



**Describe the problem**

**Provide the exact sequence of commands / steps that you executed before running into the problem**


**Any other info / logs**
Include any logs or source code that would be helpful to diagnose the problem. If including tracebacks, please include the full traceback. Large logs and files should be attached.
```
## _tensorflow_lite_g3doc_guide_build_rpi_md
```# Build TensorFlow Lite for Raspberry Pi

This page describes how to build the TensorFlow Lite static library for
Raspberry Pi. If you just want to start using TensorFlow Lite to execute your
models, the fastest option is to install the TensorFlow Lite runtime package as
shown in the [Python quickstart](python.md).

Note: This page shows how to compile only the C++ static library for
TensorFlow Lite. Alternative install options include: [install just the Python
interpreter API](python.md) (for inferencing only); [install the full
TensorFlow package from pip](https://www.tensorflow.org/install/pip);
or [build the full TensorFlow package](
https://www.tensorflow.org/install/source_rpi).


## Cross-compile for Raspberry Pi

This has been tested on Ubuntu 16.04.3 64bit and TensorFlow devel docker image
[tensorflow/tensorflow:nightly-devel](https://hub.docker.com/r/tensorflow/tensorflow/tags/).

To cross compile TensorFlow Lite, first install the toolchain and libs:

'''bash
sudo apt-get update
sudo apt-get install crossbuild-essential-armhf
'''

If you are using Docker, you may not use `sudo`.

Now git-clone the TensorFlow repository
(`https://github.com/tensorflow/tensorflow`)—if you're using the TensorFlow
Docker image, the repo is already provided in `/tensorflow_src/`—and then run
this script at the root of the TensorFlow repository to download all the
build dependencies:

'''bash
./tensorflow/lite/tools/make/download_dependencies.sh
'''

Note that you only need to do this once.

You should then be able to compile:

'''bash
./tensorflow/lite/tools/make/build_rpi_lib.sh
'''

This should compile a static library in:
`tensorflow/lite/tools/make/gen/rpi_armv7l/lib/libtensorflow-lite.a`.


## Compile natively on Raspberry Pi

This has been tested on Raspberry Pi 3b, Raspbian GNU/Linux 9.1 (stretch), gcc version 6.3.0 20170516 (Raspbian 6.3.0-18+rpi1).

Log in to your Raspberry Pi and install the toolchain:

'''bash
sudo apt-get install build-essential
'''

Now git-clone the TensorFlow repository
(`https://github.com/tensorflow/tensorflow`) and run this at the root of
the repository:

'''bash
./tensorflow/lite/tools/make/download_dependencies.sh
'''

Note that you only need to do this once.

You should then be able to compile:

'''bash
./tensorflow/lite/tools/make/build_rpi_lib.sh
'''

This should compile a static library in:
`tensorflow/lite/tools/make/gen/lib/rpi_armv7/libtensorflow-lite.a`.
```
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
## _tensorflow_lite_g3doc_r1_convert_cmdline_reference_md
```# Converter command line reference

This page is complete reference of command-line flags used by the TensorFlow
Lite Converter's command line starting from TensorFlow 1.9 up until the most
recent build of TensorFlow.

## High-level flags

The following high level flags specify the details of the input and output
files. The flag `--output_file` is always required. Additionally, either
`--graph_def_file`, `--saved_model_dir` or `--keras_model_file` is required.

*   `--output_file`. Type: string. Specifies the full path of the output file.
*   `--graph_def_file`. Type: string. Specifies the full path of the input
    GraphDef file frozen using
    [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py).
*   `--saved_model_dir`. Type: string. Specifies the full path to the directory
    containing the SavedModel.
*   `--keras_model_file`. Type: string. Specifies the full path of the HDF5 file
    containing the tf.keras model.
*   `--output_format`. Type: string. Default: `TFLITE`. Specifies the format of
    the output file. Allowed values:
    *   `TFLITE`: TensorFlow Lite FlatBuffer format.
    *   `GRAPHVIZ_DOT`: GraphViz `.dot` format containing a visualization of the
        graph after graph transformations.
        *   Note that passing `GRAPHVIZ_DOT` to `--output_format` leads to loss
            of TFLite specific transformations. Therefore, the resulting
            visualization may not reflect the final set of graph
            transformations. To get a final visualization with all graph
            transformations use `--dump_graphviz_dir` instead.

The following flags specify optional parameters when using SavedModels.

*   `--saved_model_tag_set`. Type: string. Default:
    [kSavedModelTagServe](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/cc/saved_model/tag_constants.h).
    Specifies a comma-separated set of tags identifying the MetaGraphDef within
    the SavedModel to analyze. All tags in the tag set must be specified.
*   `--saved_model_signature_key`. Type: string. Default:
    `tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`.
    Specifies the key identifying the SignatureDef containing inputs and
    outputs.

## Model flags

*Model flags* provide additional information about the model stored in the input
file.

*   `--input_arrays`. Type: comma-separated list of strings. Specifies the list
    of names of input activation tensors.
*   `--output_arrays`. Type: comma-separated list of strings. Specifies the list
    of names of output activation tensors.

The following flags define properties of the input tensors. Each item in the
`--input_arrays` flag should correspond to each item in the following flags
based on index.

*   `--input_shapes`. Type: colon-separated list of comma-separated lists of
    integers. Each comma-separated list of integers gives the shape of one of
    the input arrays specified in
    [TensorFlow convention](https://www.tensorflow.org/guide/tensors#shape).
    *   Example: `--input_shapes=1,60,80,3` for a typical vision model means a
        batch size of 1, an input image height of 60, an input image width of
        80, and an input image depth of 3 (representing RGB channels).
    *   Example: `--input_arrays=foo,bar --input_shapes=2,3:4,5,6` means "foo"
        has a shape of [2, 3] and "bar" has a shape of [4, 5, 6].
*   `--std_dev_values`, `--mean_values`. Type: comma-separated list of floats.
    These specify the (de-)quantization parameters of the input array, when it
    is quantized. This is only needed if `inference_input_type` is
    `QUANTIZED_UINT8`.
    *   The meaning of `mean_values` and `std_dev_values` is as follows: each
        quantized value in the quantized input array will be interpreted as a
        mathematical real number (i.e. as an input activation value) according
        to the following formula:
        *   `real_value = (quantized_input_value - mean_value) / std_dev_value`.
    *   When performing float inference (`--inference_type=FLOAT`) on a
        quantized input, the quantized input would be immediately dequantized by
        the inference code according to the above formula, before proceeding
        with float inference.
    *   When performing quantized inference
        (`--inference_type=QUANTIZED_UINT8`), no dequantization is performed by
        the inference code. However, the quantization parameters of all arrays,
        including those of the input arrays as specified by `mean_value` and
        `std_dev_value`, determine the fixed-point multipliers used in the
        quantized inference code. `mean_value` must be an integer when
        performing quantized inference.

## Transformation flags

*Transformation flags* specify options of the transformations to be applied to
the graph, i.e. they specify requested properties that the output file should
have.

*   `--inference_type`. Type: string. Default: `FLOAT`. Data type of all
    real-number arrays in the output file except for input arrays (defined by
    `--inference_input_type`). Must be `{FLOAT, QUANTIZED_UINT8}`.

    This flag only impacts real-number arrays including float and quantized
    arrays. This excludes all other data types including plain integer arrays
    and string arrays. Specifically:

    *   If `FLOAT`, then real-numbers arrays will be of type float in the output
        file. If they were quantized in the input file, then they get
        dequantized.
    *   If `QUANTIZED_UINT8`, then real-numbers arrays will be quantized as
        uint8 in the output file. If they were float in the input file, then
        they get quantized.

*   `--inference_input_type`. Type: string. Data type of a real-number input
    array in the output file. By default the `--inference_type` is used as type
    of all of the input arrays. Flag is primarily intended for generating a
    float-point graph with a quantized input array. A Dequantized operator is
    added immediately after the input array. Must be `{FLOAT, QUANTIZED_UINT8}`.

    The flag is typically used for vision models taking a bitmap as input but
    requiring floating-point inference. For such image models, the uint8 input
    is quantized and the quantization parameters used for such input arrays are
    their `mean_value` and `std_dev_value` parameters.

*   `--default_ranges_min`, `--default_ranges_max`. Type: floating-point.
    Default value for the (min, max) range values used for all arrays without a
    specified range. Allows user to proceed with quantization of non-quantized
    or incorrectly-quantized input files. These flags produce models with low
    accuracy. They are intended for easy experimentation with quantization via
    "dummy quantization".

*   `--drop_control_dependency`. Type: boolean. Default: True. Indicates whether
    to drop control dependencies silently. This is due to TensorFlow Lite not
    supporting control dependencies.

*   `--reorder_across_fake_quant`. Type: boolean. Default: False. Indicates
    whether to reorder FakeQuant nodes in unexpected locations. Used when the
    location of the FakeQuant nodes is preventing graph transformations
    necessary to convert the graph. Results in a graph that differs from the
    quantized training graph, potentially causing differing arithmetic behavior.

*   `--allow_custom_ops`. Type: string. Default: False. Indicates whether to
    allow custom operations. When false, any unknown operation is an error. When
    true, custom ops are created for any op that is unknown. The developer will
    need to provide these to the TensorFlow Lite runtime with a custom resolver.

*   `--post_training_quantize`. Type: boolean. Default: False. Boolean
    indicating whether to quantize the weights of the converted float model.
    Model size will be reduced and there will be latency improvements (at the
    cost of accuracy).

## Logging flags

The following flags generate graph visualizations of the graph as
[GraphViz](https://www.graphviz.org/) `.dot` files at various points during
graph transformations:

*   `--dump_graphviz_dir`. Type: string. Specifies the full path of the
    directory to output GraphViz `.dot` files. Outputs the graph immediately
    after reading in the graph and after all of the transformations have been
    completed.
*   `--dump_graphviz_video`. Type: boolean. Outputs GraphViz after every graph
    transformation. Requires `--dump_graphviz_dir` to be specified.
```
## _tensorflow_tools_benchmark_README_md
```# TensorFlow Model Benchmark Tool

## Description

A simple C++ binary to benchmark a compute graph and its individual operators,
both on desktop machines and on Android.

## To build/install/run

### On Android:

(0) Refer to https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android to edit the `WORKSPACE` to configure the android NDK/SDK.

(1) build for your specific platform, e.g.:
'''
bazel build -c opt \
  --crosstool_top=//external:android/crosstool \
  --cpu=armeabi-v7a \
  --host_crosstool_top=@bazel_tools//tools/cpp:toolchain \
  --config monolithic \
  tensorflow/tools/benchmark:benchmark_model
'''

(2) Connect your phone. Push the binary to your phone with adb push
     (make the directory if required):
'''
adb push bazel-bin/tensorflow/tools/benchmark/benchmark_model /data/local/tmp
'''

(3) Push the compute graph that you need to test. For example:
     adb push tensorflow_inception_graph.pb /data/local/tmp

(4) Run the benchmark. For example:
'''
adb shell /data/local/tmp/benchmark_model \
  --graph=/data/local/tmp/tensorflow_inception_graph.pb \
  --input_layer="input:0" \
  --input_layer_shape="1,224,224,3" \
  --input_layer_type="float" \
  --output_layer="output:0"
'''
### On desktop:
(1) build the binary
'''
bazel build -c opt tensorflow/tools/benchmark:benchmark_model
'''

(2) Run on your compute graph, similar to the Android case but without the need of adb shell.
For example:
'''
bazel-bin/tensorflow/tools/benchmark/benchmark_model \
  --graph=tensorflow_inception_graph.pb \
  --input_layer="input:0" \
  --input_layer_shape="1,224,224,3" \
  --input_layer_type="float" \
  --output_layer="output:0"
'''

The Inception graph used as an example here may be downloaded from
https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip
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
## _tensorflow_compiler_xla_g3doc_tfcompile_md
```# Using AOT compilation

## What is tfcompile?

`tfcompile` is a standalone tool that ahead-of-time (AOT) compiles TensorFlow
graphs into executable code. It can reduce total binary size, and also avoid
some runtime overheads. A typical use-case of `tfcompile` is to compile an
inference graph into executable code for mobile devices.

The TensorFlow graph is normally executed by the TensorFlow runtime. This incurs
some runtime overhead for execution of each node in the graph. This also leads
to a larger total binary size, since the code for the TensorFlow runtime needs
to be available, in addition to the graph itself. The executable code produced
by `tfcompile` does not use the TensorFlow runtime, and only has dependencies on
kernels that are actually used in the computation.

The compiler is built on top of the XLA framework. The code bridging TensorFlow
to the XLA framework resides under
[tensorflow/compiler](https://www.tensorflow.org/code/tensorflow/compiler/).

## What does tfcompile do?

`tfcompile` takes a subgraph, identified by the TensorFlow concepts of
feeds and fetches, and generates a function that implements that subgraph.
The `feeds` are the input arguments for the function, and the `fetches` are the
output arguments for the function. All inputs must be fully specified by the
feeds; the resulting pruned subgraph cannot contain Placeholder or Variable
nodes. It is common to specify all Placeholders and Variables as feeds, which
ensures the resulting subgraph no longer contains these nodes. The generated
function is packaged as a `cc_library`, with a header file exporting the
function signature, and an object file containing the implementation. The user
writes code to invoke the generated function as appropriate.

## Using tfcompile

This section details high level steps for generating an executable binary with
`tfcompile` from a TensorFlow subgraph. The steps are:

*   Step 1: Configure the subgraph to compile
*   Step 2: Use the `tf_library` build macro to compile the subgraph
*   Step 3: Write code to invoke the subgraph
*   Step 4: Create the final binary

### Step 1: Configure the subgraph to compile

Identify the feeds and fetches that correspond to the input and output
arguments for the generated function. Then configure the `feeds` and `fetches`
in a [`tensorflow.tf2xla.Config`](https://www.tensorflow.org/code/tensorflow/compiler/tf2xla/tf2xla.proto)
proto.

'''textproto
# Each feed is a positional input argument for the generated function.  The order
# of each entry matches the order of each input argument.  Here “x_hold” and “y_hold”
# refer to the names of placeholder nodes defined in the graph.
feed {
  id { node_name: "x_hold" }
  shape {
    dim { size: 2 }
    dim { size: 3 }
  }
}
feed {
  id { node_name: "y_hold" }
  shape {
    dim { size: 3 }
    dim { size: 2 }
  }
}

# Each fetch is a positional output argument for the generated function.  The order
# of each entry matches the order of each output argument.  Here “x_y_prod”
# refers to the name of a matmul node defined in the graph.
fetch {
  id { node_name: "x_y_prod" }
}
'''

### Step 2: Use tf_library build macro to compile the subgraph

This step converts the graph into a `cc_library` using the `tf_library` build
macro. The `cc_library` consists of an object file containing the code generated
from the graph, along with a header file that gives access to the generated
code. `tf_library` utilizes `tfcompile` to compile the TensorFlow graph into
executable code.

'''build
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# Use the tf_library macro to compile your graph into executable code.
tf_library(
    # name is used to generate the following underlying build rules:
    # <name>           : cc_library packaging the generated header and object files
    # <name>_test      : cc_test containing a simple test and benchmark
    # <name>_benchmark : cc_binary containing a stand-alone benchmark with minimal deps;
    #                    can be run on a mobile device
    name = "test_graph_tfmatmul",
    # cpp_class specifies the name of the generated C++ class, with namespaces allowed.
    # The class will be generated in the given namespace(s), or if no namespaces are
    # given, within the global namespace.
    cpp_class = "foo::bar::MatMulComp",
    # graph is the input GraphDef proto, by default expected in binary format.  To
    # use the text format instead, just use the ‘.pbtxt’ suffix.  A subgraph will be
    # created from this input graph, with feeds as inputs and fetches as outputs.
    # No Placeholder or Variable ops may exist in this subgraph.
    graph = "test_graph_tfmatmul.pb",
    # config is the input Config proto, by default expected in binary format.  To
    # use the text format instead, use the ‘.pbtxt’ suffix.  This is where the
    # feeds and fetches were specified above, in the previous step.
    config = "test_graph_tfmatmul.config.pbtxt",
)
'''

> To generate the GraphDef proto (test_graph_tfmatmul.pb) for this example, run
> [make_test_graphs.py](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/make_test_graphs.py)
> and specify the output location with the --out_dir flag.

Typical graphs contain [`Variables`](https://www.tensorflow.org/guide/variables)
representing the weights that are learned via training, but `tfcompile` cannot
compile a subgraph that contain `Variables`. The
[freeze_graph.py](https://www.tensorflow.org/code/tensorflow/python/tools/freeze_graph.py)
tool converts variables into constants, using values stored in a checkpoint
file. As a convenience, the `tf_library` macro supports the `freeze_checkpoint`
argument, which runs the tool. For more examples see
[tensorflow/compiler/aot/tests/BUILD](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/BUILD).

> Constants that show up in the compiled subgraph are compiled directly into the
> generated code. To pass the constants into the generated function, rather than
> having them compiled-in, simply pass them in as feeds.

For details on the `tf_library` build macro, see
[tfcompile.bzl](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile.bzl).

For details on the underlying `tfcompile` tool, see
[tfcompile_main.cc](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile_main.cc).

### Step 3: Write code to invoke the subgraph

This step uses the header file (`test_graph_tfmatmul.h`) generated by the
`tf_library` build macro in the previous step to invoke the generated code. The
header file is located in the `bazel-genfiles` directory corresponding to the
build package, and is named based on the name attribute set on the `tf_library`
build macro. For example, the header generated for `test_graph_tfmatmul` would
be `test_graph_tfmatmul.h`. Below is an abbreviated version of what is
generated. The generated file, in `bazel-genfiles`, contains additional useful
comments.

'''c++
namespace foo {
namespace bar {

// MatMulComp represents a computation previously specified in a
// TensorFlow graph, now compiled into executable code.
class MatMulComp {
 public:
  // AllocMode controls the buffer allocation mode.
  enum class AllocMode {
    ARGS_RESULTS_AND_TEMPS,  // Allocate arg, result and temp buffers
    RESULTS_AND_TEMPS_ONLY,  // Only allocate result and temp buffers
  };

  MatMulComp(AllocMode mode = AllocMode::ARGS_RESULTS_AND_TEMPS);
  ~MatMulComp();

  // Runs the computation, with inputs read from arg buffers, and outputs
  // written to result buffers. Returns true on success and false on failure.
  bool Run();

  // Arg methods for managing input buffers. Buffers are in row-major order.
  // There is a set of methods for each positional argument.
  void** args();

  void set_arg0_data(float* data);
  float* arg0_data();
  float& arg0(size_t dim0, size_t dim1);

  void set_arg1_data(float* data);
  float* arg1_data();
  float& arg1(size_t dim0, size_t dim1);

  // Result methods for managing output buffers. Buffers are in row-major order.
  // Must only be called after a successful Run call. There is a set of methods
  // for each positional result.
  void** results();


  float* result0_data();
  float& result0(size_t dim0, size_t dim1);
};

}  // end namespace bar
}  // end namespace foo
'''

The generated C++ class is called `MatMulComp` in the `foo::bar` namespace,
because that was the `cpp_class` specified in the `tf_library` macro. All
generated classes have a similar API, with the only difference being the methods
to handle arg and result buffers. Those methods differ based on the number and
types of the buffers, which were specified by the `feed` and `fetch` arguments
to the `tf_library` macro.

There are three types of buffers managed within the generated class: `args`
representing the inputs, `results` representing the outputs, and `temps`
representing temporary buffers used internally to perform the computation. By
default, each instance of the generated class allocates and manages all of these
buffers for you. The `AllocMode` constructor argument may be used to change this
behavior. All buffers are aligned to 64-byte boundaries.

The generated C++ class is just a wrapper around the low-level code generated by
XLA.

Example of invoking the generated function based on
[`tfcompile_test.cc`](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/tfcompile_test.cc):

'''c++
#define EIGEN_USE_THREADS
#define EIGEN_USE_CUSTOM_THREAD_POOL

#include <iostream>
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/compiler/aot/tests/test_graph_tfmatmul.h" // generated

int main(int argc, char** argv) {
  Eigen::ThreadPool tp(2);  // Size the thread pool as appropriate.
  Eigen::ThreadPoolDevice device(&tp, tp.NumThreads());


  foo::bar::MatMulComp matmul;
  matmul.set_thread_pool(&device);

  // Set up args and run the computation.
  const float args[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
  std::copy(args + 0, args + 6, matmul.arg0_data());
  std::copy(args + 6, args + 12, matmul.arg1_data());
  matmul.Run();

  // Check result
  if (matmul.result0(0, 0) == 58) {
    std::cout << "Success" << std::endl;
  } else {
    std::cout << "Failed. Expected value 58 at 0,0. Got:"
              << matmul.result0(0, 0) << std::endl;
  }

  return 0;
}
'''

### Step 4: Create the final binary

This step combines the library generated by `tf_library` in step 2 and the code
written in step 3 to create a final binary. Below is an example `bazel` BUILD
file.

'''build
# Example of linking your binary
# Also see //tensorflow/compiler/aot/tests/BUILD
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# The same tf_library call from step 2 above.
tf_library(
    name = "test_graph_tfmatmul",
    ...
)

# The executable code generated by tf_library can then be linked into your code.
cc_binary(
    name = "my_binary",
    srcs = [
        "my_code.cc",  # include test_graph_tfmatmul.h to access the generated header
    ],
    deps = [
        ":test_graph_tfmatmul",  # link in the generated object file
        "//third_party/eigen3",
    ],
    linkopts = [
          "-lpthread",
    ]
)
'''
```
## _tensorflow_python_autograph_g3doc_reference_error_handling_md
```# AutoGraph reference

[Index](index.md)

## Error handling

When an exception occurs in code generated by AutoGraph, the error message
is augmented with information about the location in the original code,
before conversion.

When an error occurs in a TensorFlow graph constructed using AutoGraph code,
the stack trace which points to where the failing op was created is modified
to point to the original code, before conversion.

### Python execution errors

Python execution (or tracing) exceptions that are raised in AutoGraph code are
caught and re-raised with an extended error message that contains references
to the original code.

These functions are re-raised by `@tf.function`. If you use a `try/catch` the
exception inside `tf.function`, you will obtain the original exception.

The exception traceback still contains the entire call stack, including frames
corresponding to generated code.

AutoGraph tries to re-raise an exception of the same type as the original
exception. This is usually possible for subclasses of
`Exception` that do not define a custom `__init__`. For more complex
exception types which define a custom constructor, AutoGraph raises a
`StagingError` instead.

Among the distinctive features of the re-raised exception:

 * the exception traceback indicates the call stack of the exception, up to the
   first @tf.function
 * the error message includes references to the original code within
   the `@tf.function`
 * the references corresponding to converted code are marked with an
   asterisk (`*`)

For example, the code below triggers an exception in the Python runtime, at
graph construction time:

'''
@tf.function
def f():
  tf.constant(1) + tf.constant(1.0)
f()
'''

An excerpt of the exception that is raised is shown below:

'''
Traceback (most recent call last):
  File "<ipython-input-10-1938a51c970d>", line 11, in <module>
    f()
  File "tensorflow/python/eager/def_function.py", line 417, in __call__
    self._initialize(args, kwds, add_initializers_to=initializer_map)
  ... more TensorFlow internal frames ...
TypeError: in converted code:

    <ipython-input-9-002fa22f79df>:8 f  *
        tf.constant(1) + tf.constant(1.0)
    tensorflow/python/ops/math_ops.py:900 binary_op_wrapper
        return func(x, y, name=name)
    ... more TensorFlow internal frames ...

    TypeError: Input 'y' of 'AddV2' Op has type float32 that does not match type int32 of argument 'x'.

'''

Note: the exact appearance of the various parts in the error message may change
in the future.

Let's look at the individual components of this exception.

The traceback of the exception indicates the location until the call to
`@tf.function`, including any frames internal to TensorFlow:

'''
Traceback (most recent call last):
  File "<ipython-input-10-1938a51c970d>", line 11, in <module>
    f()
  File "tensorflow/python/eager/def_function.py", line 417, in __call__
    self._initialize(args, kwds, add_initializers_to=initializer_map)
  File "tensorflow/python/eager/def_function.py", line 360, in _initialize
    *args, **kwds))
  File "tensorflow/python/eager/function.py", line 1688, in _get_concrete_function_internal_garbage_collected
    graph_function, _, _ = self._maybe_define_function(args, kwargs)
  File "tensorflow/python/eager/function.py", line 1992, in _maybe_define_function
    graph_function = self._create_graph_function(args, kwargs)
  File "tensorflow/python/eager/function.py", line 1878, in _create_graph_function
    capture_by_value=self._capture_by_value),
  File "tensorflow/python/framework/func_graph.py", line 791, in func_graph_from_py_func
    func_outputs = python_func(*func_args, **func_kwargs)
  File "tensorflow/python/eager/def_function.py", line 310, in wrapped_fn
    return weak_wrapped_fn().__wrapped__(*args, **kwds)
  File "tensorflow/python/framework/func_graph.py", line 781, in wrapper
    raise e.ag_error_metadata.to_exception(type(e))
'''

The exception message includes the location inside the converted function `f`:

'''
TypeError: in converted code:

    <ipython-input-9-002fa22f79df>:8 f  *
        tf.constant(1) + tf.constant(1.0)
    tensorflow/python/ops/math_ops.py:900 binary_op_wrapper
        return func(x, y, name=name)
    tensorflow/python/ops/math_ops.py:1198 _add_dispatch
        return gen_math_ops.add_v2(x, y, name=name)
    tensorflow/python/ops/gen_math_ops.py:549 add_v2
        "AddV2", x=x, y=y, name=name)
    tensorflow/python/framework/op_def_library.py:564 _apply_op_helper
        inferred_from[input_arg.type_attr]))
'''

Notice the frame corresponding to the call of `f`. The function is converted,
which is being indicated by the asterisk `*` character displayed next to
`f`:

'''
    <ipython-input-9-002fa22f79df>:8 f  *
        tf.constant(1) + tf.constant(1.0)
'''

Lastly, the lower part includes the message that the exception originally
reported:

'''
    TypeError: Input 'y' of 'AddV2' Op has type float32 that does not match type int32 of argument 'x'.
'''

Note: Typically, error messages raised by code internal to TensorFlow refers
to arguments of the internal API that failed. Error messages raised by code
internal to AutoGraph (that is, 'tensorflow/python/autograph') usually
refer to symbols used in your code.

### TensorFlow execution errors

TensorFlow execution errors are displayed normally, but the portions of the
error message which correspond to user code contain references to the original
code.

For example, the code below triggers an error in the TensorFlow runtime, at
graph execution time:

'''
@tf.function
def my_function():
  tf.Assert(tf.random.uniform(()) > 1.0, ['example error'])
my_function()
'''

An excerpt of the exception that is subsequently raised is shown below:

'''
Traceback (most recent call last):
  File "<ipython-input-16-af656fb445f0>", line 11, in <module>
    my_function()
  File "tensorflow/python/eager/def_function.py", line 435, in __call__
    return self._concrete_stateful_fn._filtered_call(canon_args, canon_kwds)
  File "tensorflow/python/eager/function.py", line 636, in _filtered_call
    self.captured_inputs)
  File "tensorflow/python/eager/function.py", line 734, in _call_flat
    outputs = self._inference_function.call(ctx, args)
  File "tensorflow/python/eager/function.py", line 460, in call
    ctx=ctx)
  File "tensorflow/python/eager/execute.py", line 68, in quick_execute
    six.raise_from(core._status_to_exception(e.code, message), None)
  File "<string>", line 3, in raise_from
InvalidArgumentError:  assertion failed: [example error]
    [[node Assert/Assert (defined at <ipython-input-16-af656fb445f0>:8) ]] [Op:__inference_my_function_79]
'''

Notice the error message containing references to the location where the failing
op was defined in the code (`<ipython-input-16-af656fb445f0>:8`):

'''
InvalidArgumentError:  assertion failed: [example error]
    [[node Assert/Assert (defined at <ipython-input-16-af656fb445f0>:8) ]] [Op:__inference_my_function_79]
'''

### AutoGraph conversion exceptions

Within `@tf.function`, when AutoGraph fails to convert a function, it displays
a warning message and attempts to run the function without conversion.

For example, the code below make a call to a Python
[generator](https://wiki.python.org/moin/Generators) function, which is not
supported by AutoGraph:

'''
def example_generator():
  yield 1

@tf.function
def f():
  for i in example_generator():
    print(i)
'''

Calling `f()` will still run the code. AutoGraph will convert the function `f`,
but skips the function `example_generator`. In addition, AutoGraph prints a
warning to the console indicating that the function is called without being
converted.

'''
WARNING: Entity <function example_generator at 0x7f951b67f158> appears to be
a generator function. It will not be converted by AutoGraph.
'''
```
## _tensorflow_python_autograph_STYLE_GUIDE_md
```# AutoGraph Style Guide

This page contains style decisions that developers should follow when
contributing code to AutoGraph.

## TensorFlow Style

Follow the [TensorFlow style
guide](https://www.tensorflow.org/community/style_guide), the [documentation
guide](https://www.tensorflow.org/community/documentation) and the
[Google Python style guide](https://google.github.io/styleguide/pyguide.html).

Naming conventions:

1.  The name is TensorFlow, not Tensorflow.
2.  The name is AutoGraph, not Autograph.

## AutoGraph Style

Below are AutoGraph-specific conventions. In the event of conflict,
it supercedes all previous conventions.

1. __Types in docstrings.__ Use [PEP 484][https://www.python.org/dev/peps/pep-0484/]
    notation to describe the type for args, return values and attributes.

    Example:

    '''
    Args:
      foo: Dict[str, List[int]], a dictionary of sorts
    '''

2.  __Citations in Docstrings.__ Write a `#### References` subsection at the
    bottom of any docstring with citations. Use ICLR’s bibliography style to
    write references; for example, order entries by the first author's last
    name. Add a link to the paper if the publication is open source (ideally,
    arXiv).

    Write in-paragraph citations in general, e.g., [(Tran and Blei, 2018)][1].
    Write in-text citations when the citation is a noun, e.g., [Tran and Blei
    (2018)][1]. Write citations with more than two authors using et al., e.g.,
    [(Tran et al., 2018)][1]. Separate multiple citations with semicolon, e.g.,
    ([Tran and Blei, 2018][1]; [Gelman and Rubin, 1992][2]).

    Examples:

    '''none
    #### References

    # technical report
    [1]: Tony Finch. Incremental calculation of weighted mean and variance.
         _Technical Report_, 2009.
         http://people.ds.cam.ac.uk/fanf2/hermes/doc/antiforgery/stats.pdf

    # journal
    [2]: Andrew Gelman and Donald B. Rubin. Inference from Iterative Simulation
         Using Multiple Sequences. _Statistical Science_, 7(4):457-472, 1992.

    # arXiv preprint
    # use "et al." for papers with too many authors to maintain
    [3]: Aaron van den Oord et al. Parallel WaveNet: Fast High-Fidelity Speech
         Synthesis. _arXiv preprint arXiv:1711.10433_, 2017.
         https://arxiv.org/abs/1711.10433

    # conference
    [4]: Yeming Wen, Paul Vicol, Jimmy Ba, Dustin Tran, and Roger Grosse.
         Flipout: Efficient Pseudo-Independent Weight Perturbations on
         Mini-Batches. In _International Conference on Learning
         Representations_, 2018.
         https://arxiv.org/abs/1803.04386
    '''

3.  Avoid LaTeX in docstrings.

    *   It is not rendered in many (if not most) editors and can be hard to read
        for both LaTeX experts and non-experts.

4. Write docstring and comment math using ASCII friendly notation; python using
    operators. E.g., `x**2` better than `x^2`, `x[i, j]` better than `x_{i,j}`,
    `sum{ f(x[i]) : i=1...n }` better than `\sum_{i=1}^n f(x_i)` `int{sin(x) dx:
    x in [0, 2 pi]}` better than `\int_0^{2\pi} sin(x) dx`.

    *   The more we stick to python style, the more someone can
        copy/paste/execute.
    *   Python style is usually easier to read as ASCII.
```
## _tensorflow_python_autograph_g3doc_reference_control_flow_md
```# AutoGraph reference

[Index](index.md)

## Control flow

AutoGraph rewrites all control flow statements with specialized AutoGraph
function calls. These function calls are capable of executing the corresponding
control flow statement using Python semantics for effects outside the Python
interpreter itself (see the [Introduction](intro.md)).

### Dispatch rules

Key Point: Only statements that are conditioned on, or iterate over, a
TensorFlow object such as `tf.Tensor`, are converted into TensorFlow ops.

As described in the [Introduction](intro.md), AutoGraph aims to preserve the
semantics of valid Python code. If a control flow statement runs in graph
execution without raising an error, then AutoGraph will also execute it as
normal Python control flow. Statements which would normally raise an error, for
example because a `tf.Tensor` cannot be used as a `bool` in an `if` statement,
are converted to TensorFlow control flow ops.

#### Analogy with compile-time constants and code optimization

From the perspective of a TensorFlow graph, non-Tensor values, for example an
integer or a NumPy array, are _constants_: they do not change value while the
graph executes.

For example, in the graph below, the condition is always `True` (it is
invariant):

'''
x = 1
y = tf.cond(x > 0, lambda: 3 * x, lambda 5 * x)
'''

That is equivalent to the code below:

'''
x = 1
y = 3 * x
'''

In the example above, we've optimized away the conditional on a constant
condition. The AutoGraph dispatch rules have the same effect: anything that is
not a TensorFlow object is a compile-time constant for TensorFlow, and can be
optimized away. For this reason, you can usually mix Python and TensorFlow
computation and it will transparently have the expected result even
when only some computations are executed in the graph.

<!-- TODO(mdan): This is actually a limitation (a very subtle one) -->
Caution: The assumption of invariant code made above is not true if the
TensorFlow graph had callbacks into the Python code. If you modify data
from within a `tf.py_function`, then the code outside a `tf.py_function`
will have unpredictable behavior if it depends on the same data.

For example, the `tf.cond` that runs as part of the `if` statement below will
miss the update made by `f`:

'''
n = [10]
def f():
  n[0] = 20
  return 0
tf.py_function(f, (), (tf.int32,))
if tf.equal(n[0], 10):
  tf.print('n is 10')
'''

'''
n is 10
'''

### Compound symbols

AutoGraph usually handles basic symbols:

'''
if a < 0:
  a = -a
'''

'''
a = tf.cond(a < 0, lambda: -a, lambda: a)
'''

But it can also handle complex symbols in many cases. For example, if we treat
`a.b` as a symbol in the code below, then we can use it as if it were a basic
symbol name:

'''
if a.b < 0
  a.b = -a.b
'''

'''
a.b = tf.cond(a.b < 0, lambda: -a.b, lambda: a.b)
'''

This is useful in methods, which can operate on properties of `self`, as well as
working directly on more complex object structures or collections.

Caution: There are certain [limitations](limitations.md) around using Python
collections and object mutation. When in doubt, place the values you work
with into local variables and operate on those.

### Effects of the tracing process

#### All Python code paths are executed during tracing

When constructing a graph, TensorFlow _traces_ the code. The tracing of control
flow requires visiting _every possible code path_ (usually once).

Note: In rare cases, the runtime may decide to trace some code paths several
times. For example, the condition of a `while` statement may be executed twice,
first with a temporary graph, to determine whether it evaluates to a
`tf.Tensor`, then if it is a `tf.Tensor`, it's executed a second time in the
proper graph.

In other words, when tracing executes both branches of an if statement.
Similarly, the body of loops is executed once (even if the loop would otherwise
not iterate at all).

This explains why inserting `print` statements in an `if` statement produces
this output:

'''
print('before if')
if tf.constant(True):
  print('true branch')
else:
  print('false branch')
print('after if')
'''

'''
before if
true branch
false branch
after if
'''

Note: Control flow that is not executed as a TensorFlow graph is not traced. Its
body will execute as expected.

Example of code that runs as regular Python code:

'''
print('before if')
if True:  # Condition not a Tensor, running normally
  print('true branch')
else:
  print('false branch')
print('after if')
'''

'''
before if
true branch
after if
'''

#### Python values modified in TensorFlow control flow become Tensors

If a symbol is modified in a TensorFlow control flow statement, then it becomes
a `tf.Tensor`, even if it started off as a Python promitive value.

For example, the conditional below will run as a `tf.cond` (its condition is a
`tf.Tensor`), which in turn will cause `i` to become a `tf.Tensor`.

'''
i = 0
if tf.greater(i, 0):
  i = 1
# i is not a Tensor
'''

### `if` statements

`if` statements whose condition is a `tf.Tensor` are executed as TensorFlow
conditionals by converting them to `tf.cond`:

'''
if tf.random.uniform(()) > 0.5:
  x = 1
else:
  x = 2
'''

`if` statements whose condition is not a `tf.Tensor` are executed as normal
Python:

'''
if np.random.uniform() > 0.5:
  x = 1
else:
  x = 2
'''

`if` statements executed as TensorFlow conditionals are subject to restrictions
(see [limitations](limitations.md)). All symbols affected by the statement and
used thereafter must be:

 * of a data type understood by TensorFlow
 * defined in both branches
 * of consistent dtypes in both branches, for TensorFlow entities
 * of consistent structure in both branches, for static collections (such as
   lists or tuples)

### `while` statements

`while` statements whose condition is a `tf.Tensor` are executed as TensorFlow
loops by converting them to `tf.while_loop`:

'''
x = 0
while tf.random.uniform(()) > 0.5:
  x = x + 1
'''

`while` statements whose condition is not a `tf.Tensor` are executed as normal
Python:

'''
x = 0
while np.random.uniform() > 0.5:
  x = x + 1
'''

`while` statements executed as TensorFlow loops are subject to restrictions
(see [limitations](limitations.md)). All symbols affected by the statement and
used thereafter must be:

 * of a data type understood by TensorFlow
 * defined before the loop
 * of consistent dtype at the beginning and the end of the loop,
   for TensorFlow entities
 * either of consistent shape at the beginning and the end of the loop,
   for TensorFlow entities, or declared in `shape_invariants`
 * of consistent structure  at the beginning and the end of the loop, for
   static collections (such as lists or tuples)

Caution: A `while` loop whose condition is a Python scalar will execute as
normal Python. If you intended to run the loop as a TensorFlow loop, the loop
will replicate its body in the graph (it is unrolled). To avoid that, make sure
its condition is converted to a `tf.Tensor`, using for instance `tf.constant`.

For example, the following loop is unrolled, even though the list contains
`tf.Tensor` values, because the type of `l` is a Python `list`:

'''
l = [tf.constant(1), tf.constant(2), tf.constant(3)]
for i in l:
  tf.print(i)  # This is unrolled - three `tf.print`s are built in the graph. 
'''

If you wish for the loop to run as a TensorFlow loop, stack the loop:

'''
l = [tf.constant(1), tf.constant(2), tf.constant(3)]
for i in tf.stack(l):
  tf.print(i)  # This runs as a TensorFlow loop.
'''

<!-- TODO(mdan): List this under limitations -->
Caution: A loop in which the type of the condition condition changes across
iterations, in a way that would influence the way the loop is executed, is not
allowed in AutoGraph.

For example, the loop below will generate an error. After the first iteration,
`i` becomes a tf.Tensor, because

'''
i = 0
while i < 10:  # `i < 10` is a Python bool - run as normal while loop
  i = tf.constant(1)  # Error -- `i < 10` would now be a `tf.Tensor`
'''

### `for` statements

`for` statements that iterate over a `tf.Tensor` are executed as TensorFlow
loops by converting them to a `tf.while_loop` which iterates over the first
dimension (equivalent to NumPy):

'''
for i in tf.constant(((1, 2), (3, 4))):
  tf.print('iteration:', i)
'''

'''
iteration: [1, 2]
iteration: [3, 4]
'''

Note: If possible, AutoGraph will also set the `maximum_iteration` parameter
of the `tf.while_loop`.

`for` statements that iterate over a the output of a `tf.range` are executed as
TensorFlow loops by converting them to a `tf.while_loop` which uses the
arguments passed to the `tf.range`:

'''
for i in tf.range(3):
  tf.print('iteration:', i)
'''

`for` statements that iterate over a `tf.data.Dataset` and which do not contain
`break` or `return` statements are executed as TensorFlow loops by converting
them to `tf.data.Dataset.reduce` ops:

'''
for i in tf.data.Dataset.range(3):
  tf.print('iteration:', i)
'''

`for` statements that iterate over a _distributed_ `tf.data.Dataset` and which
do not contain `break` or `return` statements are executed as TensorFlow loops
by converting them to the datasets' `reduce` ops:

'''
for i in tf.distribute.OneDeviceStrategy('cpu').experimental_distribute_dataset(
    tf.data.Dataset.range(3)):
  tf.print('iteration:', i)
'''

`for` statements that iterate over a `tf.data.Dataset` and which contain
`break` or `return` statements are executed as TensorFlow loops by converting
them to a combination of `tf.data.Dataset.scan`, `tf.data.Dataset.take_while`
and `tf.data.Dataset.reduce` ops:

'''
for i in tf.data.Dataset.range(3):
  tf.print('iteration:', i)
  break
'''

'''
iteration: 1
'''

`for` statements that iterate over a `tf.data.Dataset` _iterator_ are executed
as TensorFlow loops by converting them to a combination of `tf.while_loop`,
and `tf.cond` ops:

'''
for i in iter(tf.data.Dataset.range(3)):
  tf.print('iteration:', i)
'''

`for` statements that iterate over a type different from any of the above are
executed as normal Python:

'''
for i in [1, 2, 3]:
  print('iteration:', i)
'''

Caution: A `for` loop over a `list` or `tuple` of `tf.Tensor` is considered to
iterate over a Python `list` (or respectively `tuple`), therefore will be
executed as normal Python. If you intended to run it as a TensorFlow loop,
use `tf.stack` or `tf.concat`.

Caution: A `for` loop over a Python `range` will be executed as normal Python.
If you intended to run it as a TensorFlow loop, `tf.range`.

Note: AutoGraph may output a warning when it believes that you are unrolling
a loop inefficiently. However, the warning thresholds are very conservative.

### `break` statements

Code blocks in which `break` statements are used are rewritten with equivalent
code that uses extra control booleans and conditionals. The control booleans are
used directly in `while` loops. In the case of `for` loops, the AutoGraph
corresponding operator accepts an `extra_test` argument which is similar to
the conditional of a while loop, and which contains the control boolean.

For example, the `while` loop below is rewritten as (showing the output of the
`break` transformation only):

'''
while i < 10:
  if i > 3:
    break
  i += 1
'''

'''
break_ = False
while i < 10 and not break_:
  if i > 3:
    break_ = True
    continue  # The continue statement is also rewritten in a subsequent pass
  i += 1
'''

Another example shows how the control boolean is used in the overload of a `for`
loop (showing portions of the final output):

'''
for i in range(10):
  if i > 3:
    break
'''

'''
break_ = False
...
def extra_test(break_):
  return ag__.not_(break_)
# break_ becomes a loop variable.
break_, = ag__.for_stmt(range(10), extra_test, ..., (break_,))
'''

### `continue` statements

Code blocks in which `continue` statements are used are rewritten with
equivalent code that uses extra control booleans and conditionals, similar to
how `break` is handled.

For example, the `for` loop below is rewritten as (showing the output of the
`continue` transformation only):

'''
for i in range(10):
  if i > 3:
    continue
'''

'''
for i in range(10):
  continue_ = False
  if i > 3:
    continue_ = True
  if not continue_:
    i += 1
'''

Notice that unlike `break`, `continue` statements are local to the loop and do
not influence the number of iterations.

### `return` statements

`return` statements are also rewritten using control symbols, in a manner
similar to how `break` is converted. In the case of `return` statements, an
additional symbol keeps track of the return value.

Depending on the structure of the code, the return value might be undefined
in parts of the code (for example on code paths in which no return statement
has executed). AutoGraph keeps track of this by using a special value.
This special value is converted to `None` (the default return value) upon
exiting the function.

Caution: TensorFlow control flow doe not support undefined values, and an
undefined return value is no exception. Therefore, AutoGraph will raise an
error for TensorFlow control flow in which the return value is not known for
all code paths.

For example, the following code raises an error because the return value would
be undefined when the random number would be less than 0.5:

'''
if tf.random.uniform(()) > 0.5:
  return 1
'''

'''
ValueError: A value must also be returned from the else branch.
'''

An example of rewriting a `while` (showing the output of the `return`
transformation only):

'''
def f():
  while i < 10:
    if i > 3:
      return 1
    i += 1
'''

'''
def f():
  do_return = False
  retval_ = ag__.UndefinedReturnValue()
  while i < 10 and not do_return:
    if i > 3:
      do_return = True
      retval_ = 1
    if not do_return:
      i += 1
  return ag__.retval(retval_)  # Transforms any UndefinedReturnValue to None
'''

Note: AutoGraph performs an additional code normalization in which an `if`
statement with no `else` branch contains a `return` statement it is rewritten as
an `if-else` statement in which the code that follows the statement is moved
under the `else` branch.

Example (showing the normalization only):

'''
def f():
  if i > 3:
    return 1
  i += 1
'''

'''
def f():
  if i > 3:
    return 1
  else:
   i += 1
'''


```
## _tensorflow_lite_nnapi_README_md
```# Android Neural Network API

The Android Neural Networks API (NNAPI) is an Android C API designed for running
computationally intensive operators for machine learning on mobile devices.
Tensorflow Lite is designed to use the NNAPI to perform hardware-accelerated
inference operators on supported devices.
Based on the app’s requirements and the hardware capabilities on a device, the
NNAPI can distribute the computation workload across available on-device
processors, including dedicated neural network hardware, graphics processing
units (GPUs), and digital signal processors (DSPs).
For devices that lack a specialized vendor driver, the NNAPI runtime relies on
optimized code to execute requests on the CPU. For more information about the
NNAPI, please refer to the [NNAPI documentation](https://developer.android.com/ndk/guides/neuralnetworks/index.html)


```
## _tensorflow_tools_dockerfiles_readme_for_jupyter_md
```Want more tutorials like these?

Check out tensorflow.org/tutorials!
```
## _README_md
```<div align="center">
  <img src="https://www.tensorflow.org/images/tf_logo_social.png">
</div>

**`Documentation`** |
------------------- |
[![Documentation](https://img.shields.io/badge/api-reference-blue.svg)](https://www.tensorflow.org/api_docs/) |

[TensorFlow](https://www.tensorflow.org/) is an end-to-end open source platform
for machine learning. It has a comprehensive, flexible ecosystem of
[tools](https://www.tensorflow.org/resources/tools),
[libraries](https://www.tensorflow.org/resources/libraries-extensions), and
[community](https://www.tensorflow.org/community) resources that lets
researchers push the state-of-the-art in ML and developers easily build and
deploy ML powered applications.

TensorFlow was originally developed by researchers and engineers working on the
Google Brain team within Google's Machine Intelligence Research organization for
the purposes of conducting machine learning and deep neural networks research.
The system is general enough to be applicable in a wide variety of other
domains, as well.

TensorFlow provides stable [Python](https://www.tensorflow.org/api_docs/python)
and [C++](https://www.tensorflow.org/api_docs/cc) APIs, as well as
non-guaranteed backwards compatible API for
[other languages](https://www.tensorflow.org/api_docs).

Keep up-to-date with release announcements and security updates by subscribing
to
[announce@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/announce).
See all the [mailing lists](https://www.tensorflow.org/community/forums).

## Install

See the [TensorFlow install guide](https://www.tensorflow.org/install) for the
[pip package](https://www.tensorflow.org/install/pip), to
[enable GPU support](https://www.tensorflow.org/install/gpu), use a
[Docker container](https://www.tensorflow.org/install/docker), and
[build from source](https://www.tensorflow.org/install/source).

To install the current release for CPU-only:

'''
$ pip install tensorflow
'''

Use the GPU package for
[CUDA-enabled GPU cards](https://www.tensorflow.org/install/gpu):

'''
$ pip install tensorflow-gpu
'''

*Nightly binaries are available for testing using the
[tf-nightly](https://pypi.python.org/pypi/tf-nightly) and
[tf-nightly-gpu](https://pypi.python.org/pypi/tf-nightly-gpu) packages on PyPi.*

#### *Try your first TensorFlow program*

'''shell
$ python
'''

'''python
>>> import tensorflow as tf
>>> tf.add(1, 2).numpy()
3
>>> hello = tf.constant('Hello, TensorFlow!')
>>> hello.numpy()
'Hello, TensorFlow!'
'''

For more examples, see the
[TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

## Contribution guidelines

**If you want to contribute to TensorFlow, be sure to review the
[contribution guidelines](CONTRIBUTING.md). This project adheres to TensorFlow's
[code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to
uphold this code.**

**We use [GitHub issues](https://github.com/tensorflow/tensorflow/issues) for
tracking requests and bugs, please see
[TensorFlow Discuss](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss)
for general questions and discussion, and please direct specific questions to
[Stack Overflow](https://stackoverflow.com/questions/tagged/tensorflow).**

The TensorFlow project strives to abide by generally accepted best practices in
open-source software development:

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1486/badge)](https://bestpractices.coreinfrastructure.org/projects/1486)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

## Continuous build status

### Official Builds

Build Type               | Status                                                                                                                                                                                                                                                                                                                                        | Artifacts
------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------
**Linux CPU**            | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-cc.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-cc.html)                                                                                                                                                                        | [pypi](https://pypi.org/project/tf-nightly/)
**Linux GPU**            | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-gpu-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-gpu-py3.html)                                                                                                                                                              | [pypi](https://pypi.org/project/tf-nightly-gpu/)
**Linux XLA**            | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-xla.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-xla.html)                                                                                                                                                                      | TBA
**MacOS**                | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/macos-py2-cc.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/macos-py2-cc.html)                                                                                                                                                                  | [pypi](https://pypi.org/project/tf-nightly/)
**Windows CPU**          | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-cpu.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-cpu.html)                                                                                                                                                                    | [pypi](https://pypi.org/project/tf-nightly/)
**Windows GPU**          | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-gpu.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-gpu.html)                                                                                                                                                                    | [pypi](https://pypi.org/project/tf-nightly-gpu/)
**Android**              | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/android.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/android.html)                                                                                                                                                                            | [![Download](https://api.bintray.com/packages/google/tensorflow/tensorflow/images/download.svg)](https://bintray.com/google/tensorflow/tensorflow/_latestVersion)
**Raspberry Pi 0 and 1** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py2.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py2.html) [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py3.html) | [Py2](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp27-none-linux_armv6l.whl) [Py3](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp34-none-linux_armv6l.whl)
**Raspberry Pi 2 and 3** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py2.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py2.html) [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py3.html) | [Py2](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp27-none-linux_armv7l.whl) [Py3](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp34-none-linux_armv7l.whl)

### Community Supported Builds

Build Type                                                                            | Status                                                                                                                                                                                        | Artifacts
------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------
**Linux AMD ROCm GPU** Nightly                                                        | [![Build Status](http://ml-ci.amd.com:21096/job/tensorflow-rocm-nightly/badge/icon)](http://ml-ci.amd.com:21096/job/tensorflow-rocm-nightly)                                                  | [Nightly](http://ml-ci.amd.com:21096/job/tensorflow-rocm-nightly/lastSuccessfulBuild/)
**Linux AMD ROCm GPU** Stable Release                                                 | [![Build Status](http://ml-ci.amd.com:21096/job/tensorflow-rocm-release/badge/icon)](http://ml-ci.amd.com:21096/job/tensorflow-rocm-release/)                                                 | Release [1.15](http://ml-ci.amd.com:21096/job/tensorflow-rocm-release/lastSuccessfulBuild/) / [2.x](http://ml-ci.amd.com:21096/job/tensorflow-rocm-v2-release/lastSuccessfulBuild/)
**Linux s390x** Nightly                                                               | [![Build Status](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_CI/badge/icon)](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_CI/)                                                             | [Nightly](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_CI/)
**Linux s390x CPU** Stable Release                                                    | [![Build Status](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_Release_Build/badge/icon)](https://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_Release_Build/)                                      | [Release](https://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_Release_Build/)
**Linux ppc64le CPU** Nightly                                                         | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Build/)                                       | [Nightly](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Nightly_Artifact/)
**Linux ppc64le CPU** Stable Release                                                  | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/)                       | [Release](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/)
**Linux ppc64le GPU** Nightly                                                         | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Build/)                                       | [Nightly](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Nightly_Artifact/)
**Linux ppc64le GPU** Stable Release                                                  | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/)                       | [Release](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/)
**Linux CPU with Intel® MKL-DNN** Nightly                                             | [![Build Status](https://tensorflow-ci.intel.com/job/tensorflow-mkl-linux-cpu/badge/icon)](https://tensorflow-ci.intel.com/job/tensorflow-mkl-linux-cpu/)                                     | [Nightly](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-whl-nightly/)
**Linux CPU with Intel® MKL-DNN** <br> **Supports Python 2.7, 3.4, 3.5, 3.6 and 3.7** | [![Build Status](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-release-whl/badge/icon)](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-release-whl/lastStableBuild)      | [1.14.0 pypi](https://pypi.org/project/intel-tensorflow/)
**Red Hat® Enterprise Linux® 7.6 CPU & GPU** <br> Python 2.7, 3.6                     | [![Build Status](https://jenkins-tensorflow.apps.ci.centos.org/buildStatus/icon?job=tensorflow-rhel7-3.6&build=2)](https://jenkins-tensorflow.apps.ci.centos.org/job/tensorflow-rhel7-3.6/2/) | [1.13.1 pypi](https://tensorflow.pypi.thoth-station.ninja/index/)

## Resources

*   [TensorFlow.org](https://www.tensorflow.org)
*   [TensorFlow tutorials](https://www.tensorflow.org/tutorials/)
*   [TensorFlow official models](https://github.com/tensorflow/models/tree/master/official)
*   [TensorFlow examples](https://github.com/tensorflow/examples)
*   [TensorFlow in Practice from Coursera](https://www.coursera.org/specializations/tensorflow-in-practice)
*   [TensorFlow blog](https://blog.tensorflow.org)
*   [TensorFlow Twitter](https://twitter.com/tensorflow)
*   [TensorFlow YouTube](https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ)
*   [TensorFlow roadmap](https://www.tensorflow.org/community/roadmap)
*   [TensorFlow white papers](https://www.tensorflow.org/about/bib)
*   [TensorBoard visualization toolkit](https://github.com/tensorflow/tensorboard)

Learn more about the
[TensorFlow community](https://www.tensorflow.org/community) and how to
[contribute](https://www.tensorflow.org/community/contribute).

## License

[Apache License 2.0](LICENSE)
```
# Inline
## _third_party_mlir_lib_Transforms_SimplifyAffineStructures_cpp
### Line 1-57
```
//===- SimplifyAffineStructures.cpp ---------------------------------------===//
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
// This file implements a pass to simplify affine structures.
//
//===----------------------------------------------------------------------===//

#include "mlir/Analysis/AffineStructures.h"
#include "mlir/IR/IntegerSet.h"
#include "mlir/Pass/Pass.h"
#include "mlir/Transforms/Passes.h"
#include "mlir/Transforms/Utils.h"

#define DEBUG_TYPE "simplify-affine-structure"

using namespace mlir;

namespace {

/// Simplifies affine maps and sets appearing in the operations of the Function.
/// This part is mainly to test the simplifyAffineExpr method. In addition,
/// all memrefs with non-trivial layout maps are converted to ones with trivial
/// identity layout ones.
struct SimplifyAffineStructures
    : public FunctionPass<SimplifyAffineStructures> {
  void runOnFunction() override;

  /// Utility to simplify an affine attribute and update its entry in the parent
  /// operation if necessary.
  template <typename AttributeT>
  void simplifyAndUpdateAttribute(Operation *op, Identifier name,
                                  AttributeT attr) {
    auto &simplified = simplifiedAttributes[attr];
    if (simplified == attr)
      return;

    // This is a newly encountered attribute.
    if (!simplified) {
      // Try to simplify the value of the attribute.
      auto value = attr.getValue();
      auto simplifiedValue = simplify(value);
      if (simplifiedValue == value) {
        simplified = attr;

```
### Line 58-81
```
        return;
      }
      simplified = AttributeT::get(simplifiedValue);
    }

    // Simplification was successful, so update the attribute.
    op->setAttr(name, simplified);
  }

  /// Performs basic integer set simplifications. Checks if it's empty, and
  /// replaces it with the canonical empty set if it is.
  IntegerSet simplify(IntegerSet set) {
    FlatAffineConstraints fac(set);
    if (fac.isEmpty())
      return IntegerSet::getEmptySet(set.getNumDims(), set.getNumSymbols(),
                                     &getContext());
    return set;
  }

  /// Performs basic affine map simplifications.
  AffineMap simplify(AffineMap map) {
    MutableAffineMap mMap(map);
    mMap.simplify();
    return mMap.getAffineMap();

```
### Line 100-111
```
      else if (auto setAttr = attr.second.dyn_cast<IntegerSetAttr>())
        simplifyAndUpdateAttribute(opInst, attr.first, setAttr);
    }
  });

  // Turn memrefs' non-identity layouts maps into ones with identity. Collect
  // alloc ops first and then process since normalizeMemRef replaces/erases ops
  // during memref rewriting.
  SmallVector<AllocOp, 4> allocOps;
  func.walk([&](AllocOp op) { allocOps.push_back(op); });
  for (auto allocOp : allocOps) {
    normalizeMemRef(allocOp);

```

## _tensorflow_lite_testing_op_tests_constant_py
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
"""Test configs for constant ops."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

```
### Line 23-43
```
from tensorflow.lite.testing.zip_test_utils import make_zip_of_tests
from tensorflow.lite.testing.zip_test_utils import register_make_test_function
from tensorflow.lite.testing.zip_test_utils import TF_TYPE_INFO


# This function tests various TensorFLow functions that generates Const op,
# including `tf.ones`, `tf.zeros` and random functions.
@register_make_test_function()
def make_constant_tests(options):
  """Make a set of tests to do constant ops."""

  test_parameters = [{
      "dtype": [tf.float32, tf.int32],
      "input_shape": [[], [1], [2], [1, 1, 1, 1], [2, 2, 2, 2]],
      "constant_is_also_output": [True, False],
      # This is a regression test for a bug where Toco rejects models with
      # unread inputs.
      "has_unread_input": [True, False],
  }]

  def build_graph(parameters):

```

## _tensorflow_python_distribute_multi_worker_test_base_py
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
"""Base testing class for strategies that require multiple nodes."""

from __future__ import absolute_import
from __future__ import division

```
### Line 33-42
```
  import portpicker  # pylint: disable=g-import-not-at-top
except ImportError as _error:  # pylint: disable=invalid-name
  _portpicker_import_error = _error
  portpicker = None

# pylint: disable=g-import-not-at-top
from tensorflow.core.protobuf import config_pb2
from tensorflow.core.protobuf import rewriter_config_pb2
from tensorflow.python.client import session
from tensorflow.python.distribute import distribute_coordinator as dc

```
### Line 147-163
```
                              num_ps,
                              has_chief=False,
                              has_eval=False,
                              rpc_layer='grpc'):
  """Create an in-process cluster that consists of only standard server."""
  # Leave some memory for cuda runtime.
  gpu_mem_frac = 0.7 / (num_workers + int(has_chief) + int(has_eval))
  worker_config = config_pb2.ConfigProto()
  worker_config.gpu_options.per_process_gpu_memory_fraction = gpu_mem_frac

  # Enable collective ops which has no impact on non-collective ops.
  # TODO(yuefengz, tucker): removing this after we move the initialization of
  # collective mgr to the session level.
  if has_chief:
    worker_config.experimental.collective_group_leader = (
        '/job:chief/replica:0/task:0')
  else:

```
### Line 168-185
```
  ps_config.device_count['GPU'] = 0

  eval_config = config_pb2.ConfigProto()
  eval_config.experimental.collective_group_leader = ''

  # Create in-process servers. Once an in-process tensorflow server is created,
  # there is no way to terminate it. So we create one cluster per test process.
  # We could've started the server in another process, we could then kill that
  # process to terminate the server. The reasons why we don't want multiple
  # processes are
  # 1) it is more difficult to manage these processes;
  # 2) there is something global in CUDA such that if we initialize CUDA in the
  # parent process, the child process cannot initialize it again and thus cannot
  # use GPUs (https://stackoverflow.com/questions/22950047).
  cluster = None
  try:
    cluster = _create_cluster(
        num_workers,

```
### Line 196-206
```
    else:
      raise
  return cluster


# TODO(rchao): Remove `test_obj` once estimator repo picks up the updated
# nightly TF.
def create_cluster_spec(has_chief=False,
                        num_workers=1,
                        num_ps=0,
                        has_eval=False,

```
### Line 249-259
```
    cls._cluster_spec = create_in_process_cluster(num_workers=num_workers,
                                                  num_ps=num_ps)
    cls._default_target = 'grpc://' + cls._cluster_spec['worker'][0]

  def setUp(self):
    # We only cache the session in one test because another test may have a
    # different session config or master target.
    self._thread_local = threading.local()
    self._thread_local.cached_session = None
    self._coord = coordinator.Coordinator()


```
### Line 279-288
```
      target = self._default_target
    with session.Session(graph=graph, config=config, target=target) as sess:
      yield sess

  @contextlib.contextmanager
  # TODO(b/117573461): Overwrite self.evaluate() to use this function.
  def cached_session(self, graph=None, config=None, target=None):
    """Create a test session with master target set to the testing cluster.

    Creates a test session that connects to the local testing cluster.

```
### Line 313-323
```
  def _create_config(self, config):
    if config is None:
      config = config_pb2.ConfigProto(allow_soft_placement=True)
    else:
      config = copy.deepcopy(config)
    # Don't perform optimizations for tests so we don't inadvertently run
    # gpu ops on cpu
    config.graph_options.optimizer_options.opt_level = -1
    config.graph_options.rewrite_options.constant_folding = (
        rewriter_config_pb2.RewriterConfig.OFF)


```
### Line 444-456
```

    def _mock_run_std_server(*args, **kwargs):
      """Returns the std server once all threads have started it."""
      with skip_if_grpc_server_cant_be_started(self):
        ret = original_run_std_server(*args, **kwargs)
      # Wait for all std servers to be brought up in order to reduce the chance
      # of remote sessions taking local ports that have been assigned to std
      # servers. Only call this barrier the first time this function is run for
      # each thread.
      if not getattr(self._thread_local, 'server_started', False):
        self._barrier.wait()
      self._thread_local.server_started = True
      return ret

```
### Line 462-471
```
    self._mock_context = test.mock.patch.object(os, 'environ',
                                                self._mock_os_env)
    self._coord = coordinator.Coordinator()
    super(IndependentWorkerTestBase, self).setUp()
    self._mock_context.__enter__()
    # threading local object to be shared by all threads
    self._thread_local = threading.local()

  def tearDown(self):
    self._mock_context.__exit__(None, None, None)

```
### Line 473-483
```

  def _task_thread(self, task_fn, tf_config, executing_eagerly, *args,
                   **kwargs):
    with self._coord.stop_on_exception():
      os.environ['TF_CONFIG'] = json.dumps(tf_config)
      # Force the new thread simulating a worker to run in the same context
      # mode as the parent thread does.
      if executing_eagerly:
        with context.eager_mode():
          task_fn(*args, **kwargs)
      else:

```
### Line 526-535
```
    t.start()
    return t

  def run_multiple_tasks_in_threads(self, task_fn, cluster_spec, *args,
                                    **kwargs):
    # The task_fn should create std_server by itself.
    threads = {}
    for task_type in cluster_spec.keys():
      threads[task_type] = []
      for task_id in range(len(cluster_spec[task_type])):

```
### Line 571-584
```

  def join_independent_workers(self, worker_processes):
    return_codes = []
    for p in nest.flatten(worker_processes):
      try:
        # Calling p.wait() will hang if we don't consume its output.
        p.communicate()
      except ValueError:
        # The output of the process may have been consumed, in which case
        # calling `p.communicate()` will raise a ValueError.
        pass
      finally:
        return_codes.append(p.returncode)
    for return_code in return_codes:

```

## _tensorflow_python_eager_test_py
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
"""Utilities for testing tfe code."""

from __future__ import absolute_import
from __future__ import division

```
### Line 21-29
```
from tensorflow.python.framework import ops as _ops
from tensorflow.python.platform import test as _test
from tensorflow.python.platform.test import *  # pylint: disable=wildcard-import


# TODO(akshayka): Do away with this file.
def main(argv=None):  # pylint: disable=function-redefined
  _ops.enable_eager_execution()
  _test.main(argv)

```

## _tensorflow_python_data_experimental_kernel_tests_optimization_choose_fastest_dataset_test_py
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
"""Tests for `tf.data.experimental._ChooseFastestDataset`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

```
### Line 69-78
```
  def testChooseFastestErrorWithIncompatibleInput(self, slices_a, slices_b,
                                                  error_msg):
    dataset_a = dataset_ops.Dataset.from_tensor_slices(slices_a)
    dataset_b = dataset_ops.Dataset.from_tensor_slices(slices_b)

    # The error is raised at dataset creation time.
    if context.executing_eagerly():
      with self.assertRaises(errors.InvalidArgumentError):
        merge = optimization._ChooseFastestDataset([dataset_a, dataset_b])
    else:

```

## _tensorflow_python_data_kernel_tests_test_base_py
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
"""Test utilities for tf.data functionality."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

```
### Line 68-77
```
  def getNext(self, dataset, requires_initialization=False, shared_name=None):
    """Returns a callable that returns the next element of the dataset.

    Example use:
    ```python
    # In both graph and eager modes
    dataset = ...
    get_next = self.getNext(dataset)
    result = self.evaluate(get_next())
    ```

```
### Line 95-105
```
          return r.stack()
        else:
          return r
      return _wrapper

    # Create an anonymous iterator if we are in eager-mode or are graph inside
    # of a tf.function.
    building_function = ops.get_default_graph()._building_function  # pylint: disable=protected-access
    if context.executing_eagerly() or building_function:
      iterator = iter(dataset)
      return ta_wrapper(iterator._next_internal)  # pylint: disable=protected-access

```
### Line 113-123
```
      return ta_wrapper(lambda: get_next)

  def _compareOutputToExpected(self, result_values, expected_values,
                               assert_items_equal):
    if assert_items_equal:
      # TODO(shivaniagrawal): add support for nested elements containing sparse
      # tensors when needed.
      self.assertItemsEqual(result_values, expected_values)
      return
    for i in range(len(result_values)):
      nest.assert_same_structure(result_values[i], expected_values[i])

```
### Line 239-248
```
          repr(exception_class))
    except exception_class as e:
      expected_message = e.message
      for old, new, count in replacements:
        expected_message = expected_message.replace(old, new, count)
      # Check that the first segment of the error messages are the same.
      with self.assertRaisesRegexp(exception_class,
                                   re.escape(expected_message)):
        self.evaluate(next2())


```

## _tensorflow_examples_speech_commands_label_wav_test_py
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
"""Tests for WAVE file labeling tool."""

from __future__ import absolute_import
from __future__ import division

```

## _tensorflow_python_kernel_tests_random_multinomial_op_test_py
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
"""Tests for Multinomial."""

from __future__ import absolute_import
from __future__ import division

```
### Line 36-52
```
from tensorflow.python.ops import random_ops
from tensorflow.python.platform import test


def composed_sampler(logits, num_samples):
  # [batch size, num classes, num samples]
  unif = random_ops.random_uniform(logits.get_shape().concatenate(
      tensor_shape.TensorShape([num_samples])))
  noise = -math_ops.log(-math_ops.log(unif))
  # [batch size, num classes, 1]
  logits = array_ops.expand_dims(logits, -1)

  # [batch size, num samples]
  return math_ops.argmax(logits + noise, axis=1)


native_sampler = random_ops.multinomial

```
### Line 57-66
```
  @test_util.run_in_graph_and_eager_modes
  def testSmallEntropy(self):
    random_seed.set_random_seed(1618)
    for output_dtype in [np.int32, np.int64]:
      with test_util.device(use_gpu=True):
        # A logit value of -10 corresponds to a probability of ~5e-5.
        logits = constant_op.constant([[-10., 10., -10.], [-10., -10., 10.]])
        num_samples = 1000
        samples = self.evaluate(random_ops.multinomial(
            logits, num_samples, output_dtype=output_dtype))

```
### Line 68-93
```

  @test_util.run_deprecated_v1
  def testOneOpMultipleStepsIndependent(self):
    with test_util.use_gpu():
      sample_op1, _ = self._make_ops(10)
      # Consecutive runs shouldn't yield identical output.
      sample1a = self.evaluate(sample_op1)
      sample1b = self.evaluate(sample_op1)
      self.assertFalse(np.equal(sample1a, sample1b).all())

  def testEagerOneOpMultipleStepsIndependent(self):
    with context.eager_mode(), test_util.device(use_gpu=True):
      sample1, sample2 = self._make_ops(10)
      # Consecutive runs shouldn't yield identical output.
      self.assertFalse(np.equal(sample1.numpy(), sample2.numpy()).all())

  def testTwoOpsIndependent(self):
    with test_util.use_gpu():
      sample_op1, sample_op2 = self._make_ops(32)
      sample1, sample2 = self.evaluate([sample_op1, sample_op2])
      # We expect sample1 and sample2 to be independent.
      # 1 in 2^32 chance of this assertion failing.
      self.assertFalse(np.equal(sample1, sample2).all())

  @test_util.run_deprecated_v1
  def testTwoOpsSameSeedDrawSameSequences(self):

```
### Line 101-110
```
      with test_util.use_gpu():
        logits = np.array([[1000.] * 5])
        if neg:
          logits *= -1
        samples = self.evaluate(random_ops.multinomial(logits, 10))
      # Sampled classes should be in-range.
      self.assertTrue((samples >= 0).all())
      self.assertTrue((samples < 5).all())

  def testSamplingCorrectness(self):

```
### Line 120-129
```

      logits = np.log(probs).astype(np.float32)
      composed_freqs = self._do_sampling(logits, num_samples, composed_sampler)
      native_freqs = self._do_sampling(logits, num_samples, native_sampler)

      # the test here is similar to core/lib/random/distribution_sampler_test.cc
      composed_chi2 = self._chi2(probs, composed_freqs)
      native_chi2 = self._chi2(probs, native_freqs)
      composed_native_chi2 = self._chi2(composed_freqs, native_freqs)


```
### Line 136-145
```
      check(composed_native_chi2)

  def _make_ops(self, num_samples, seed=None):
    prob_dist = constant_op.constant([[0.15, 0.5, 0.3, 0.05]])
    logits = math_ops.log(prob_dist)
    # Two independent sets of samples from the same distribution
    sample_op1 = random_ops.multinomial(logits, num_samples, seed)
    sample_op2 = random_ops.multinomial(logits, num_samples, seed)
    return (sample_op1, sample_op2)


```
### Line 167-176
```
    batch_size, num_classes = logits.shape
    freqs_mat = []
    for i in range(batch_size):
      cnts = dict(collections.Counter(d[i, :]))

      # Requires drawn class labels be in range.
      self.assertLess(max(cnts.keys()), num_classes)
      self.assertGreaterEqual(min(cnts.keys()), 0)

      freqs = [(cnts[k] * 1. / num_samples if k in cnts else 0)

```
### Line 210-225
```
      num_samples = 1000
      samples = self.evaluate(random_ops.multinomial(logits, num_samples))
      self.assertAllEqual([[1023] * num_samples], samples)


# Benchmarking code
def native_op_vs_composed_ops(batch_size, num_classes, num_samples, num_iters):
  np.random.seed(1618)  # Make it reproducible.
  shape = [batch_size, num_classes]
  logits_np = np.random.randn(*shape).astype(np.float32)

  # No CSE/CF.
  optimizer_options = config_pb2.OptimizerOptions(
      opt_level=config_pb2.OptimizerOptions.L0)
  config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
      optimizer_options=optimizer_options))

```

## _tensorflow_compiler_tests_lrn_ops_test_py
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
"""Tests for Local Response Normalization ops."""

from __future__ import absolute_import
from __future__ import division

```
### Line 32-42
```
from tensorflow.python.platform import googletest

CPU_DEVICE = "/job:localhost/replica:0/task:0/cpu:0"


# Local response normalization tests. The forward tests are copied from
# tensorflow/python/kernel_tests/lrn_op_test.py
class LRNTest(xla_test.XLATestCase):

  def _LRN(self, input_image, lrn_depth_radius=5, bias=1.0, alpha=1.0,
           beta=0.5):

```
### Line 57-71
```
                np.power(bias + alpha * np.sum(patch * patch), beta))
    return output

  def _RunAndVerify(self, dtype):
    with self.session():
      # random shape
      shape = np.random.randint(1, 16, size=4)
      # Make depth at least 2 to make it meaningful
      shape[3] += 1
      p = array_ops.placeholder(dtype, shape=shape)
      # random depth_radius, bias, alpha, beta
      lrn_depth_radius = np.random.randint(1, shape[3])
      bias = 1.0 + np.random.rand()
      alpha = 2.0 * np.random.rand()
      beta = 2.0 * np.random.rand()

```
### Line 97-106
```
  def testCompute(self):
    for _ in range(2):
      self._RunAndVerify(dtypes.float32)

  def testLrnGrad(self):
    # Test for LRNGrad that compares against the CPU implementation.
    shape = [1, 2, 3, 4]
    total_size = np.prod(shape)
    in_image_vals = np.arange(1, total_size + 1, dtype=np.float32)
    out_image_vals = np.arange(1, total_size + 1, dtype=np.float32)

```

## _tensorflow_python_feature_column_feature_column_v2_test_py
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
"""Tests for feature_column."""

from __future__ import absolute_import
from __future__ import division

```
### Line 89-100
```


class SortableFeatureColumnTest(test.TestCase):

  def test_sort_columns_by_string_representation(self):
    # These should be sorted lexicographically based on their string
    # representations. For FeatureColumns, this looks like
    # '<__main__.FeatureColumn object at ...>'.

    a = fc.numeric_column('first')  # '<__main__.NumericColumn ...>'
    b = fc.numeric_column('second')  # '<__main__.NumericColumn ...>'
    c = fc_old._numeric_column('third')  # '<__main__._NumericColumn ...>'

```
### Line 101-116
```

    sorted_sequence = ['0', a, b, c, 'd']
    reversed_sequence = sorted_sequence[::-1]
    self.assertAllEqual(sorted(reversed_sequence), sorted_sequence)

    # pylint: disable=g-generic-assert
    self.assertTrue(a < b)  # V2 < V2 feature columns.
    self.assertTrue(a < c)  # V2 < V1 feature columns.
    self.assertFalse(c < a)  # V1 < V2 feature columns.
    self.assertTrue('0' < a)  # string < V2 feature column.
    self.assertTrue(a < 'd')  # V2 feature column < string.
    # pylint: enable=g-generic-assert


class LazyColumnTest(test.TestCase):


```
### Line 216-225
```
      @property
      def name(self):
        return 'NotAProperColumn'

      def transform_feature(self, transformation_cache, state_manager):
        # It should return not None.
        pass

      @property
      def parse_example_spec(self):

```
### Line 242-251
```
        TypeError, '"key" must be either a "str" or "FeatureColumn".'):
      transformation_cache.get(NotAFeatureColumn(), None)

  @test_util.run_deprecated_v1
  def test_expand_dim_rank_1_sparse_tensor_empty_batch(self):
    # empty 1-D sparse tensor:
    transformation_cache = fc.FeatureTransformationCache(
        features={
            'a':
                sparse_tensor.SparseTensor(

```
### Line 490-499
```
    new_col = fc.NumericColumn.from_config(
        config, custom_objects={'_increment_two': _increment_two})
    self.assertEqual(price, new_col)
    self.assertEqual(new_col.shape, (1,))

    # Also test round trip through feature column serialization utils.
    new_col = serialization.deserialize_feature_column(
        serialization.serialize_feature_column(price),
        custom_objects={'_increment_two': _increment_two})
    self.assertEqual(price, new_col)

```
### Line 549-564
```
    }, b.parse_example_spec)

  def test_variable_shape(self):
    a = fc.numeric_column('aaa', shape=[2], dtype=dtypes.int32)
    b = fc.bucketized_column(a, boundaries=[0, 1])
    # Column 'aaa` has shape [2] times three buckets -> variable_shape=[2, 3].
    self.assertAllEqual((2, 3), b.variable_shape)

  def test_num_buckets(self):
    a = fc.numeric_column('aaa', shape=[2], dtype=dtypes.int32)
    b = fc.bucketized_column(a, boundaries=[0, 1])
    # Column 'aaa` has shape [2] times three buckets -> num_buckets=6.
    self.assertEqual(6, b.num_buckets)

  @test_util.run_deprecated_v1
  def test_parse_example(self):

```
### Line 606-615
```
      self.evaluate(lookup_ops.tables_initializer())

      bucketized_price_tensor = bucketized_price.get_dense_tensor(
          transformation_cache, None)
      self.assertAllClose(
          # One-hot tensor.
          [[[1., 0., 0., 0., 0.]], [[0., 1., 0., 0., 0.]],
           [[0., 0., 0., 1., 0.]], [[0., 0., 0., 0., 1.]]],
          self.evaluate(bucketized_price_tensor))


```
### Line 626-635
```
      self.evaluate(lookup_ops.tables_initializer())

      bucketized_price_tensor = bucketized_price.get_dense_tensor(
          transformation_cache, None)
      self.assertAllClose(
          # One-hot tensor.
          [[[1., 0., 0., 0., 0.], [0., 1., 0., 0., 0.]],
           [[0., 0., 0., 1., 0.], [0., 0., 0., 0., 1.]]],
          self.evaluate(bucketized_price_tensor))


```
### Line 664-674
```
            transformation_cache, None)
        self.assertIsNone(id_weight_pair.weight_tensor)
        id_tensor_value = sess.run(id_weight_pair.id_tensor)
        self.assertAllEqual([[0, 0], [0, 1], [1, 0], [1, 1]],
                            id_tensor_value.indices)
        # Values 0-4 correspond to the first column of the input price.
        # Values 5-9 correspond to the second column of the input price.
        self.assertAllEqual([0, 6, 3, 9], id_tensor_value.values)
        self.assertAllEqual([2, 2], id_tensor_value.dense_shape)

  def test_sparse_tensor_input_not_supported(self):

```
### Line 700-719
```
      model = fc.LinearModel([bucketized_price])
      predictions = model(features)
      bucketized_price_var, bias = model.variables
      with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight variable per bucket, all initialized to zero.
        self.assertAllClose([[0.], [0.], [0.], [0.], [0.]],
                            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.], [0.], [0.]],
                            self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.]]))
        # price -1. is in the 0th bucket, whose weight is 10.
        # price 1. is in the 1st bucket, whose weight is 20.
        # price 5. is in the 3rd bucket, whose weight is 40.
        # price 6. is in the 4th bucket, whose weight is 50.
        self.assertAllClose([[10.], [20.], [40.], [50.]],
                            self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[11.], [21.], [41.], [51.]],

```
### Line 728-750
```
      model = fc.LinearModel([bucketized_price])
      predictions = model(features)
      bucketized_price_var, bias = model.variables
      with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight per bucket per input column, all initialized to zero.
        self.assertAllClose(
            [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]],
            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.]], self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.],
                                         [60.], [70.], [80.], [90.], [100.]]))
        # 1st example:
        #   price -1. is in the 0th bucket, whose weight is 10.
        #   price 1. is in the 6th bucket, whose weight is 70.
        # 2nd example:
        #   price 5. is in the 3rd bucket, whose weight is 40.
        #   price 6. is in the 9th bucket, whose weight is 100.
        self.assertAllClose([[80.], [140.]], self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[81.], [141.]], self.evaluate(predictions))


```
### Line 757-776
```
      predictions = fc_old.linear_model(features, [bucketized_price])
      bias = get_linear_model_bias()
      bucketized_price_var = get_linear_model_column_var(bucketized_price)
      with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight variable per bucket, all initialized to zero.
        self.assertAllClose([[0.], [0.], [0.], [0.], [0.]],
                            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.], [0.], [0.]],
                            self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.]]))
        # price -1. is in the 0th bucket, whose weight is 10.
        # price 1. is in the 1st bucket, whose weight is 20.
        # price 5. is in the 3rd bucket, whose weight is 40.
        # price 6. is in the 4th bucket, whose weight is 50.
        self.assertAllClose([[10.], [20.], [40.], [50.]],
                            self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[11.], [21.], [41.], [51.]],

```
### Line 785-807
```
      predictions = fc_old.linear_model(features, [bucketized_price])
      bias = get_linear_model_bias()
      bucketized_price_var = get_linear_model_column_var(bucketized_price)
      with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight per bucket per input column, all initialized to zero.
        self.assertAllClose(
            [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]],
            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.]], self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.],
                                         [60.], [70.], [80.], [90.], [100.]]))
        # 1st example:
        #   price -1. is in the 0th bucket, whose weight is 10.
        #   price 1. is in the 6th bucket, whose weight is 70.
        # 2nd example:
        #   price 5. is in the 3rd bucket, whose weight is 40.
        #   price 6. is in the 9th bucket, whose weight is 100.
        self.assertAllClose([[80.], [140.]], self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[81.], [141.]], self.evaluate(predictions))


```
### Line 814-833
```
      predictions = fc_old.linear_model(features, [bucketized_price])
      bias = get_linear_model_bias()
      bucketized_price_var = get_linear_model_column_var(bucketized_price)
      with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight variable per bucket, all initialized to zero.
        self.assertAllClose([[0.], [0.], [0.], [0.], [0.]],
                            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.], [0.], [0.]],
                            self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.]]))
        # price -1. is in the 0th bucket, whose weight is 10.
        # price 1. is in the 1st bucket, whose weight is 20.
        # price 5. is in the 3rd bucket, whose weight is 40.
        # price 6. is in the 4th bucket, whose weight is 50.
        self.assertAllClose([[10.], [20.], [40.], [50.]],
                            self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[11.], [21.], [41.], [51.]],

```
### Line 953-962
```
        dense_shape=[2, 2])
    outputs = fc._transform_features_v2({
        'wire': wire_tensor
    }, [hashed_sparse], None)
    output = outputs[hashed_sparse]
    # Check exact hashed output. If hashing changes this test will break.
    expected_values = [6, 4, 1]

    self.assertEqual(dtypes.int64, output.values.dtype)
    self.assertAllEqual(expected_values, self.evaluate(output.values))

```
### Line 1006-1015
```
        values=[101, 201, 301],
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    transformation_cache = fc.FeatureTransformationCache({'wire': wire_tensor})
    output = transformation_cache.get(hashed_sparse, None)
    # Check exact hashed output. If hashing changes this test will break.
    expected_values = [3, 7, 5]

    self.assertAllEqual(expected_values, self.evaluate(output.values))


```
### Line 1021-1030
```
        values=constant_op.constant([101, 201, 301], dtype=dtypes.int32),
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    transformation_cache = fc.FeatureTransformationCache({'wire': wire_tensor})
    output = transformation_cache.get(hashed_sparse, None)
    # Check exact hashed output. If hashing changes this test will break.
    expected_values = [3, 7, 5]

    self.assertAllEqual(expected_values, self.evaluate(output.values))


```
### Line 1076-1086
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 3: wire_var[3] = 4
      # 'skywalker' -> 2, 'omar' -> 2: wire_var[2] + wire_var[2] = 3+3 = 6
      self.assertAllClose(((4.,), (6.,)), self.evaluate(predictions))

  def test_old_linear_model(self):
    wire_column = fc.categorical_column_with_hash_bucket('wire', 4)

```
### Line 1101-1111
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 3: wire_var[3] = 4
      # 'skywalker' -> 2, 'omar' -> 2: wire_var[2] + wire_var[2] = 3+3 = 6
      self.assertAllClose(((4.,), (6.,)), self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_serialization(self):

```
### Line 1246-1255
```
    self.assertIn('wire', features)

    self.assertAllEqual([[20., 110.]], self.evaluate(features['price']))
    wire_sparse = features['wire']
    self.assertAllEqual([[0, 0], [0, 1]], self.evaluate(wire_sparse.indices))
    # Use byte constants to pass the open-source test.
    self.assertAllEqual([b'omar', b'stringer'],
                        self.evaluate(wire_sparse.values))
    self.assertAllEqual([1, 2], self.evaluate(wire_sparse.dense_shape))


```
### Line 1312-1322
```
      id_tensor_eval = self.evaluate(id_weight_pair.id_tensor)
      self.assertAllEqual(
          ((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
           (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13),
           (1, 14), (1, 15)), id_tensor_eval.indices)
      # Check exact hashed output. If hashing changes this test will break.
      # All values are within [0, hash_bucket_size).
      expected_values = (6, 14, 0, 13, 8, 8, 10, 12, 2, 0, 1, 9, 8, 12, 2, 0,
                         10, 11)
      self.assertAllEqual(expected_values, id_tensor_eval.values)
      self.assertAllEqual((2, 16), id_tensor_eval.dense_shape)

```
### Line 1342-1352
```
      self.evaluate(lookup_ops.tables_initializer())

      id_tensor_eval = self.evaluate(id_weight_pair.id_tensor)
      self.assertAllEqual(((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3)),
                          id_tensor_eval.indices)
      # Check exact hashed output. If hashing changes this test will break.
      # All values are within [0, hash_bucket_size).
      expected_values = (1, 0, 1, 3, 4, 2)
      self.assertAllEqual(expected_values, id_tensor_eval.values)
      self.assertAllEqual((2, 4), id_tensor_eval.dense_shape)


```
### Line 1375-1384
```
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(crossed_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        sess.run(crossed_var.assign(((1.,), (2.,), (3.,), (4.,), (5.,))))
        # Expected ids after cross = (1, 0, 1, 3, 4, 2)
        self.assertAllClose(((3.,), (14.,)), self.evaluate(predictions))
        sess.run(bias.assign((.1,)))
        self.assertAllClose(((3.1,), (14.1,)), self.evaluate(predictions))


```
### Line 1469-1478
```
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(crossed_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        sess.run(crossed_var.assign(((1.,), (2.,), (3.,), (4.,), (5.,))))
        # Expected ids after cross = (1, 0, 1, 3, 4, 2)
        self.assertAllClose(((3.,), (14.,)), self.evaluate(predictions))
        sess.run(bias.assign((.1,)))
        self.assertAllClose(((3.1,), (14.1,)), self.evaluate(predictions))


```
### Line 1579-1588
```
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(crossed_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        sess.run(crossed_var.assign(((1.,), (2.,), (3.,), (4.,), (5.,))))
        # Expected ids after cross = (1, 0, 1, 3, 4, 2)
        self.assertAllClose(((3.,), (14.,)), self.evaluate(predictions))
        sess.run(bias.assign((.1,)))
        self.assertAllClose(((3.1,), (14.1,)), self.evaluate(predictions))


```
### Line 2171-2180
```
            100.,
        ])
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price':
            constant_op.constant([
                -1.,

```
### Line 2213-2222
```
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
    country = fc.categorical_column_with_vocabulary_list(
        'country', vocabulary_list=['US', 'JP', 'CA'])

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price': array_ops.placeholder(dtypes.float32),
        'body-style': array_ops.sparse_placeholder(dtypes.string),
        'country': array_ops.placeholder(dtypes.string),

```
### Line 2252-2266
```
    features = {
        'price': constant_op.constant(0),
    }
    self.assertEqual(0, features['price'].shape.ndims)

    # Static rank 0 should fail
    with self.assertRaisesRegexp(ValueError, 'Feature .* cannot have rank 0'):
      model = fc.LinearModel([price])
      model(features)

    # Dynamic rank 0 should fail
    features = {
        'price': array_ops.placeholder(dtypes.float32),
    }
    model = fc.LinearModel([price])

```
### Line 2678-2698
```

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      self.assertEqual([0.], self.evaluate(cols_to_vars['bias'][0]))
      # Partitioning shards the [2, 1] price1 var into 2 [1, 1] Variables.
      self.assertAllEqual([[0.]], self.evaluate(cols_to_vars[price1][0]))
      self.assertAllEqual([[0.]], self.evaluate(cols_to_vars[price1][1]))
      # Partitioning shards the [3, 1] price2 var into a [2, 1] Variable and
      # a [1, 1] Variable.
      self.assertAllEqual([[0.], [0.]], self.evaluate(cols_to_vars[price2][0]))
      self.assertAllEqual([[0.]], self.evaluate(cols_to_vars[price2][1]))

  def test_fills_cols_to_output_tensors(self):
    # Provide three _DenseColumn's to input_layer: a _NumericColumn, a
    # _BucketizedColumn, and an _EmbeddingColumn.  Only the _EmbeddingColumn
    # creates a Variable.
    apple_numeric_column = fc.numeric_column('apple_numeric_column')
    banana_dense_feature = fc.numeric_column('banana_dense_feature')
    banana_dense_feature_bucketized = fc.bucketized_column(
        banana_dense_feature, boundaries=[0.])

```
### Line 2712-2723
```
          dragonfruit_embedding_column
      ]
      input_layer = fc_old.input_layer(
          features, all_cols, cols_to_output_tensors=cols_to_output_tensors)

      # We check the mapping by checking that we have the right keys,
      # and that the values (output_tensors) were indeed the ones used to
      # form the input layer.
      self.assertItemsEqual(all_cols, cols_to_output_tensors.keys())
      input_layer_inputs = [tensor for tensor in input_layer.op.inputs[:-1]]
      output_tensors = [tensor for tensor in cols_to_output_tensors.values()]
      self.assertItemsEqual(input_layer_inputs, output_tensors)

```
### Line 2894-2903
```
            100.,
        ])
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price':
            constant_op.constant([
                -1.,

```
### Line 2937-2946
```
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
    country = fc.categorical_column_with_vocabulary_list(
        'country', vocabulary_list=['US', 'JP', 'CA'])

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price': array_ops.placeholder(dtypes.float32),
        'body-style': array_ops.sparse_placeholder(dtypes.string),
        'country': array_ops.placeholder(dtypes.string),

```
### Line 2977-2990
```
    features = {
        'price': constant_op.constant(0),
    }
    self.assertEqual(0, features['price'].shape.ndims)

    # Static rank 0 should fail
    with self.assertRaisesRegexp(ValueError, 'Feature .* cannot have rank 0'):
      fc_old.linear_model(features, [price])

    # Dynamic rank 0 should fail
    features = {
        'price': array_ops.placeholder(dtypes.float32),
    }
    net = fc_old.linear_model(features, [price])

```
### Line 3185-3194
```
      sparse_input = sparse_tensor.SparseTensor(
          indices=((0, 0), (1, 0), (2, 0)),
          values=(0, 1, 2),
          dense_shape=(3, 3))

      # Create feature columns (categorical and embedding).
      categorical_column = fc.categorical_column_with_identity(
          key='a', num_buckets=3)
      embedding_dimension = 2


```
### Line 3211-3227
```
      features = {'a': sparse_input}

      inputs = input_layer(features)
      variables = input_layer.variables

      # Sanity check: test that the inputs are correct.
      self.assertAllEqual([[1, 0], [0, 1], [1, 1]], inputs)

      # Check that only one variable was created.
      self.assertEqual(1, len(variables))

      # Check that invoking input_layer on the same features does not create
      # additional variables
      _ = input_layer(features)
      self.assertEqual(1, len(variables))
      self.assertIs(variables[0], input_layer.variables[0])


```
### Line 3230-3239
```
      sparse_input = sparse_tensor.SparseTensor(
          indices=((0, 0), (1, 0), (2, 0)),
          values=(0, 1, 2),
          dense_shape=(3, 3))

      # Create feature columns (categorical and embedding).
      categorical_column = fc.categorical_column_with_identity(
          key='a', num_buckets=3)
      embedding_dimension = 2


```
### Line 3257-3269
```

      def scale_matrix():
        matrix = input_layer(features)
        return 2 * matrix

      # Sanity check: Verify that scale_matrix returns the correct output.
      self.assertAllEqual([[2, 0], [0, 2], [2, 2]], scale_matrix())

      # Check that the returned gradient is correct.
      grad_function = backprop.implicit_grad(scale_matrix)
      grads_and_vars = grad_function()
      indexed_slice = grads_and_vars[0][0]
      gradient = grads_and_vars[0][0].values

```
### Line 3375-3386
```
      self.evaluate(lookup_ops.tables_initializer())

      self.assertAllClose([[1., 2., 3.], [5., 6., 4.]], self.evaluate(net))

  def test_fills_cols_to_vars(self):
    # Provide three _DenseColumn's to input_layer: a _NumericColumn, a
    # _BucketizedColumn, and an _EmbeddingColumn.  Only the _EmbeddingColumn
    # creates a Variable.
    price1 = fc.numeric_column('price1')
    dense_feature = fc.numeric_column('dense_feature')
    dense_feature_bucketized = fc.bucketized_column(
        dense_feature, boundaries=[0.])

```
### Line 3405-3417
```
                            variables_lib.VariableV1)
      self.assertAllEqual(cols_to_vars[some_embedding_column][0].shape, [5, 10])

  @test_util.run_deprecated_v1
  def test_fills_cols_to_vars_shared_embedding(self):
    # Provide 5 DenseColumn's to input_layer: a NumericColumn, a
    # BucketizedColumn, an EmbeddingColumn, two SharedEmbeddingColumns. The
    # EmbeddingColumn creates a Variable and the two SharedEmbeddingColumns
    # shared one variable.
    price1 = fc.numeric_column('price1')
    dense_feature = fc.numeric_column('dense_feature')
    dense_feature_bucketized = fc.bucketized_column(
        dense_feature, boundaries=[0.])

```
### Line 3450-3460
```
      self.assertItemsEqual(list(cols_to_vars.keys()), all_cols)
      self.assertEqual(0, len(cols_to_vars[price1]))
      self.assertEqual(0, len(cols_to_vars[dense_feature_bucketized]))
      self.assertEqual(1, len(cols_to_vars[some_embedding_column]))
      self.assertEqual(1, len(cols_to_vars[shared_embedding_a]))
      # This is a bug in the current implementation and should be fixed in the
      # new one.
      self.assertEqual(0, len(cols_to_vars[shared_embedding_b]))
      self.assertIsInstance(cols_to_vars[some_embedding_column][0],
                            variables_lib.Variable)
      self.assertAllEqual(cols_to_vars[some_embedding_column][0].shape, [5, 10])

```
### Line 3593-3602
```
          'sparse_feature': [['a'], ['x']],
      }
      all_cols = [some_embedding_column]
      fc_old.input_layer(features, all_cols)
      fc_old.input_layer(features, all_cols)
      # Make sure that 2 variables get created in this case.
      self.assertEqual(2, len(
          ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)))
      expected_var_names = [
          'input_layer/sparse_feature_embedding/embedding_weights:0',

```
### Line 3616-3639
```

    def _initializer(shape, dtype, partition_info=None):
      del shape, dtype, partition_info
      return embedding_values

    # price has 1 dimension in input_layer
    price = fc.numeric_column('price')

    # one_hot_body_style has 3 dims in input_layer.
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
    one_hot_body_style = fc.indicator_column(body_style)

    # embedded_body_style has 5 dims in input_layer.
    country = fc.categorical_column_with_vocabulary_list(
        'country', vocabulary_list=['US', 'JP', 'CA'])
    embedded_country = fc.embedding_column(
        country, dimension=5, initializer=_initializer)

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price':
            constant_op.constant([
                11.,

```
### Line 3642-3651
```
        'body-style':
            sparse_tensor.SparseTensor(
                indices=((0,), (1,)),
                values=('sedan', 'hardtop'),
                dense_shape=(2,)),
        # This is dense tensor for the categorical_column.
        'country':
            constant_op.constant(['CA', 'US']),
    }
    self.assertEqual(1, features['price'].shape.ndims)

```
### Line 3655-3665
```
    net = fc_old.input_layer(features,
                             [price, one_hot_body_style, embedded_country])
    self.assertEqual(1 + 3 + 5, net.shape[1])
    with _initialized_session() as sess:

      # Each row is formed by concatenating `embedded_body_style`,
      # `one_hot_body_style`, and `price` in order.
      self.assertAllEqual([[0., 0., 1., 11., 12., 13., 14., 15., 11.],
                           [1., 0., 0., 1., 2., 3., 4., 5., 12.]],
                          sess.run(net))


```
### Line 3673-3700
```

    def _initializer(shape, dtype, partition_info=None):
      del shape, dtype, partition_info
      return embedding_values

    # price has 1 dimension in input_layer
    price = fc.numeric_column('price')

    # one_hot_body_style has 3 dims in input_layer.
    body_style = fc.categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
    one_hot_body_style = fc.indicator_column(body_style)

    # embedded_body_style has 5 dims in input_layer.
    country = fc.categorical_column_with_vocabulary_list(
        'country', vocabulary_list=['US', 'JP', 'CA'])
    embedded_country = fc.embedding_column(
        country, dimension=2, initializer=_initializer)

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price': array_ops.placeholder(dtypes.float32),
        'body-style': array_ops.sparse_placeholder(dtypes.string),
        # This is dense tensor for the categorical_column.
        'country': array_ops.placeholder(dtypes.string),
    }
    self.assertIsNone(features['price'].shape.ndims)
    self.assertIsNone(features['body-style'].get_shape().ndims)

```
### Line 3708-3718
```
    net = fc_old.input_layer(features,
                             [price, one_hot_body_style, embedded_country])
    self.assertEqual(1 + 3 + 2, net.shape[1])
    with _initialized_session() as sess:

      # Each row is formed by concatenating `embedded_body_style`,
      # `one_hot_body_style`, and `price` in order.
      self.assertAllEqual(
          [[0., 0., 1., 1., 2., 11.], [1., 0., 0., 11., 12., 12.]],
          sess.run(
              net,

```
### Line 3722-3742
```
                  features['country']: country_data
              }))

  @test_util.run_deprecated_v1
  def test_with_rank_0_feature(self):
    # price has 1 dimension in input_layer
    price = fc.numeric_column('price')
    features = {
        'price': constant_op.constant(0),
    }
    self.assertEqual(0, features['price'].shape.ndims)

    # Static rank 0 should fail
    with self.assertRaisesRegexp(ValueError, 'Feature .* cannot have rank 0'):
      fc_old.input_layer(features, [price])

    # Dynamic rank 0 should fail
    features = {
        'price': array_ops.placeholder(dtypes.float32),
    }
    net = fc_old.input_layer(features, [price])

```
### Line 3874-3888
```
class VocabularyFileCategoricalColumnTest(test.TestCase):

  def setUp(self):
    super(VocabularyFileCategoricalColumnTest, self).setUp()

    # Contains ints, Golden State Warriors jersey numbers: 30, 35, 11, 23, 22
    self._warriors_vocabulary_file_name = test.test_src_dir_path(
        'python/feature_column/testdata/warriors_vocabulary.txt')
    self._warriors_vocabulary_size = 5

    # Contains strings, character names from 'The Wire': omar, stringer, marlo
    self._wire_vocabulary_file_name = test.test_src_dir_path(
        'python/feature_column/testdata/wire_vocabulary.txt')
    self._wire_vocabulary_size = 3


```
### Line 4221-4232
```
            dense_shape=inputs.dense_shape),
        self.evaluate(id_weight_pair.id_tensor))

  @test_util.run_deprecated_v1
  def test_get_sparse_tensors_small_vocabulary_size(self):
    # 'marlo' is the last entry in our vocabulary file, so be setting
    # `vocabulary_size` to 1 less than number of entries in file, we take
    # 'marlo' out of the vocabulary.
    column = fc.categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file=self._wire_vocabulary_file_name,
        vocabulary_size=self._wire_vocabulary_size - 1)

```
### Line 4357-4367
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 2: wire_var[2] = 3
      # 'skywalker' -> 3, 'omar' -> 0: wire_var[3] + wire_var[0] = 4+1 = 5
      self.assertAllClose(((3.,), (5.,)), self.evaluate(predictions))

  def test_old_linear_model(self):
    wire_column = fc.categorical_column_with_vocabulary_file(

```
### Line 4386-4396
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 2: wire_var[2] = 3
      # 'skywalker' -> 3, 'omar' -> 0: wire_var[3] + wire_var[0] = 4+1 = 5
      self.assertAllClose(((3.,), (5.,)), self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_serialization(self):

```
### Line 4822-4832
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 2: wire_var[2] = 3
      # 'skywalker' -> 3, 'omar' -> 0: wire_var[3] + wire_var[0] = 4+1 = 5
      self.assertAllClose(((3.,), (5.,)), self.evaluate(predictions))

  def test_old_linear_model(self):
    wire_column = fc.categorical_column_with_vocabulary_list(

```
### Line 4850-4860
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,), (0.,)), self.evaluate(wire_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(wire_var.assign(((1.,), (2.,), (3.,), (4.,))))
      # 'marlo' -> 2: wire_var[2] = 3
      # 'skywalker' -> 3, 'omar' -> 0: wire_var[3] + wire_var[0] = 4+1 = 5
      self.assertAllClose(((3.,), (5.,)), self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_serialization(self):

```
### Line 5015-5031
```
            indices=((0, 0), (1, 0), (1, 1)),
            values=np.array((0, 1, 0), dtype=np.int64),
            dense_shape=(2, 2)), self.evaluate(id_weight_pair.id_tensor))

  def _test_get_sparse_tensors_with_inputs_too_small(self):
    # Inputs.
    vocabulary_size = 2
    sparse_input = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (0, 0), (1, 1), (1, 2)),
        values=(-9, 0, -6, 1),
        dense_shape=(2, 4))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 5033-5042
```

    def _initializer(shape, dtype, partition_info=None):
      del shape, dtype, partition_info
      return embedding_values

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 5043-5052
```
        dimension=embedding_dimension,
        initializer=_initializer)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({'aaa': sparse_input}), state_manager)

    self.evaluate(variables_lib.global_variables_initializer())

```
### Line 5063-5077
```
  @test_util.enable_control_flow_v2
  def test_get_sparse_tensors_with_inputs_too_small_v2(self):
    self._test_get_sparse_tensors_with_inputs_too_small()

  def _test_get_sparse_tensors_with_inputs_too_big(self):
    # Inputs.
    vocabulary_size = 2
    sparse_input = sparse_tensor.SparseTensorValue(
        indices=((0, 0), (1, 0)), values=(2, 0), dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 5079-5088
```

    def _initializer(shape, dtype, partition_info=None):
      del shape, dtype, partition_info
      return embedding_values

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 5089-5098
```
        dimension=embedding_dimension,
        initializer=_initializer)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({'aaa': sparse_input}), state_manager)

    self.evaluate(variables_lib.global_variables_initializer())

```
### Line 5187-5197
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] = 1
      # weight_var[2] + weight_var[1] = 3+2 = 5
      self.assertAllClose(((1.,), (5.,)), self.evaluate(predictions))

  def test_old_linear_model(self):
    column = fc.categorical_column_with_identity(key='aaa', num_buckets=3)

```
### Line 5212-5222
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] = 1
      # weight_var[2] + weight_var[1] = 3+2 = 5
      self.assertAllClose(((1.,), (5.,)), self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_serialization(self):

```
### Line 5234-5244
```
    self.assertEqual(column, fc.IdentityCategoricalColumn.from_config(config))


class TransformFeaturesTest(test.TestCase):

  # All transform tests are distributed in column test.
  # Here we only test multi column case and naming
  def transform_multi_column(self):
    bucketized_price = fc.bucketized_column(
        fc.numeric_column('price'), boundaries=[0, 2, 4, 6])
    hashed_sparse = fc.categorical_column_with_hash_bucket('wire', 10)

```
### Line 5330-5339
```

    self.assertAllEqual([[0., 0., 1., 0.], [0., 0., 1., 0.]],
                        self.evaluate(output))

  def test_2D_shape_succeeds(self):
    # TODO(ispir/cassandrax): Swith to categorical_column_with_keys when ready.
    animal = fc.indicator_column(
        fc.categorical_column_with_hash_bucket('animal', 4))
    transformation_cache = fc.FeatureTransformationCache({
        'animal':

```
### Line 5426-5435
```

    self.assertAllEqual([[0, 0, 1], [1, 0, 0]], self.evaluate(indicator_tensor))

  @test_util.run_deprecated_v1
  def test_transform_with_weighted_column(self):
    # Github issue 12557
    ids = fc.categorical_column_with_vocabulary_list(
        key='ids', vocabulary_list=('a', 'b', 'c'))
    weights = fc.weighted_categorical_column(ids, 'weights')
    indicator = fc.indicator_column(weights)

```
### Line 5445-5454
```

    self.assertAllEqual([[6., 4., 3.]], self.evaluate(indicator_tensor))

  @test_util.run_deprecated_v1
  def test_transform_with_missing_value_in_weighted_column(self):
    # Github issue 12583
    ids = fc.categorical_column_with_vocabulary_list(
        key='ids', vocabulary_list=('a', 'b', 'c'))
    weights = fc.weighted_categorical_column(ids, 'weights')
    indicator = fc.indicator_column(weights)

```
### Line 5464-5473
```

    self.assertAllEqual([[0., 4., 2.]], self.evaluate(indicator_tensor))

  @test_util.run_deprecated_v1
  def test_transform_with_missing_value_in_categorical_column(self):
    # Github issue 12583
    ids = fc.categorical_column_with_vocabulary_list(
        key='ids', vocabulary_list=('a', 'b', 'c'))
    indicator = fc.indicator_column(ids)
    features = {

```
### Line 5497-5506
```
      weight_var, _ = model.variables

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # All should be zero-initialized.
      self.assertAllClose([[0.], [0.], [0.], [0.]], self.evaluate(weight_var))
      self.assertAllClose([[0.]], self.evaluate(predictions))
      self.evaluate(weight_var.assign([[1.], [2.], [3.], [4.]]))
      self.assertAllClose([[2. + 3.]], self.evaluate(predictions))

```
### Line 5519-5528
```
      weight_var = get_linear_model_column_var(animal)

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # All should be zero-initialized.
      self.assertAllClose([[0.], [0.], [0.], [0.]], self.evaluate(weight_var))
      self.assertAllClose([[0.]], self.evaluate(predictions))
      self.evaluate(weight_var.assign([[1.], [2.], [3.], [4.]]))
      self.assertAllClose([[2. + 3.]], self.evaluate(predictions))

```
### Line 5541-5550
```
      weight_var = get_linear_model_column_var(animal)

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # All should be zero-initialized.
      self.assertAllClose([[0.], [0.], [0.], [0.]], self.evaluate(weight_var))
      self.assertAllClose([[0.]], self.evaluate(predictions))
      self.evaluate(weight_var.assign([[1.], [2.], [3.], [4.]]))
      self.assertAllClose([[2. + 3.]], self.evaluate(predictions))

```
### Line 5632-5641
```


class _TestStateManager(fc.StateManager):

  def __init__(self, trainable=True):
    # Dict of feature_column to a dict of variables.
    self._all_variables = {}
    self._trainable = trainable

  def create_variable(self,

```
### Line 5814-5834
```
    _assert_sparse_tensor_value(self, self.evaluate(output_a),
                                self.evaluate(output_embedded))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 5839-5860
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 5861-5876
```
        dimension=embedding_dimension,
        initializer=_initializer)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({
            'aaa': sparse_input
        }), state_manager)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))


```
### Line 5880-5900
```
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor_old_categorical(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 5905-5940
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc_old._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column._get_dense_tensor(
        fc_old._LazyBuilder({
            'aaa': sparse_input
        }))

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))


```
### Line 5944-5964
```
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor_3d(self):
    # Inputs.
    vocabulary_size = 4
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0, 0), (1, 1, 0), (1, 1, 4), (3, 0, 0), (3, 1, 2)),
        values=(2, 0, 1, 1, 2),
        dense_shape=(4, 2, 5))

    # Embedding variable.
    embedding_dimension = 3
    embedding_values = (
        (1., 2., 4.),  # id 0
        (3., 5., 1.),  # id 1

```
### Line 5970-5992
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [[2], []], embedding = [[7, 11, 2], [0, 0, 0]]
        ((7., 11., 2.), (0., 0., 0.)),
        # example 1, ids [[], [0, 1]], embedding
        # = mean([[], [1, 2, 4] + [3, 5, 1]]) = [[0, 0, 0], [2, 3.5, 2.5]]
        ((0., 0., 0.), (2., 3.5, 2.5)),
        # example 2, ids [[], []], embedding = [[0, 0, 0], [0, 0, 0]]
        ((0., 0., 0.), (0., 0., 0.)),
        # example 3, ids [[1], [2]], embedding = [[3, 5, 1], [7, 11, 2]]
        ((3., 5., 1.), (7., 11., 2.)),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 5993-6008
```
        dimension=embedding_dimension,
        initializer=_initializer)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({
            'aaa': sparse_input
        }), state_manager)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))


```
### Line 6012-6032
```
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor_placeholder_inputs(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6037-6058
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 6059-6068
```
        dimension=embedding_dimension,
        initializer=_initializer)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    input_indices = array_ops.placeholder(dtype=dtypes.int64)
    input_values = array_ops.placeholder(dtype=dtypes.int64)
    input_shape = array_ops.placeholder(dtype=dtypes.int64)
    embedding_lookup = embedding_column.get_dense_tensor(

```
### Line 6072-6081
```
                    indices=input_indices,
                    values=input_values,
                    dense_shape=input_shape)
        }), state_manager)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))


```
### Line 6092-6112
```
                  input_shape: sparse_input.dense_shape,
              }))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor_restore_from_ckpt(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable. The checkpoint file contains _embedding_values.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6114-6135
```
    )
    ckpt_path = test.test_src_dir_path(
        'python/feature_column/testdata/embedding.ckpt')
    ckpt_tensor = 'my_embedding'

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 6137-6152
```
        ckpt_to_load_from=ckpt_path,
        tensor_name_in_ckpt=ckpt_tensor)
    state_manager = _TestStateManager()
    embedding_column.create_state(state_manager)

    # Provide sparse input and get dense result.
    embedding_lookup = embedding_column.get_dense_tensor(
        fc.FeatureTransformationCache({
            'aaa': sparse_input
        }), state_manager)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('embedding_weights:0',),
                          tuple([v.name for v in global_vars]))


```
### Line 6156-6177
```
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(embedding_lookup))

  @test_util.run_deprecated_v1
  def test_linear_model(self):
    # Inputs.
    batch_size = 4
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(batch_size, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_shape = (vocabulary_size, embedding_dimension)
    zeros_embedding_values = np.zeros(embedding_shape)


```
### Line 6179-6188
```
      self.assertAllEqual(embedding_shape, shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return zeros_embedding_values

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 6211-6258
```
      linear_weights = trainable_vars['linear_model/aaa_embedding/weights:0']

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # Predictions with all zero weights.
      self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
      self.assertAllClose(zeros_embedding_values,
                          self.evaluate(embedding_weights))
      self.assertAllClose(
          np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights))
      self.assertAllClose(np.zeros((batch_size, 1)), self.evaluate(predictions))

      # Predictions with all non-zero weights.
      self.evaluate(
          embedding_weights.assign((
              (1., 2.),  # id 0
              (3., 5.),  # id 1
              (7., 11.)  # id 2
          )))
      self.evaluate(linear_weights.assign(((4.,), (6.,))))
      # example 0, ids [2], embedding[0] = [7, 11]
      # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
      # example 2, ids [], embedding[2] = [0, 0]
      # example 3, ids [1], embedding[3] = [3, 5]
      # sum(embeddings * linear_weights)
      # = [4*7 + 6*11, 4*2 + 6*3.5, 4*0 + 6*0, 4*3 + 6*5] = [94, 29, 0, 42]
      self.assertAllClose(((94.,), (29.,), (0.,), (42.,)),
                          self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_dense_features(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6263-6296
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    l = df.DenseFeatures((embedding_column,))
    dense_features = l({'aaa': sparse_input})

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('dense_features/aaa_embedding/embedding_weights:0',),
                          tuple([v.name for v in global_vars]))
    for v in global_vars:

```
### Line 6305-6325
```
    self.assertAllEqual(embedding_values, self.evaluate(trainable_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(dense_features))

  @test_util.run_deprecated_v1
  def test_dense_features_not_trainable(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6330-6365
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_initializer,
        trainable=False)

    # Provide sparse input and get dense result.
    dense_features = df.DenseFeatures((embedding_column,))({
        'aaa': sparse_input
    })

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('dense_features/aaa_embedding/embedding_weights:0',),
                          tuple([v.name for v in global_vars]))
    self.assertItemsEqual([],

```
### Line 6371-6391
```
    self.assertAllEqual(embedding_values, self.evaluate(global_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(dense_features))

  @test_util.run_deprecated_v1
  def test_input_layer(self):
    # Inputs.
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(4, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6396-6430
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0, ids [2], embedding = [7, 11]
        (7., 11.),
        # example 1, ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        (2., 3.5),
        # example 2, ids [], embedding = [0, 0]
        (0., 0.),
        # example 3, ids [1], embedding = [3, 5]
        (3., 5.),
    )

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    feature_layer = fc_old.input_layer({
        'aaa': sparse_input
    }, (embedding_column,))

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('input_layer/aaa_embedding/embedding_weights:0',),
                          tuple([v.name for v in global_vars]))
    trainable_vars = ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)

```
### Line 6436-6457
```

    self.assertAllEqual(embedding_values, self.evaluate(trainable_vars[0]))
    self.assertAllEqual(expected_lookups, self.evaluate(feature_layer))

  def test_old_linear_model(self):
    # Inputs.
    batch_size = 4
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(batch_size, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_shape = (vocabulary_size, embedding_dimension)
    zeros_embedding_values = np.zeros(embedding_shape)


```
### Line 6459-6468
```
      self.assertAllEqual(embedding_shape, shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return zeros_embedding_values

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 6492-6539
```
      linear_weights = trainable_vars['linear_model/aaa_embedding/weights:0']

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # Predictions with all zero weights.
      self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
      self.assertAllClose(zeros_embedding_values,
                          self.evaluate(embedding_weights))
      self.assertAllClose(
          np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights))
      self.assertAllClose(np.zeros((batch_size, 1)), self.evaluate(predictions))

      # Predictions with all non-zero weights.
      self.evaluate(
          embedding_weights.assign((
              (1., 2.),  # id 0
              (3., 5.),  # id 1
              (7., 11.)  # id 2
          )))
      self.evaluate(linear_weights.assign(((4.,), (6.,))))
      # example 0, ids [2], embedding[0] = [7, 11]
      # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
      # example 2, ids [], embedding[2] = [0, 0]
      # example 3, ids [1], embedding[3] = [3, 5]
      # sum(embeddings * linear_weights)
      # = [4*7 + 6*11, 4*2 + 6*3.5, 4*0 + 6*0, 4*3 + 6*5] = [94, 29, 0, 42]
      self.assertAllClose(((94.,), (29.,), (0.,), (42.,)),
                          self.evaluate(predictions))

  def test_old_linear_model_old_categorical(self):
    # Inputs.
    batch_size = 4
    vocabulary_size = 3
    sparse_input = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        # example 2, ids []
        # example 3, ids [1]
        indices=((0, 0), (1, 0), (1, 4), (3, 0)),
        values=(2, 0, 1, 1),
        dense_shape=(batch_size, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_shape = (vocabulary_size, embedding_dimension)
    zeros_embedding_values = np.zeros(embedding_shape)


```
### Line 6541-6550
```
      self.assertAllEqual(embedding_shape, shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return zeros_embedding_values

    # Build columns.
    categorical_column = fc_old._categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    embedding_column = fc.embedding_column(
        categorical_column,

```
### Line 6574-6611
```
      linear_weights = trainable_vars['linear_model/aaa_embedding/weights:0']

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # Predictions with all zero weights.
      self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
      self.assertAllClose(zeros_embedding_values,
                          self.evaluate(embedding_weights))
      self.assertAllClose(
          np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights))
      self.assertAllClose(np.zeros((batch_size, 1)), self.evaluate(predictions))

      # Predictions with all non-zero weights.
      self.evaluate(
          embedding_weights.assign((
              (1., 2.),  # id 0
              (3., 5.),  # id 1
              (7., 11.)  # id 2
          )))
      self.evaluate(linear_weights.assign(((4.,), (6.,))))
      # example 0, ids [2], embedding[0] = [7, 11]
      # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
      # example 2, ids [], embedding[2] = [0, 0]
      # example 3, ids [1], embedding[3] = [3, 5]
      # sum(embeddings * linear_weights)
      # = [4*7 + 6*11, 4*2 + 6*3.5, 4*0 + 6*0, 4*3 + 6*5] = [94, 29, 0, 42]
      self.assertAllClose(((94.,), (29.,), (0.,), (42.,)),
                          self.evaluate(predictions))

  @test_util.run_deprecated_v1
  def test_serialization_with_default_initializer(self):

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    embedding_column = fc.embedding_column(categorical_column, dimension=2)


```
### Line 6662-6671
```

    def _initializer(shape, dtype, partition_info=None):
      del shape, dtype, partition_info
      return ValueError('Not expected to be called')

    # Build columns.
    categorical_column = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    embedding_column = fc.embedding_column(
        categorical_column, dimension=2, initializer=_initializer)

```
### Line 6918-6929
```
    _assert_sparse_tensor_value(self, self.evaluate(output_b),
                                self.evaluate(output_b_embedded))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor(self):
    # Inputs.
    vocabulary_size = 3
    # -1 values are ignored.
    input_a = np.array([
        [2, -1, -1],  # example 0, ids [2]
        [0, 1, -1]
    ])  # example 1, ids [0, 1]

```
### Line 6931-6940
```
        [0, -1, -1],  # example 0, ids [0]
        [-1, -1, -1]
    ])  # example 1, ids []
    input_features = {'aaa': input_a, 'bbb': input_b}

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 6945-6968
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups_a = (
        # example 0:
        (7., 11.),  # ids [2], embedding = [7, 11]
        # example 1:
        (2., 3.5),  # ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
    )
    expected_lookups_b = (
        # example 0:
        (1., 2.),  # ids [0], embedding = [1, 2]
        # example 1:
        (0., 0.),  # ids [], embedding = [0, 0]
    )

    # Build columns.
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

```
### Line 6969-6984
```
    embedding_column_a, embedding_column_b = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    embedding_lookup_a = embedding_column_a.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)
    embedding_lookup_b = embedding_column_b.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(('aaa_bbb_shared_embedding:0',),
                          tuple([v.name for v in global_vars]))
    embedding_var = global_vars[0]

```
### Line 6990-7010
```
    self.assertAllEqual(expected_lookups_a, self.evaluate(embedding_lookup_a))
    self.assertAllEqual(expected_lookups_b, self.evaluate(embedding_lookup_b))

  @test_util.run_deprecated_v1
  def test_get_dense_tensor_placeholder_inputs(self):
    # Inputs.
    vocabulary_size = 3
    # -1 values are ignored.
    input_a = np.array([
        [2, -1, -1],  # example 0, ids [2]
        [0, 1, -1]
    ])  # example 1, ids [0, 1]
    input_b = np.array([
        [0, -1, -1],  # example 0, ids [0]
        [-1, -1, -1]
    ])  # example 1, ids []
    # Specify shape, because dense input must have rank specified.
    input_a_placeholder = array_ops.placeholder(
        dtype=dtypes.int64, shape=[None, 3])
    input_b_placeholder = array_ops.placeholder(
        dtype=dtypes.int64, shape=[None, 3])

```
### Line 7015-7024
```
    feed_dict = {
        input_a_placeholder: input_a,
        input_b_placeholder: input_b,
    }

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 7029-7038
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Build columns.
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

```
### Line 7039-7048
```
    embedding_column_a, embedding_column_b = fc.shared_embedding_columns_v2(
        [categorical_column_a, categorical_column_b],
        dimension=embedding_dimension,
        initializer=_initializer)

    # Provide sparse input and get dense result.
    embedding_lookup_a = embedding_column_a.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)
    embedding_lookup_b = embedding_column_b.get_dense_tensor(
        fc.FeatureTransformationCache(input_features), None)

```
### Line 7050-7062
```
    with _initialized_session() as sess:
      sess.run([embedding_lookup_a, embedding_lookup_b], feed_dict=feed_dict)

  @test_util.run_deprecated_v1
  def test_linear_model(self):
    # Inputs.
    batch_size = 2
    vocabulary_size = 3
    # -1 values are ignored.
    input_a = np.array([
        [2, -1, -1],  # example 0, ids [2]
        [0, 1, -1]
    ])  # example 1, ids [0, 1]

```
### Line 7063-7072
```
    input_b = np.array([
        [0, -1, -1],  # example 0, ids [0]
        [-1, -1, -1]
    ])  # example 1, ids []

    # Embedding variable.
    embedding_dimension = 2
    embedding_shape = (vocabulary_size, embedding_dimension)
    zeros_embedding_values = np.zeros(embedding_shape)


```
### Line 7074-7083
```
      self.assertAllEqual(embedding_shape, shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return zeros_embedding_values

    # Build columns.
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

```
### Line 7091-7101
```
      predictions = model({
          categorical_column_a.name: input_a,
          categorical_column_b.name: input_b
      })

      # Linear weights do not follow the column name. But this is a rare use
      # case, and fixing it would add too much complexity to the code.
      expected_var_names = (
          'linear_model/bias_weights:0',
          'linear_model/aaa_shared_embedding/weights:0',
          'aaa_bbb_shared_embedding:0',

```
### Line 7117-7126
```
          'linear_model/bbb_shared_embedding/weights:0']

      self.evaluate(variables_lib.global_variables_initializer())
      self.evaluate(lookup_ops.tables_initializer())

      # Predictions with all zero weights.
      self.assertAllClose(np.zeros((1,)), self.evaluate(bias))
      self.assertAllClose(zeros_embedding_values,
                          self.evaluate(embedding_weights))
      self.assertAllClose(

```
### Line 7127-7183
```
          np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights_a))
      self.assertAllClose(
          np.zeros((embedding_dimension, 1)), self.evaluate(linear_weights_b))
      self.assertAllClose(np.zeros((batch_size, 1)), self.evaluate(predictions))

      # Predictions with all non-zero weights.
      self.evaluate(
          embedding_weights.assign((
              (1., 2.),  # id 0
              (3., 5.),  # id 1
              (7., 11.)  # id 2
          )))
      self.evaluate(linear_weights_a.assign(((4.,), (6.,))))
      # example 0, ids [2], embedding[0] = [7, 11]
      # example 1, ids [0, 1], embedding[1] = mean([1, 2] + [3, 5]) = [2, 3.5]
      # sum(embeddings * linear_weights)
      # = [4*7 + 6*11, 4*2 + 6*3.5] = [94, 29]
      self.evaluate(linear_weights_b.assign(((3.,), (5.,))))
      # example 0, ids [0], embedding[0] = [1, 2]
      # example 1, ids [], embedding[1] = 0, 0]
      # sum(embeddings * linear_weights)
      # = [3*1 + 5*2, 3*0 +5*0] = [13, 0]
      self.assertAllClose([[94. + 13.], [29.]], self.evaluate(predictions))

  def _test_dense_features(self, trainable=True):
    # Inputs.
    vocabulary_size = 3
    sparse_input_a = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        indices=((0, 0), (1, 0), (1, 4)),
        values=(2, 0, 1),
        dense_shape=(2, 5))
    sparse_input_b = sparse_tensor.SparseTensorValue(
        # example 0, ids [0]
        # example 1, ids []
        indices=((0, 0),),
        values=(0,),
        dense_shape=(2, 5))
    sparse_input_c = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids [0, 1]
        indices=((0, 1), (1, 1), (1, 3)),
        values=(2, 0, 1),
        dense_shape=(2, 5))
    sparse_input_d = sparse_tensor.SparseTensorValue(
        # example 0, ids [2]
        # example 1, ids []
        indices=((0, 1),),
        values=(2,),
        dense_shape=(2, 5))

    # Embedding variable.
    embedding_dimension = 2
    embedding_values = (
        (1., 2.),  # id 0
        (3., 5.),  # id 1

```
### Line 7188-7213
```
      self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
      self.assertEqual(dtypes.float32, dtype)
      self.assertIsNone(partition_info)
      return embedding_values

    # Expected lookup result, using combiner='mean'.
    expected_lookups = (
        # example 0:
        # A ids [2], embedding = [7, 11]
        # B ids [0], embedding = [1, 2]
        # C ids [2], embedding = [7, 11]
        # D ids [2], embedding = [7, 11]
        (7., 11., 1., 2., 7., 11., 7., 11.),
        # example 1:
        # A ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        # B ids [], embedding = [0, 0]
        # C ids [0, 1], embedding = mean([1, 2] + [3, 5]) = [2, 3.5]
        # D ids [], embedding = [0, 0]
        (2., 3.5, 0., 0., 2., 3.5, 0., 0.),
    )

    # Build columns.
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=vocabulary_size)
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=vocabulary_size)

```
### Line 7232-7247
```
        'bbb': sparse_input_b,
        'ccc': sparse_input_c,
        'ddd': sparse_input_d
    }

    # Provide sparse input and get dense result.
    dense_features = df.DenseFeatures(
        feature_columns=(embedding_column_b, embedding_column_a,
                         embedding_column_c, embedding_column_d))(
                             features)

    # Assert expected embedding variable and lookups.
    global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    self.assertItemsEqual(
        ['aaa_bbb_shared_embedding:0', 'ccc_ddd_shared_embedding:0'],
        tuple([v.name for v in global_vars]))

```
### Line 7287-7296
```
        dimension=2,
        initializer=_initializer)

    self.assertEqual([categorical_column_a], embedding_column_a.parents)
    self.assertEqual([categorical_column_b], embedding_column_b.parents)
    # TODO(rohanj): Add tests for (from|get)_config once implemented


class WeightedCategoricalColumnTest(test.TestCase):


```
### Line 7536-7547
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] * weights[0, 0] = 1 * .5 = .5
      # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
      # = 3*1 + 2*.1 = 3+.2 = 3.2
      self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))

  def test_linear_model_mismatched_shape(self):
    column = fc.weighted_categorical_column(

```
### Line 7578-7588
```
                  indices=((0, 0), (1, 0), (1, 1)),
                  values=(0, 2, 1),
                  dense_shape=(2, 2)),
          'values': ((.5,), (1.,))
      })
      # Disabling the constant folding optimizer here since it changes the
      # error message differently on CPU and GPU.
      config = config_pb2.ConfigProto()
      config.graph_options.rewrite_options.constant_folding = (
          rewriter_config_pb2.RewriterConfig.OFF)
      with _initialized_session(config):

```
### Line 7611-7622
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] * weights[0, 0] = 1 * .5 = .5
      # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
      # = 3*1 + 2*.1 = 3+.2 = 3.2
      self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))

  def test_old_linear_model(self):
    column = fc.weighted_categorical_column(

```
### Line 7644-7655
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] * weights[0, 0] = 1 * .5 = .5
      # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
      # = 3*1 + 2*.1 = 3+.2 = 3.2
      self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))

  def test_old_linear_model_mismatched_shape(self):
    column = fc.weighted_categorical_column(

```
### Line 7685-7695
```
                  values=(0, 2, 1),
                  dense_shape=(2, 2)),
          'values': ((.5,), (1.,))
      }, (column,),
                                        sparse_combiner='mean')
      # Disabling the constant folding optimizer here since it changes the
      # error message differently on CPU and GPU.
      config = config_pb2.ConfigProto()
      config.graph_options.rewrite_options.constant_folding = (
          rewriter_config_pb2.RewriterConfig.OFF)
      with _initialized_session(config):

```
### Line 7718-7729
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] * weights[0, 0] = 1 * .5 = .5
      # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
      # = 3*1 + 2*.1 = 3+.2 = 3.2
      self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))

  def test_old_linear_model_old_categorical(self):
    column = fc.weighted_categorical_column(

```
### Line 7751-7765
```

      self.assertAllClose((0.,), self.evaluate(bias))
      self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
      self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
      self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
      # weight_var[0] * weights[0, 0] = 1 * .5 = .5
      # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
      # = 3*1 + 2*.1 = 3+.2 = 3.2
      self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))

  # TODO(ptucker): Add test with embedding of weighted categorical.

  @test_util.run_deprecated_v1
  def test_serialization(self):
    categorical_column = fc.categorical_column_with_identity(

```

## _tensorflow_tools_ci_build_release_ubuntu_16_cpu_py2_full_nightly_release_sh
### Line 1-48
```
#!/bin/bash
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
set -e
set -x

source "tensorflow/tools/ci_build/release/common.sh"

set_bazel_outdir

# Install python dependencies
install_ubuntu_16_pip_deps pip2.7

python2.7 tensorflow/tools/ci_build/update_version.py --nightly

# Run configure.
export TF_NEED_GCP=1
export TF_NEED_HDFS=1
export TF_NEED_S3=1
export TF_NEED_CUDA=0
export CC_OPT_FLAGS='-mavx'
export PYTHON_BIN_PATH=$(which python2.7)
yes "" | "$PYTHON_BIN_PATH" configure.py

# Build the pip package
bazel build --config=opt --config=v2 \
  --crosstool_top=//third_party/toolchains/preconfig/ubuntu16.04/gcc7_manylinux2010-nvcc-cuda10.0:toolchain \
  tensorflow/tools/pip_package:build_pip_package

./bazel-bin/tensorflow/tools/pip_package/build_pip_package pip_pkg --cpu --nightly_flag

# Upload the built packages to pypi.
for WHL_PATH in $(ls pip_pkg/tf_nightly_cpu-*dev*.whl); do

  WHL_DIR=$(dirname "${WHL_PATH}")
  WHL_BASE_NAME=$(basename "${WHL_PATH}")

```

## _tensorflow_python_autograph_lang_special_functions_test_py
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
"""Tests for special_functions module."""

from __future__ import absolute_import
from __future__ import division

```
### Line 88-97
```

  def test_stack(self):
    self.assertEqual(special_functions.stack(1, strict=False), 1)
    self.assertListEqual(
        special_functions.stack([1, 2, 3], strict=False), [1, 2, 3])
    # TODO(mdan): This should probably forward to tf.stack.
    self.assertTrue(
        isinstance(
            special_functions.stack(
                [constant_op.constant(1),

```

## _tensorflow_python_ops_ragged_ragged_const_op_test_py
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
"""Tests for ragged_factory_ops.constant."""

from __future__ import absolute_import
from __future__ import division

```
### Line 32-55
```
@test_util.run_all_in_graph_and_eager_modes
class RaggedConstOpTest(test_util.TensorFlowTestCase,
                        parameterized.TestCase):

  @parameterized.parameters(
      #=========================================================================
      # 0-dimensional tensors.
      dict(pylist=b'x', expected_shape=()),

      #=========================================================================
      # 1-dimensional tensors.
      dict(pylist=[1, 2, 3], expected_shape=(3,)),

      #=========================================================================
      # 2-dimensional tensors.
      dict(pylist=[[1, 2, 3], [4], [5, 6]], expected_shape=(3, None)),
      dict(pylist=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], expected_shape=(3, None)),

      #=========================================================================
      # 3-dimensional tensors.
      dict(
          pylist=[[[1, 2], [3, 4]], [], [[5, 6], [7, 8], [9, 0]]],
          expected_shape=(3, None, None)),
      dict(

```
### Line 63-72
```
      dict(
          pylist=[[[1, 2], [3, 4]], [], [[5, 6], [7, 8], [9, 0]]],
          ragged_rank=1,
          inner_shape=(2,),
          expected_shape=(3, None, 2)),
      # 3-dimensional tensors with numpy arrays
      dict(
          pylist=[[[1, 2], np.array([3, np.array(4)])],
                  np.array([]), [[5, 6], [7, 8], [9, 0]]],
          expected_shape=(3, None, None)),

```
### Line 84-94
```
          pylist=[[[1, 2], np.array([3, np.array(4)])],
                  np.array([]), [[5, 6], [7, 8], [9, 0]]],
          ragged_rank=1,
          inner_shape=(2,),
          expected_shape=(3, None, 2)),
      #=========================================================================
      # 4-dimensional tensors.
      dict(
          pylist=[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                  [[[2, 4], [6, 8]], [[1, 5], [7, 9]]]],
          expected_shape=(2, None, None, None)),

```
### Line 105-121
```
      dict(
          pylist=[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                  [[[2, 4], [6, 8]], [[1, 5], [7, 9]]]],
          inner_shape=(2, 2),
          expected_shape=(2, None, 2, 2)),
      # 4-dimensional tensors with numpy arrays
      dict(
          pylist=np.array([[[np.array([1, 2]), [3, 4]], [[5, 6], [7, 8]]],
                           np.array([[[2, 4], [6, 8]], [[1, 5], [7, 9]]])]),
          expected_shape=(2, None, None, None)),

      #=========================================================================
      # Empty tensors (no scalar values) w/ default ragged_rank and inner_shape
      dict(pylist=[], expected_shape=(0,)),
      dict(pylist=[[], [], np.array([])], expected_shape=(3, None)),
      dict(
          pylist=[[[], []], [], [[], [[]]]],

```
### Line 123-133
```
      dict(
          pylist=np.array([np.array([[], []]),
                           np.array([]), [[], [[]]]]),
          expected_shape=(3, None, None, None)),

      #=========================================================================
      # Empty tensors (no scalar values) w/ explicit ragged_rank or inner_shape
      dict(pylist=[], ragged_rank=1, expected_shape=(0, None)),
      dict(pylist=[], ragged_rank=2, expected_shape=(0, None, None)),
      dict(pylist=[], inner_shape=(0, 100, 20), expected_shape=(0, 100, 20)),
      dict(

```
### Line 147-157
```
          pylist=np.array([]),
          ragged_rank=1,
          inner_shape=(100, 20),
          expected_shape=(0, None, 100, 20)),

      #=========================================================================
      # default/inferred dtypes
      dict(pylist=[], expected_dtype=dtypes.float32),
      dict(pylist=[[[], [[[]], []]]], expected_dtype=dtypes.float32),
      dict(pylist=[[1, 2], [3], [4, 5, 6]], expected_dtype=dtypes.int32),
      dict(pylist=[[1., 2.], [], [4., 5., 6.]], expected_dtype=dtypes.float32),

```
### Line 160-170
```
      dict(pylist=[[True]], expected_dtype=dtypes.bool),
      dict(
          pylist=[np.array([1, 2]), np.array([3.]), [4, 5, 6]],
          expected_dtype=dtypes.float32),

      #=========================================================================
      # explicit dtypes
      dict(pylist=[], dtype=dtypes.float32),
      dict(pylist=[], dtype=dtypes.string),
      dict(pylist=[[1, 2], [3], [4, 5, 6]], dtype=dtypes.int64),
      dict(pylist=[[1, 2], [3], [4, 5, 6]], dtype=dtypes.int32),

```
### Line 198-224
```
      expected_dtype: The expected dtype for the resulting ragged tensor (used
        to test default/inferred types when dtype=None).
    """
    rt = ragged_factory_ops.constant(
        pylist, dtype=dtype, ragged_rank=ragged_rank, inner_shape=inner_shape)
    # Normalize the pylist, i.e., convert all np.arrays to list.
    # E.g., [np.array((1,2))] --> [[1,2]]
    pylist = _normalize_pylist(pylist)

    # If dtype was explicitly specified, check it.
    if dtype is not None:
      self.assertEqual(rt.dtype, dtype)
    if expected_dtype is not None:
      self.assertEqual(rt.dtype, expected_dtype)

    # If ragged_rank was explicitly specified, check it.
    if ragged_rank is not None:
      if isinstance(rt, ragged_tensor.RaggedTensor):
        self.assertEqual(rt.ragged_rank, ragged_rank)
      else:
        self.assertEqual(0, ragged_rank)

    # If inner_shape was explicitly specified, check it.
    if inner_shape is not None:
      if isinstance(rt, ragged_tensor.RaggedTensor):
        self.assertEqual(rt.flat_values.shape.as_list()[1:], list(inner_shape))
      else:

```
### Line 401-410
```
              pylist, ragged_rank), inner_shape)


def _normalize_pylist(item):
  """Convert all (possibly nested) np.arrays contained in item to list."""
  # convert np.arrays in current level to list
  if np.ndim(item) == 0:
    return item
  level = (x.tolist() if isinstance(x, np.ndarray) else x for x in item)
  return [_normalize_pylist(el) if np.ndim(el) != 0 else el for el in level]

```

## _tensorflow_python_distribute_multi_process_runner_test_py
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
"""Tests for `multi_process_runner`."""

from __future__ import absolute_import
from __future__ import division

```
### Line 145-155
```
        proc_func_that_does_nothing,
        multi_process_runner.job_count_to_cluster_spec(job_count_dict),
        time_to_exit=10)
    time.sleep(15)
    with self.assertRaisesRegexp(Queue.Empty, ''):
      # If the signal was fired, another message would be added to internal
      # queue, so verifying it's empty.
      multi_process_runner._get_internal_queue().get(block=False)


if __name__ == '__main__':

```

## _tensorflow_lite_experimental_micro_examples_micro_speech_apollo3_compare_1k_py
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
"""Debugging script for checking calculation values."""

from __future__ import absolute_import
from __future__ import division

```
### Line 20-29
```

import struct
import matplotlib.pyplot as plt
import numpy as np

# import soundfile as sf


def new_data_to_array(fn, datatype='int16'):
  """Converts file information to an in-memory array."""

```
### Line 56-65
```
  y = np.array(struct.unpack('<' + typestr * arraylen, b))

  return y


# x is the fixed-point input in Qm.n format
def to_float(x, n):
  return x.astype(float) * 2**(-n)



```
### Line 101-111
```
plt.subplot(312)
plt.plot(cmsis_dft, label='CMSIS fixed')
plt.legend()
plt.subplot(313)
plt.plot(to_float(micro_dft, 22), label='Micro to float')
# CMSIS result has 6 fractionanl bits (not 7) due to documentation error (see
# README.md)
plt.plot(to_float(cmsis_dft, 6), label='CMSIS to float')
plt.plot(py_result, label='Python result')
plt.legend()


```
### Line 126-167
```
plt.plot(micro_power_avg, label='Micro fixed')
plt.plot(cmsis_power_avg, label='CMSIS fixed')
plt.legend()
plt.show()

# t = np.arange(16000.*0.03)/16000.
# # Factor of 10 because micro preprocessing overflows otherwise
# sin1k = 0.1*np.sin(2*np.pi*1000*t)
#
# plt.figure(1)
# plt.subplot(511)
# plt.plot(sin1k)
# plt.title('Input sine')
#
# plt.subplot(512)
# plt.plot(to_float(micro_windowed_input, 30), label='Micro-Lite')
# plt.plot(to_float(cmsis_windowed_input, 15), label='CMSIS')
# plt.title('Windowed sine')
# plt.legend(loc='center right')
#
# plt.subplot(513)
# plt.plot(to_float(micro_dft, 22), label='Micro-Lite')
# plt.plot(to_float(cmsis_dft, 6), label='CMSIS')
# plt.title('FFT')
# plt.legend(loc='center')
#
# plt.subplot(514)
# plt.plot(to_float(micro_power, 22), label='Micro-Lite')
# plt.plot(to_float(cmsis_power[0:256], 6), label='CMSIS')
# plt.title('|FFT|^2')
# plt.legend(loc='center right')
#
# plt.subplot(515)
# plt.plot(micro_power_avg, label='Micro-Lite')
# plt.plot(cmsis_power_avg, label='CMSIS')
# plt.title('Averaged |FFT|^2')
# plt.legend(loc='center right')
#
# plt.tight_layout(pad=0, w_pad=0.2, h_pad=0.2)
#
# plt.show()
#

```

## _tensorflow_python_training_tracking_benchmarks_test_py
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
"""Benchmarks for checkpoint-related APIs."""

from __future__ import absolute_import
from __future__ import division

```

## _tensorflow_tools_ci_build_devtoolset_rpm_patch_sh
### Line 1-21
```
#!/bin/bash -eu
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
# Given an RPM spec file $1, apply its patches.

SPEC="$1"
grep '%patch' "${SPEC}" |while read cmd ; do
  N=$(echo "${cmd}" |sed 's,%patch\([0-9]\+\).*,\1,')

```

## _tensorflow_python_distribute_cluster_resolver_gce_cluster_resolver_test_py
### Line 1-18
```
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for GCEClusterResolver."""

from __future__ import absolute_import
from __future__ import division

```

## _third_party_mlir_lib_Transforms_LoopFusion_cpp
### Line 1-64
```
//===- LoopFusion.cpp - Code to perform loop fusion -----------------------===//
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
// This file implements loop fusion.
//
//===----------------------------------------------------------------------===//

#include "mlir/Analysis/AffineAnalysis.h"
#include "mlir/Analysis/AffineStructures.h"
#include "mlir/Analysis/LoopAnalysis.h"
#include "mlir/Analysis/Utils.h"
#include "mlir/Dialect/AffineOps/AffineOps.h"
#include "mlir/Dialect/StandardOps/Ops.h"
#include "mlir/IR/AffineExpr.h"
#include "mlir/IR/AffineMap.h"
#include "mlir/IR/Builders.h"
#include "mlir/Pass/Pass.h"
#include "mlir/Transforms/LoopFusionUtils.h"
#include "mlir/Transforms/LoopUtils.h"
#include "mlir/Transforms/Passes.h"
#include "mlir/Transforms/Utils.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/DenseSet.h"
#include "llvm/ADT/SetVector.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/Debug.h"
#include "llvm/Support/raw_ostream.h"
#include <iomanip>
#include <sstream>
#define DEBUG_TYPE "affine-loop-fusion"

using llvm::SetVector;

using namespace mlir;

static llvm::cl::OptionCategory clOptionsCategory(DEBUG_TYPE " options");

/// Disables fusion profitability check and fuses if valid. Ignore any
/// additional (redundant) computation tolerance threshold
/// that would have prevented fusion.
static llvm::cl::opt<bool>
    clMaximalLoopFusion("fusion-maximal",
                        llvm::cl::desc("Enables maximal loop fusion"),
                        llvm::cl::cat(clOptionsCategory));

/// A threshold in percent of additional computation allowed when fusing.
static llvm::cl::opt<double> clFusionAddlComputeTolerance(
    "fusion-compute-tolerance",
    llvm::cl::desc("Fractional increase in additional "
                   "computation tolerated while fusing"),

```
### Line 67-93
```
static llvm::cl::opt<unsigned> clFusionFastMemorySpace(
    "fusion-fast-mem-space",
    llvm::cl::desc("Faster memory space number to promote fusion buffers to"),
    llvm::cl::cat(clOptionsCategory));

// A local buffer of size less than or equal to this size is automatically
// promoted to fast memory after producer-consumer fusion.
static llvm::cl::opt<unsigned long long> clFusionLocalBufThreshold(
    "fusion-local-buf-threshold",
    llvm::cl::desc("Threshold size (KiB) for promoting local buffers to fast "
                   "memory space"),
    llvm::cl::cat(clOptionsCategory));

namespace {

/// Loop fusion pass. This pass currently supports a greedy fusion policy,
/// which fuses loop nests with single-writer/single-reader memref dependences
/// with the goal of improving locality.

// TODO(andydavis) Support fusion of source loop nests which write to multiple
// memrefs, where each memref can have multiple users (if profitable).
// TODO(andydavis) Extend this pass to check for fusion preventing dependences,
// and add support for more general loop fusion algorithms.

struct LoopFusion : public FunctionPass<LoopFusion> {
  LoopFusion(unsigned fastMemorySpace = 0, uint64_t localBufSizeThreshold = 0,
             bool maximalFusion = false)

```
### Line 94-112
```
      : localBufSizeThreshold(localBufSizeThreshold),
        fastMemorySpace(fastMemorySpace), maximalFusion(maximalFusion) {}

  void runOnFunction() override;

  // Any local buffers smaller than this size (in bytes) will be created in
  // `fastMemorySpace` if provided.
  uint64_t localBufSizeThreshold;
  Optional<unsigned> fastMemorySpace = None;
  // If true, ignore any additional (redundant) computation tolerance threshold
  // that would have prevented fusion.
  bool maximalFusion;

  // The amount of additional computation that is tolerated while fusing
  // pair-wise as a fraction of the total computation.
  constexpr static double kComputeToleranceThreshold = 0.30f;
};

} // end anonymous namespace

```
### Line 118-128
```
                                      maximalFusion);
}

namespace {

// LoopNestStateCollector walks loop nests and collects load and store
// operations, and whether or not an IfInst was encountered in the loop nest.
struct LoopNestStateCollector {
  SmallVector<AffineForOp, 4> forOps;
  SmallVector<Operation *, 4> loadOpInsts;
  SmallVector<Operation *, 4> storeOpInsts;

```
### Line 140-178
```
        storeOpInsts.push_back(op);
    });
  }
};

// TODO(b/117228571) Replace when this is modeled through side-effects/op traits
static bool isMemRefDereferencingOp(Operation &op) {
  if (isa<AffineLoadOp>(op) || isa<AffineStoreOp>(op) ||
      isa<AffineDmaStartOp>(op) || isa<AffineDmaWaitOp>(op))
    return true;
  return false;
}

// MemRefDependenceGraph is a graph data structure where graph nodes are
// top-level operations in a FuncOp which contain load/store ops, and edges
// are memref dependences between the nodes.
// TODO(andydavis) Add a more flexible dependence graph representation.
// TODO(andydavis) Add a depth parameter to dependence graph construction.
struct MemRefDependenceGraph {
public:
  // Node represents a node in the graph. A Node is either an entire loop nest
  // rooted at the top level which contains loads/stores, or a top level
  // load/store.
  struct Node {
    // The unique identifier of this node in the graph.
    unsigned id;
    // The top-level statement which is (or contains) a load/store.
    Operation *op;
    // List of load operations.
    SmallVector<Operation *, 4> loads;
    // List of store op insts.
    SmallVector<Operation *, 4> stores;
    Node(unsigned id, Operation *op) : id(id), op(op) {}

    // Returns the load op count for 'memref'.
    unsigned getLoadOpCount(Value *memref) {
      unsigned loadOpCount = 0;
      for (auto *loadOpInst : loads) {
        if (memref == cast<AffineLoadOp>(loadOpInst).getMemRef())

```
### Line 179-188
```
          ++loadOpCount;
      }
      return loadOpCount;
    }

    // Returns the store op count for 'memref'.
    unsigned getStoreOpCount(Value *memref) {
      unsigned storeOpCount = 0;
      for (auto *storeOpInst : stores) {
        if (memref == cast<AffineStoreOp>(storeOpInst).getMemRef())

```
### Line 189-217
```
          ++storeOpCount;
      }
      return storeOpCount;
    }

    // Returns all store ops in 'storeOps' which access 'memref'.
    void getStoreOpsForMemref(Value *memref,
                              SmallVectorImpl<Operation *> *storeOps) {
      for (auto *storeOpInst : stores) {
        if (memref == cast<AffineStoreOp>(storeOpInst).getMemRef())
          storeOps->push_back(storeOpInst);
      }
    }

    // Returns all load ops in 'loadOps' which access 'memref'.
    void getLoadOpsForMemref(Value *memref,
                             SmallVectorImpl<Operation *> *loadOps) {
      for (auto *loadOpInst : loads) {
        if (memref == cast<AffineLoadOp>(loadOpInst).getMemRef())
          loadOps->push_back(loadOpInst);
      }
    }

    // Returns all memrefs in 'loadAndStoreMemrefSet' for which this node
    // has at least one load and store operation.
    void getLoadAndStoreMemrefSet(DenseSet<Value *> *loadAndStoreMemrefSet) {
      llvm::SmallDenseSet<Value *, 2> loadMemrefs;
      for (auto *loadOpInst : loads) {
        loadMemrefs.insert(cast<AffineLoadOp>(loadOpInst).getMemRef());

```
### Line 222-387
```
          loadAndStoreMemrefSet->insert(memref);
      }
    }
  };

  // Edge represents a data dependence between nodes in the graph.
  struct Edge {
    // The id of the node at the other end of the edge.
    // If this edge is stored in Edge = Node.inEdges[i], then
    // 'Node.inEdges[i].id' is the identifier of the source node of the edge.
    // If this edge is stored in Edge = Node.outEdges[i], then
    // 'Node.outEdges[i].id' is the identifier of the dest node of the edge.
    unsigned id;
    // The SSA value on which this edge represents a dependence.
    // If the value is a memref, then the dependence is between graph nodes
    // which contain accesses to the same memref 'value'. If the value is a
    // non-memref value, then the dependence is between a graph node which
    // defines an SSA value and another graph node which uses the SSA value
    // (e.g. a constant operation defining a value which is used inside a loop
    // nest).
    Value *value;
  };

  // Map from node id to Node.
  DenseMap<unsigned, Node> nodes;
  // Map from node id to list of input edges.
  DenseMap<unsigned, SmallVector<Edge, 2>> inEdges;
  // Map from node id to list of output edges.
  DenseMap<unsigned, SmallVector<Edge, 2>> outEdges;
  // Map from memref to a count on the dependence edges associated with that
  // memref.
  DenseMap<Value *, unsigned> memrefEdgeCount;
  // The next unique identifier to use for newly created graph nodes.
  unsigned nextNodeId = 0;

  MemRefDependenceGraph() {}

  // Initializes the dependence graph based on operations in 'f'.
  // Returns true on success, false otherwise.
  bool init(FuncOp f);

  // Returns the graph node for 'id'.
  Node *getNode(unsigned id) {
    auto it = nodes.find(id);
    assert(it != nodes.end());
    return &it->second;
  }

  // Returns the graph node for 'forOp'.
  Node *getForOpNode(AffineForOp forOp) {
    for (auto &idAndNode : nodes)
      if (idAndNode.second.op == forOp.getOperation())
        return &idAndNode.second;
    return nullptr;
  }

  // Adds a node with 'op' to the graph and returns its unique identifier.
  unsigned addNode(Operation *op) {
    Node node(nextNodeId++, op);
    nodes.insert({node.id, node});
    return node.id;
  }

  // Remove node 'id' (and its associated edges) from graph.
  void removeNode(unsigned id) {
    // Remove each edge in 'inEdges[id]'.
    if (inEdges.count(id) > 0) {
      SmallVector<Edge, 2> oldInEdges = inEdges[id];
      for (auto &inEdge : oldInEdges) {
        removeEdge(inEdge.id, id, inEdge.value);
      }
    }
    // Remove each edge in 'outEdges[id]'.
    if (outEdges.count(id) > 0) {
      SmallVector<Edge, 2> oldOutEdges = outEdges[id];
      for (auto &outEdge : oldOutEdges) {
        removeEdge(id, outEdge.id, outEdge.value);
      }
    }
    // Erase remaining node state.
    inEdges.erase(id);
    outEdges.erase(id);
    nodes.erase(id);
  }

  // Returns true if node 'id' writes to any memref which escapes (or is an
  // argument to) the function/block. Returns false otherwise.
  bool writesToLiveInOrEscapingMemrefs(unsigned id) {
    Node *node = getNode(id);
    for (auto *storeOpInst : node->stores) {
      auto *memref = cast<AffineStoreOp>(storeOpInst).getMemRef();
      auto *op = memref->getDefiningOp();
      // Return true if 'memref' is a block argument.
      if (!op)
        return true;
      // Return true if any use of 'memref' escapes the function.
      for (auto *user : memref->getUsers())
        if (!isMemRefDereferencingOp(*user))
          return true;
    }
    return false;
  }

  // Returns the unique AffineStoreOp in `node` that meets all the following:
  //   *) store is the only one that writes to a function-local memref live out
  //      of `node`,
  //   *) store is not the source of a self-dependence on `node`.
  // Otherwise, returns a null AffineStoreOp.
  AffineStoreOp getUniqueOutgoingStore(Node *node) {
    AffineStoreOp uniqueStore;

    // Return null if `node` doesn't have any outgoing edges.
    auto outEdgeIt = outEdges.find(node->id);
    if (outEdgeIt == outEdges.end())
      return nullptr;

    const auto &nodeOutEdges = outEdgeIt->second;
    for (auto *op : node->stores) {
      auto storeOp = cast<AffineStoreOp>(op);
      auto *memref = storeOp.getMemRef();
      // Skip this store if there are no dependences on its memref. This means
      // that store either:
      // *) writes to a memref that is only read within the same loop nest
      //    (self-dependence edges are not represented in graph at the moment),
      // *) writes to a function live out memref (function parameter), or
      // *) is dead.
      if (llvm::all_of(nodeOutEdges, [=](const Edge &edge) {
            return (edge.value != memref);
          }))
        continue;

      if (uniqueStore)
        // Found multiple stores to function-local live-out memrefs.
        return nullptr;
      // Found first store to function-local live-out memref.
      uniqueStore = storeOp;
    }

    return uniqueStore;
  }

  // Returns true if node 'id' can be removed from the graph. Returns false
  // otherwise. A node can be removed from the graph iff the following
  // conditions are met:
  // *) The node does not write to any memref which escapes (or is a
  //    function/block argument).
  // *) The node has no successors in the dependence graph.
  bool canRemoveNode(unsigned id) {
    if (writesToLiveInOrEscapingMemrefs(id))
      return false;
    Node *node = getNode(id);
    for (auto *storeOpInst : node->stores) {
      // Return false if there exist out edges from 'id' on 'memref'.
      if (getOutEdgeCount(id, cast<AffineStoreOp>(storeOpInst).getMemRef()) > 0)
        return false;
    }
    return true;
  }

  // Returns true iff there is an edge from node 'srcId' to node 'dstId' which
  // is for 'value' if non-null, or for any value otherwise. Returns false
  // otherwise.
  bool hasEdge(unsigned srcId, unsigned dstId, Value *value = nullptr) {
    if (outEdges.count(srcId) == 0 || inEdges.count(dstId) == 0) {
      return false;
    }

```
### Line 392-401
```
      return edge.id == srcId && (!value || edge.value == value);
    });
    return hasOutEdge && hasInEdge;
  }

  // Adds an edge from node 'srcId' to node 'dstId' for 'value'.
  void addEdge(unsigned srcId, unsigned dstId, Value *value) {
    if (!hasEdge(srcId, dstId, value)) {
      outEdges[srcId].push_back({dstId, value});
      inEdges[dstId].push_back({srcId, value});

```
### Line 402-480
```
      if (value->getType().isa<MemRefType>())
        memrefEdgeCount[value]++;
    }
  }

  // Removes an edge from node 'srcId' to node 'dstId' for 'value'.
  void removeEdge(unsigned srcId, unsigned dstId, Value *value) {
    assert(inEdges.count(dstId) > 0);
    assert(outEdges.count(srcId) > 0);
    if (value->getType().isa<MemRefType>()) {
      assert(memrefEdgeCount.count(value) > 0);
      memrefEdgeCount[value]--;
    }
    // Remove 'srcId' from 'inEdges[dstId]'.
    for (auto it = inEdges[dstId].begin(); it != inEdges[dstId].end(); ++it) {
      if ((*it).id == srcId && (*it).value == value) {
        inEdges[dstId].erase(it);
        break;
      }
    }
    // Remove 'dstId' from 'outEdges[srcId]'.
    for (auto it = outEdges[srcId].begin(); it != outEdges[srcId].end(); ++it) {
      if ((*it).id == dstId && (*it).value == value) {
        outEdges[srcId].erase(it);
        break;
      }
    }
  }

  // Returns true if there is a path in the dependence graph from node 'srcId'
  // to node 'dstId'. Returns false otherwise.
  bool hasDependencePath(unsigned srcId, unsigned dstId) {
    // Worklist state is: <node-id, next-output-edge-index-to-visit>
    SmallVector<std::pair<unsigned, unsigned>, 4> worklist;
    worklist.push_back({srcId, 0});
    // Run DFS traversal to see if 'dstId' is reachable from 'srcId'.
    while (!worklist.empty()) {
      auto &idAndIndex = worklist.back();
      // Return true if we have reached 'dstId'.
      if (idAndIndex.first == dstId)
        return true;
      // Pop and continue if node has no out edges, or if all out edges have
      // already been visited.
      if (outEdges.count(idAndIndex.first) == 0 ||
          idAndIndex.second == outEdges[idAndIndex.first].size()) {
        worklist.pop_back();
        continue;
      }
      // Get graph edge to traverse.
      Edge edge = outEdges[idAndIndex.first][idAndIndex.second];
      // Increment next output edge index for 'idAndIndex'.
      ++idAndIndex.second;
      // Add node at 'edge.id' to worklist.
      worklist.push_back({edge.id, 0});
    }
    return false;
  }

  // Returns the input edge count for node 'id' and 'memref' from src nodes
  // which access 'memref' with a store operation.
  unsigned getIncomingMemRefAccesses(unsigned id, Value *memref) {
    unsigned inEdgeCount = 0;
    if (inEdges.count(id) > 0)
      for (auto &inEdge : inEdges[id])
        if (inEdge.value == memref) {
          Node *srcNode = getNode(inEdge.id);
          // Only count in edges from 'srcNode' if 'srcNode' accesses 'memref'
          if (srcNode->getStoreOpCount(memref) > 0)
            ++inEdgeCount;
        }
    return inEdgeCount;
  }

  // Returns the output edge count for node 'id' and 'memref' (if non-null),
  // otherwise returns the total output edge count from node 'id'.
  unsigned getOutEdgeCount(unsigned id, Value *memref = nullptr) {
    unsigned outEdgeCount = 0;
    if (outEdges.count(id) > 0)
      for (auto &outEdge : outEdges[id])

```
### Line 481-521
```
        if (!memref || outEdge.value == memref)
          ++outEdgeCount;
    return outEdgeCount;
  }

  // Computes and returns an insertion point operation, before which the
  // the fused <srcId, dstId> loop nest can be inserted while preserving
  // dependences. Returns nullptr if no such insertion point is found.
  Operation *getFusedLoopNestInsertionPoint(unsigned srcId, unsigned dstId) {
    if (outEdges.count(srcId) == 0)
      return getNode(dstId)->op;

    // Build set of insts in range (srcId, dstId) which depend on 'srcId'.
    SmallPtrSet<Operation *, 2> srcDepInsts;
    for (auto &outEdge : outEdges[srcId])
      if (outEdge.id != dstId)
        srcDepInsts.insert(getNode(outEdge.id)->op);

    // Build set of insts in range (srcId, dstId) on which 'dstId' depends.
    SmallPtrSet<Operation *, 2> dstDepInsts;
    for (auto &inEdge : inEdges[dstId])
      if (inEdge.id != srcId)
        dstDepInsts.insert(getNode(inEdge.id)->op);

    Operation *srcNodeInst = getNode(srcId)->op;
    Operation *dstNodeInst = getNode(dstId)->op;

    // Computing insertion point:
    // *) Walk all operation positions in Block operation list in the
    //    range (src, dst). For each operation 'op' visited in this search:
    //   *) Store in 'firstSrcDepPos' the first position where 'op' has a
    //      dependence edge from 'srcNode'.
    //   *) Store in 'lastDstDepPost' the last position where 'op' has a
    //      dependence edge to 'dstNode'.
    // *) Compare 'firstSrcDepPos' and 'lastDstDepPost' to determine the
    //    operation insertion point (or return null pointer if no such
    //    insertion point exists: 'firstSrcDepPos' <= 'lastDstDepPos').
    SmallVector<Operation *, 2> depInsts;
    Optional<unsigned> firstSrcDepPos;
    Optional<unsigned> lastDstDepPos;
    unsigned pos = 0;

```
### Line 531-600
```
    }

    if (firstSrcDepPos.hasValue()) {
      if (lastDstDepPos.hasValue()) {
        if (firstSrcDepPos.getValue() <= lastDstDepPos.getValue()) {
          // No valid insertion point exists which preserves dependences.
          return nullptr;
        }
      }
      // Return the insertion point at 'firstSrcDepPos'.
      return depInsts[firstSrcDepPos.getValue()];
    }
    // No dependence targets in range (or only dst deps in range), return
    // 'dstNodInst' insertion point.
    return dstNodeInst;
  }

  // Updates edge mappings from node 'srcId' to node 'dstId' after 'oldMemRef'
  // has been replaced in node at 'dstId' by a private memref.
  void updateEdges(unsigned srcId, unsigned dstId, Value *oldMemRef) {
    // For each edge in 'inEdges[srcId]': add new edge remaping to 'dstId'.
    if (inEdges.count(srcId) > 0) {
      SmallVector<Edge, 2> oldInEdges = inEdges[srcId];
      for (auto &inEdge : oldInEdges) {
        // Add edge from 'inEdge.id' to 'dstId' if not for 'oldMemRef'.
        if (inEdge.value != oldMemRef)
          addEdge(inEdge.id, dstId, inEdge.value);
      }
    }
    // For each edge in 'outEdges[srcId]': remove edge from 'srcId' to 'dstId'.
    if (outEdges.count(srcId) > 0) {
      SmallVector<Edge, 2> oldOutEdges = outEdges[srcId];
      for (auto &outEdge : oldOutEdges) {
        // Remove any out edges from 'srcId' to 'dstId' across memrefs.
        if (outEdge.id == dstId)
          removeEdge(srcId, outEdge.id, outEdge.value);
      }
    }
    // Remove any edges in 'inEdges[dstId]' on 'oldMemRef' (which is being
    // replaced by a private memref). These edges could come from nodes
    // other than 'srcId' which were removed in the previous step.
    if (inEdges.count(dstId) > 0) {
      SmallVector<Edge, 2> oldInEdges = inEdges[dstId];
      for (auto &inEdge : oldInEdges)
        if (inEdge.value == oldMemRef)
          removeEdge(inEdge.id, dstId, inEdge.value);
    }
  }

  // Update edge mappings for nodes 'sibId' and 'dstId' to reflect fusion
  // of sibling node 'sidId' into node 'dstId'.
  void updateEdges(unsigned sibId, unsigned dstId) {
    // For each edge in 'inEdges[sibId]':
    // *) Add new edge from source node 'inEdge.id' to 'dstNode'.
    // *) Remove edge from source node 'inEdge.id' to 'sibNode'.
    if (inEdges.count(sibId) > 0) {
      SmallVector<Edge, 2> oldInEdges = inEdges[sibId];
      for (auto &inEdge : oldInEdges) {
        addEdge(inEdge.id, dstId, inEdge.value);
        removeEdge(inEdge.id, sibId, inEdge.value);
      }
    }

    // For each edge in 'outEdges[sibId]' to node 'id'
    // *) Add new edge from 'dstId' to 'outEdge.id'.
    // *) Remove edge from 'sibId' to 'outEdge.id'.
    if (outEdges.count(sibId) > 0) {
      SmallVector<Edge, 2> oldOutEdges = outEdges[sibId];
      for (auto &outEdge : oldOutEdges) {
        addEdge(dstId, outEdge.id, outEdge.value);

```
### Line 601-610
```
        removeEdge(sibId, outEdge.id, outEdge.value);
      }
    }
  }

  // Adds ops in 'loads' and 'stores' to node at 'id'.
  void addToNode(unsigned id, const SmallVectorImpl<Operation *> &loads,
                 const SmallVectorImpl<Operation *> &stores) {
    Node *node = getNode(id);
    for (auto *loadOpInst : loads)

```
### Line 617-654
```
    Node *node = getNode(id);
    node->loads.clear();
    node->stores.clear();
  }

  // Calls 'callback' for each input edge incident to node 'id' which carries a
  // memref dependence.
  void forEachMemRefInputEdge(unsigned id,
                              const std::function<void(Edge)> &callback) {
    if (inEdges.count(id) > 0)
      forEachMemRefEdge(inEdges[id], callback);
  }

  // Calls 'callback' for each output edge from node 'id' which carries a
  // memref dependence.
  void forEachMemRefOutputEdge(unsigned id,
                               const std::function<void(Edge)> &callback) {
    if (outEdges.count(id) > 0)
      forEachMemRefEdge(outEdges[id], callback);
  }

  // Calls 'callback' for each edge in 'edges' which carries a memref
  // dependence.
  void forEachMemRefEdge(ArrayRef<Edge> edges,
                         const std::function<void(Edge)> &callback) {
    for (auto &edge : edges) {
      // Skip if 'edge' is not a memref dependence edge.
      if (!edge.value->getType().isa<MemRefType>())
        continue;
      assert(nodes.count(edge.id) > 0);
      // Skip if 'edge.id' is not a loop nest.
      if (!isa<AffineForOp>(getNode(edge.id)->op))
        continue;
      // Visit current input edge 'edge'.
      callback(edge);
    }
  }


```
### Line 670-698
```
    }
  }
  void dump() const { print(llvm::errs()); }
};

// Initializes the data dependence graph by walking operations in 'f'.
// Assigns each node in the graph a node id based on program order in 'f'.
// TODO(andydavis) Add support for taking a Block arg to construct the
// dependence graph at a different depth.
bool MemRefDependenceGraph::init(FuncOp f) {
  DenseMap<Value *, SetVector<unsigned>> memrefAccesses;

  // TODO: support multi-block functions.
  if (f.getBlocks().size() != 1)
    return false;

  DenseMap<Operation *, unsigned> forToNodeMap;
  for (auto &op : f.front()) {
    if (auto forOp = dyn_cast<AffineForOp>(op)) {
      // Create graph node 'id' to represent top-level 'forOp' and record
      // all loads and store accesses it contains.
      LoopNestStateCollector collector;
      collector.collect(&op);
      // Return false if a non 'affine.for' region was found (not currently
      // supported).
      if (collector.hasNonForRegion)
        return false;
      Node node(nextNodeId++, &op);
      for (auto *opInst : collector.loadOpInsts) {

```
### Line 706-740
```
        memrefAccesses[memref].insert(node.id);
      }
      forToNodeMap[&op] = node.id;
      nodes.insert({node.id, node});
    } else if (auto loadOp = dyn_cast<AffineLoadOp>(op)) {
      // Create graph node for top-level load op.
      Node node(nextNodeId++, &op);
      node.loads.push_back(&op);
      auto *memref = cast<AffineLoadOp>(op).getMemRef();
      memrefAccesses[memref].insert(node.id);
      nodes.insert({node.id, node});
    } else if (auto storeOp = dyn_cast<AffineStoreOp>(op)) {
      // Create graph node for top-level store op.
      Node node(nextNodeId++, &op);
      node.stores.push_back(&op);
      auto *memref = cast<AffineStoreOp>(op).getMemRef();
      memrefAccesses[memref].insert(node.id);
      nodes.insert({node.id, node});
    } else if (op.getNumRegions() != 0) {
      // Return false if another region is found (not currently supported).
      return false;
    } else if (op.getNumResults() > 0 && !op.use_empty()) {
      // Create graph node for top-level producer of SSA values, which
      // could be used by loop nest nodes.
      Node node(nextNodeId++, &op);
      nodes.insert({node.id, node});
    }
  }

  // Add dependence edges between nodes which produce SSA values and their
  // users.
  for (auto &idAndNode : nodes) {
    const Node &node = idAndNode.second;
    if (!node.loads.empty() || !node.stores.empty())
      continue;

```
### Line 750-759
```
        addEdge(node.id, userLoopNestId, value);
      }
    }
  }

  // Walk memref access lists and add graph edges between dependent nodes.
  for (auto &memrefAndList : memrefAccesses) {
    unsigned n = memrefAndList.second.size();
    for (unsigned i = 0; i < n; ++i) {
      unsigned srcId = memrefAndList.second[i];

```
### Line 769-779
```
    }
  }
  return true;
}

// Removes load operations from 'srcLoads' which operate on 'memref', and
// adds them to 'dstLoads'.
static void moveLoadsAccessingMemrefTo(Value *memref,
                                       SmallVectorImpl<Operation *> *srcLoads,
                                       SmallVectorImpl<Operation *> *dstLoads) {
  dstLoads->clear();

```
### Line 785-794
```
      srcLoadsToKeep.push_back(load);
  }
  srcLoads->swap(srcLoadsToKeep);
}

// Returns the innermost common loop depth for the set of operations in 'ops'.
static unsigned getInnermostCommonLoopDepth(ArrayRef<Operation *> ops) {
  unsigned numOps = ops.size();
  assert(numOps > 0);


```
### Line 812-837
```
    ++loopDepth;
  }
  return loopDepth;
}

// Returns the maximum loop depth at which no dependences between 'loadOpInsts'
// and 'storeOpInsts' are satisfied.
static unsigned getMaxLoopDepth(ArrayRef<Operation *> loadOpInsts,
                                ArrayRef<Operation *> storeOpInsts) {
  // Merge loads and stores into the same array.
  SmallVector<Operation *, 2> ops(loadOpInsts.begin(), loadOpInsts.end());
  ops.append(storeOpInsts.begin(), storeOpInsts.end());

  // Compute the innermost common loop depth for loads and stores.
  unsigned loopDepth = getInnermostCommonLoopDepth(ops);

  // Return common loop depth for loads if there are no store ops.
  if (storeOpInsts.empty())
    return loopDepth;

  // Check dependences on all pairs of ops in 'ops' and store the minimum
  // loop depth at which a dependence is satisfied.
  for (unsigned i = 0, e = ops.size(); i < e; ++i) {
    auto *srcOpInst = ops[i];
    MemRefAccess srcAccess(srcOpInst);
    for (unsigned j = 0; j < e; ++j) {

```
### Line 840-855
```

      unsigned numCommonLoops =
          getNumCommonSurroundingLoops(*srcOpInst, *dstOpInst);
      for (unsigned d = 1; d <= numCommonLoops + 1; ++d) {
        FlatAffineConstraints dependenceConstraints;
        // TODO(andydavis) Cache dependence analysis results, check cache here.
        DependenceResult result = checkMemrefAccessDependence(
            srcAccess, dstAccess, d, &dependenceConstraints,
            /*dependenceComponents=*/nullptr);
        if (hasDependence(result)) {
          // Store minimum loop depth and break because we want the min 'd' at
          // which there is a dependence.
          loopDepth = std::min(loopDepth, d - 1);
          break;
        }
      }

```
### Line 856-876
```
    }
  }
  return loopDepth;
}

// Sinks all sequential loops to the innermost levels (while preserving
// relative order among them) and moves all parallel loops to the
// outermost (while again preserving relative order among them).
// This can increase the loop depth at which we can fuse a slice, since we are
// pushing loop carried dependence to a greater depth in the loop nest.
static void sinkSequentialLoops(MemRefDependenceGraph::Node *node) {
  assert(isa<AffineForOp>(node->op));
  AffineForOp newRootForOp = sinkSequentialLoops(cast<AffineForOp>(node->op));
  node->op = newRootForOp.getOperation();
}

//  TODO(mlir-team): improve/complete this when we have target data.
unsigned getMemRefEltSizeInBytes(MemRefType memRefType) {
  auto elementType = memRefType.getElementType();

  unsigned sizeInBits;

```
### Line 882-934
```
        vectorType.getElementTypeBitWidth() * vectorType.getNumElements();
  }
  return llvm::divideCeil(sizeInBits, 8);
}

// Creates and returns a private (single-user) memref for fused loop rooted
// at 'forOp', with (potentially reduced) memref size based on the
// MemRefRegion written to by 'srcStoreOpInst' at depth 'dstLoopDepth'.
// TODO(bondhugula): consider refactoring the common code from generateDma and
// this one.
static Value *createPrivateMemRef(AffineForOp forOp, Operation *srcStoreOpInst,
                                  unsigned dstLoopDepth,
                                  Optional<unsigned> fastMemorySpace,
                                  uint64_t localBufSizeThreshold) {
  auto *forInst = forOp.getOperation();

  // Create builder to insert alloc op just before 'forOp'.
  OpBuilder b(forInst);
  // Builder to create constants at the top level.
  OpBuilder top(forInst->getParentOfType<FuncOp>().getBody());
  // Create new memref type based on slice bounds.
  auto *oldMemRef = cast<AffineStoreOp>(srcStoreOpInst).getMemRef();
  auto oldMemRefType = oldMemRef->getType().cast<MemRefType>();
  unsigned rank = oldMemRefType.getRank();

  // Compute MemRefRegion for 'srcStoreOpInst' at depth 'dstLoopDepth'.
  MemRefRegion region(srcStoreOpInst->getLoc());
  bool validRegion = succeeded(region.compute(srcStoreOpInst, dstLoopDepth));
  (void)validRegion;
  assert(validRegion && "unexpected memref region failure");
  SmallVector<int64_t, 4> newShape;
  std::vector<SmallVector<int64_t, 4>> lbs;
  SmallVector<int64_t, 8> lbDivisors;
  lbs.reserve(rank);
  // Query 'region' for 'newShape' and lower bounds of MemRefRegion accessed
  // by 'srcStoreOpInst' at depth 'dstLoopDepth'.
  Optional<int64_t> numElements =
      region.getConstantBoundingSizeAndShape(&newShape, &lbs, &lbDivisors);
  assert(numElements.hasValue() &&
         "non-constant number of elts in local buffer");

  const FlatAffineConstraints *cst = region.getConstraints();
  // 'outerIVs' holds the values that this memory region is symbolic/parametric
  // on; this would correspond to loop IVs surrounding the level at which the
  // slice is being materialized.
  SmallVector<Value *, 8> outerIVs;
  cst->getIdValues(rank, cst->getNumIds(), &outerIVs);

  // Build 'rank' AffineExprs from MemRefRegion 'lbs'
  SmallVector<AffineExpr, 4> offsets;
  offsets.reserve(rank);
  for (unsigned d = 0; d < rank; ++d) {
    assert(lbs[d].size() == cst->getNumCols() - rank && "incorrect bound size");

```
### Line 941-951
```
    offset =
        (offset + lbs[d][cst->getNumCols() - 1 - rank]).floorDiv(lbDivisors[d]);
    offsets.push_back(offset);
  }

  // Create 'newMemRefType' using 'newShape' from MemRefRegion accessed
  // by 'srcStoreOpInst'.
  uint64_t bufSize =
      getMemRefEltSizeInBytes(oldMemRefType) * numElements.getValue();
  unsigned newMemSpace;
  if (bufSize <= localBufSizeThreshold && fastMemorySpace.hasValue()) {

```
### Line 953-979
```
  } else {
    newMemSpace = oldMemRefType.getMemorySpace();
  }
  auto newMemRefType = MemRefType::get(newShape, oldMemRefType.getElementType(),
                                       {}, newMemSpace);
  // Gather alloc operands for the dynamic dimensions of the memref.
  SmallVector<Value *, 4> allocOperands;
  unsigned dynamicDimCount = 0;
  for (auto dimSize : oldMemRefType.getShape()) {
    if (dimSize == -1)
      allocOperands.push_back(
          top.create<DimOp>(forOp.getLoc(), oldMemRef, dynamicDimCount++));
  }

  // Create new private memref for fused loop 'forOp'.
  // TODO(andydavis) Create/move alloc ops for private memrefs closer to their
  // consumer loop nests to reduce their live range. Currently they are added
  // at the beginning of the function, because loop nests can be reordered
  // during the fusion pass.
  Value *newMemRef =
      top.create<AllocOp>(forOp.getLoc(), newMemRefType, allocOperands);

  // Build an AffineMap to remap access functions based on lower bound offsets.
  SmallVector<AffineExpr, 4> remapExprs;
  remapExprs.reserve(rank);
  unsigned zeroOffsetCount = 0;
  for (unsigned i = 0; i < rank; i++) {

```
### Line 987-996
```
    remapExprs.push_back(remapExpr);
  }
  auto indexRemap = zeroOffsetCount == rank
                        ? AffineMap()
                        : AffineMap::get(outerIVs.size() + rank, 0, remapExprs);
  // Replace all users of 'oldMemRef' with 'newMemRef'.
  LogicalResult res =
      replaceAllMemRefUsesWith(oldMemRef, newMemRef, {}, indexRemap,
                               /*extraOperands=*/outerIVs,
                               /*symbolOperands=*/{},

```
### Line 999-1039
```
         "replaceAllMemrefUsesWith should always succeed here");
  (void)res;
  return newMemRef;
}

// Checks if node 'srcId' can be safely fused into node 'dstId'. Node 'srcId'
// may write to multiple memrefs but it is required that only one of them,
// 'srcLiveOutStoreOp', have an output edge.
// Returns true if 'dstNode's read/write region to 'memref' is a super set of
// 'srcNode's write region to 'memref'.
// TODO(andydavis) Generalize this to handle more live in/out cases.
static bool canFuseSrcWhichWritesToLiveOut(unsigned srcId, unsigned dstId,
                                           AffineStoreOp srcLiveOutStoreOp,
                                           MemRefDependenceGraph *mdg) {
  assert(srcLiveOutStoreOp && "Expected a valid store op");
  assert(mdg->getOutEdgeCount(srcId) == 1 && "Expected only one output edge");
  auto *dstNode = mdg->getNode(dstId);
  Value *memref = srcLiveOutStoreOp.getMemRef();

  // Compute MemRefRegion 'srcWriteRegion' for 'srcStoreOp' on 'memref'.
  MemRefRegion srcWriteRegion(srcLiveOutStoreOp.getLoc());
  if (failed(srcWriteRegion.compute(srcLiveOutStoreOp, /*loopDepth=*/0))) {
    LLVM_DEBUG(llvm::dbgs()
               << "Unable to compute MemRefRegion for source operation\n.");
    return false;
  }
  SmallVector<int64_t, 4> srcShape;
  // Query 'srcWriteRegion' for 'srcShape' and 'srcNumElements'.
  // by 'srcStoreOp' at depth 'dstLoopDepth'.
  Optional<int64_t> srcNumElements =
      srcWriteRegion.getConstantBoundingSizeAndShape(&srcShape);
  if (!srcNumElements.hasValue())
    return false;

  // Compute MemRefRegion 'dstRegion' for 'dstStore/LoadOpInst' on 'memref'.
  // TODO(andydavis) Compute 'unionboundingbox' of all write regions (one for
  // each store op in 'dstStoreOps').
  SmallVector<Operation *, 2> dstStoreOps;
  dstNode->getStoreOpsForMemref(memref, &dstStoreOps);
  SmallVector<Operation *, 2> dstLoadOps;
  dstNode->getLoadOpsForMemref(memref, &dstLoadOps);

```
### Line 1044-1105
```
    LLVM_DEBUG(llvm::dbgs()
               << "Unable to compute MemRefRegion for dest operation\n.");
    return false;
  }
  SmallVector<int64_t, 4> dstShape;
  // Query 'dstRegion' for 'dstShape' and 'dstNumElements'.
  // by 'dstOpInst' at depth 'dstLoopDepth'.
  Optional<int64_t> dstNumElements =
      dstRegion.getConstantBoundingSizeAndShape(&dstShape);
  if (!dstNumElements.hasValue())
    return false;

  // Return false if write region is not a superset of 'srcNodes' write
  // region to 'memref'.
  // TODO(andydavis) Check the shape and lower bounds here too.
  if (srcNumElements != dstNumElements)
    return false;
  return true;
}

// Checks the profitability of fusing a backwards slice of the loop nest
// surrounding 'srcOpInst' into the loop nest surrounding 'dstLoadOpInsts'.
// The argument 'srcStoreOpInst' is used to calculate the storage reduction on
// the memref being produced and consumed, which is an input to the cost model.
// For producer-consumer fusion, 'srcStoreOpInst' will be the same as
// 'srcOpInst', as we are slicing w.r.t to that producer.
// For input-reuse fusion, 'srcOpInst' will be the src loop nest LoadOp which
// reads from the same memref as dst loop nest load ops, and 'srcStoreOpInst'
// will be the unique store op in the src node, which will be used to check
// that the write region is the same after input-reuse fusion.
// Returns true if it is profitable to fuse the candidate loop nests. Returns
// false otherwise. `dstLoopDepth` is set to the most profitable depth at which
// to materialize the source loop nest slice.
// The profitability model executes the following steps:
// *) Computes the backward computation slice at 'srcOpInst'. This
//    computation slice of the loop nest surrounding 'srcOpInst' is
//    represented by modified src loop bounds in 'sliceState', which are
//    functions of loop IVs in the loop nest surrounding 'srcOpInst'.
// *) Computes the cost of unfused src/dst loop nests (currently the cost of a
//    loop nest is the total number of dynamic operation instances in the loop
//    nest).
// *) Computes the cost of fusing a slice of the src loop nest into the dst
//    loop nest at various values of dst loop depth, attempting to fuse
//    the largest computation slice at the maximal dst loop depth (closest to
//    the load) to minimize reuse distance and potentially enable subsequent
//    load/store forwarding.
//    NOTE: If the dst loop nest includes multiple loads in 'dstLoadOpInsts' for
//    the same memref as is written by 'srcOpInst', then the union of slice
//    loop bounds is used to compute the slice and associated slice cost.
//    NOTE: 'dstLoopDepth' refers to the loop depth within the destination loop
//    nest, at which the src computation slice is inserted/fused.
//    NOTE: We attempt to maximize the dst loop depth, but there are cases
//    where a particular setting for 'dstLoopNest' might fuse an unsliced
//    loop (within the src computation slice) at a depth which results in
//    excessive recomputation (see unit tests for examples).
// *) Compares the total cost of the unfused loop nests to the min cost fused
//    loop nest computed in the previous step, and returns true if the latter
//    is lower.
static bool isFusionProfitable(Operation *srcOpInst, Operation *srcStoreOpInst,
                               ArrayRef<Operation *> dstLoadOpInsts,
                               ArrayRef<Operation *> dstStoreOpInsts,
                               ComputationSliceState *sliceState,

```
### Line 1110-1138
```
    for (auto dstOpInst : dstLoadOpInsts) {
      llvm::dbgs() << " " << *dstOpInst << "\n";
    };
  });

  // Compute cost of sliced and unsliced src loop nest.
  SmallVector<AffineForOp, 4> srcLoopIVs;
  getLoopIVs(*srcOpInst, &srcLoopIVs);
  unsigned numSrcLoopIVs = srcLoopIVs.size();

  // Walk src loop nest and collect stats.
  LoopNestStats srcLoopNestStats;
  if (!getLoopNestStats(srcLoopIVs[0], &srcLoopNestStats))
    return false;

  // Compute cost of dst loop nest.
  SmallVector<AffineForOp, 4> dstLoopIVs;
  getLoopIVs(*dstLoadOpInsts[0], &dstLoopIVs);

  LoopNestStats dstLoopNestStats;
  if (!getLoopNestStats(dstLoopIVs[0], &dstLoopNestStats))
    return false;

  // Compute the maximum loop depth at which we can can insert the src slice
  // and still satisfy dest loop nest dependences, for producer-consumer fusion.
  unsigned maxDstLoopDepth =
      (srcOpInst == srcStoreOpInst)
          ? getMaxLoopDepth(dstLoadOpInsts, dstStoreOpInsts)
          : dstLoopIVs.size();

```
### Line 1139-1166
```
  if (maxDstLoopDepth == 0) {
    LLVM_DEBUG(llvm::dbgs() << "Can't fuse: maxDstLoopDepth == 0 .\n");
    return false;
  }

  // Search for min cost value for 'dstLoopDepth'. At each value of
  // 'dstLoopDepth' from 'maxDstLoopDepth' to '1', compute computation slice
  // bounds between 'srcOpInst' and each op in 'dstOpinsts' (taking the union
  // of these bounds). Next the union slice bounds are used to calculate
  // the cost of the slice and the cost of the slice inserted into the dst
  // loop nest at 'dstLoopDepth'.
  uint64_t minFusedLoopNestComputeCost = std::numeric_limits<uint64_t>::max();
  double maxStorageReduction = 0.0;
  Optional<uint64_t> sliceMemEstimate = None;

  SmallVector<ComputationSliceState, 4> sliceStates;
  sliceStates.resize(maxDstLoopDepth);
  // The best loop depth at which to materialize the slice.
  Optional<unsigned> bestDstLoopDepth = None;

  // Compute op instance count for the src loop nest without iteration slicing.
  uint64_t srcLoopNestCost = getComputeCost(srcLoopIVs[0], srcLoopNestStats);

  // Compute src loop nest write region size.
  MemRefRegion srcWriteRegion(srcStoreOpInst->getLoc());
  if (failed(srcWriteRegion.compute(srcStoreOpInst, /*loopDepth=*/0))) {
    LLVM_DEBUG(llvm::dbgs()
               << "Unable to compute MemRefRegion for source operation\n.");

```
### Line 1171-1186
```
      srcWriteRegion.getRegionSize();
  if (!maybeSrcWriteRegionSizeBytes.hasValue())
    return false;
  int64_t srcWriteRegionSizeBytes = maybeSrcWriteRegionSizeBytes.getValue();

  // Compute op instance count for the src loop nest.
  uint64_t dstLoopNestCost = getComputeCost(dstLoopIVs[0], dstLoopNestStats);

  // Evaluate all depth choices for materializing the slice in the destination
  // loop nest.
  for (unsigned i = maxDstLoopDepth; i >= 1; --i) {
    // Compute the union of slice bounds of all ops in 'dstLoadOpInsts'.
    if (failed(mlir::computeSliceUnion({srcOpInst}, dstLoadOpInsts,
                                       /*loopDepth=*/i,
                                       /*numCommonLoops=*/0,
                                       /*isBackwardSlice=*/true,

```
### Line 1201-1212
```
    double additionalComputeFraction =
        fusedLoopNestComputeCost /
            (static_cast<double>(srcLoopNestCost) + dstLoopNestCost) -
        1;

    // Determine what the slice write MemRefRegion would be, if the src loop
    // nest slice 'sliceStates[i - 1]' were to be inserted into the dst loop
    // nest at loop depth 'i'
    MemRefRegion sliceWriteRegion(srcStoreOpInst->getLoc());
    if (failed(sliceWriteRegion.compute(srcStoreOpInst, /*loopDepth=*/0,
                                        &sliceStates[i - 1]))) {
      LLVM_DEBUG(llvm::dbgs()

```
### Line 1225-1237
```
      continue;
    }
    int64_t sliceWriteRegionSizeBytes =
        maybeSliceWriteRegionSizeBytes.getValue();

    // If we are fusing for reuse, check that write regions remain the same.
    // TODO(andydavis) Write region check should check sizes and offsets in
    // each dimension, so that we are sure they are covering the same memref
    // region. Also, move this out to a isMemRefRegionSuperSet helper function.
    if (srcOpInst != srcStoreOpInst &&
        sliceWriteRegionSizeBytes != srcWriteRegionSizeBytes)
      continue;


```
### Line 1255-1267
```
    double computeToleranceThreshold =
        clFusionAddlComputeTolerance.getNumOccurrences() > 0
            ? clFusionAddlComputeTolerance
            : LoopFusion::kComputeToleranceThreshold;

    // TODO(b/123247369): This is a placeholder cost model.
    // Among all choices that add an acceptable amount of redundant computation
    // (as per computeToleranceThreshold), we will simply pick the one that
    // reduces the intermediary size the most.
    if ((storageReduction > maxStorageReduction) &&
        (maximalFusion ||
         (additionalComputeFraction < computeToleranceThreshold))) {
      maxStorageReduction = storageReduction;

```
### Line 1269-1279
```
      minFusedLoopNestComputeCost = fusedLoopNestComputeCost;
      sliceMemEstimate = sliceWriteRegionSizeBytes;
    }
  }

  // A simple cost model: fuse if it reduces the memory footprint. If
  // -maximal-fusion is set, fuse nevertheless.

  if (!maximalFusion && !bestDstLoopDepth.hasValue()) {
    LLVM_DEBUG(
        llvm::dbgs()

```
### Line 1285-1294
```
  if (!bestDstLoopDepth.hasValue()) {
    LLVM_DEBUG(llvm::dbgs() << "no fusion depth could be evaluated.\n");
    return false;
  }

  // Set dstLoopDepth based on best values from search.
  *dstLoopDepth = bestDstLoopDepth.getValue();

  LLVM_DEBUG(
      llvm::dbgs() << " LoopFusion fusion stats:"

```
### Line 1346-1362
```
                : "<unknown>");
    msg << "% storage reduction.\n";
    llvm::dbgs() << msg.str();
  });

  // Update return parameter 'sliceState' with 'bestSliceState'.
  ComputationSliceState *bestSliceState = &sliceStates[*dstLoopDepth - 1];
  sliceState->lbs = bestSliceState->lbs;
  sliceState->ubs = bestSliceState->ubs;
  sliceState->lbOperands = bestSliceState->lbOperands;
  sliceState->ubOperands = bestSliceState->ubOperands;

  // Canonicalize slice bound affine maps.
  for (unsigned i = 0; i < numSrcLoopIVs; ++i) {
    if (sliceState->lbs[i] != AffineMap()) {
      canonicalizeMapAndOperands(&sliceState->lbs[i],
                                 &sliceState->lbOperands[i]);

```
### Line 1367-1434
```
    }
  }
  return true;
}

// GreedyFusion greedily fuses loop nests which have a producer/consumer or
// input-reuse relationship on a memref, with the goal of improving locality.
//
// The steps of the producer-consumer fusion algorithm are as follows:
//
// *) A worklist is initialized with node ids from the dependence graph.
// *) For each node id in the worklist:
//   *) Pop an AffineForOp of the worklist. This 'dstAffineForOp' will be a
//      candidate destination AffineForOp into which fusion will be attempted.
//   *) Add each LoadOp currently in 'dstAffineForOp' into list 'dstLoadOps'.
//   *) For each LoadOp in 'dstLoadOps' do:
//      *) Look up dependent loop nests which have a single store op to the same
//         memref.
//      *) Check if dependences would be violated by the fusion.
//      *) Get a computation slice of 'srcLoopNest', which adjusts its loop
//         bounds to be functions of 'dstLoopNest' IVs and symbols.
//      *) Fuse the 'srcLoopNest' computation slice into the 'dstLoopNest',
//         at a loop depth determined by the cost model in 'isFusionProfitable'.
//      *) Add the newly fused load/store operations to the state,
//         and also add newly fused load ops to 'dstLoopOps' to be considered
//         as fusion dst load ops in another iteration.
//      *) Remove old src loop nest and its associated state.
//
// The steps of the input-reuse fusion algorithm are as follows:
//
// *) Initialize 'worklist' with node ids from the dependence graph.
// *) For each 'dstNode' in the worklist:
//   *) Find a candidate sibling node 'sibNode' to fuse with 'dstNode' which
//      loads from the same memref, but which has no dependence paths to/from.
//   *) Get a computation slice of 'sibLoopNest', which adjusts its loop
//      bounds to be functions of 'dstLoopNest' IVs and symbols.
//   *) Fuse the 'sibLoopNest' computation slice into the 'dstLoopNest',
//      at a loop depth determined by the cost model in 'isFusionProfitable'.
//      This function also checks that the memref write region of 'sibLoopNest',
//      is preserved in the fused loop nest.
//   *) Update graph state to reflect the fusion of 'sibNode' into 'dstNode'.
//
// Given a graph where top-level operations are vertices in the set 'V' and
// edges in the set 'E' are dependences between vertices, this algorithm
// takes O(V) time for initialization, and has runtime O(V + E).
//
// This greedy algorithm is not 'maximal' due to the current restriction of
// fusing along single producer consumer edges, but there is a TODO to fix this.
//
// TODO(andydavis) Experiment with other fusion policies.
struct GreedyFusion {
public:
  // The data dependence graph to traverse during fusion.
  MemRefDependenceGraph *mdg;
  // Worklist of graph nodes visited during the fusion pass.
  SmallVector<unsigned, 8> worklist;
  // Set of graph nodes which are present on the worklist.
  llvm::SmallDenseSet<unsigned, 16> worklistSet;
  // Parameter for local buffer size threshold.
  unsigned localBufSizeThreshold;
  // Parameter for fast memory space.
  Optional<unsigned> fastMemorySpace;
  // If true, ignore any additional (redundant) computation tolerance threshold
  // that would have prevented fusion.
  bool maximalFusion;

  using Node = MemRefDependenceGraph::Node;


```
### Line 1435-1447
```
  GreedyFusion(MemRefDependenceGraph *mdg, unsigned localBufSizeThreshold,
               Optional<unsigned> fastMemorySpace, bool maximalFusion)
      : mdg(mdg), localBufSizeThreshold(localBufSizeThreshold),
        fastMemorySpace(fastMemorySpace), maximalFusion(maximalFusion) {}

  // Initializes 'worklist' with nodes from 'mdg'
  void init() {
    // TODO(andydavis) Add a priority queue for prioritizing nodes by different
    // metrics (e.g. arithmetic intensity/flops-to-bytes ratio).
    worklist.clear();
    worklistSet.clear();
    for (auto &idAndNode : mdg->nodes) {
      const Node &node = idAndNode.second;

```
### Line 1448-1463
```
      worklist.push_back(node.id);
      worklistSet.insert(node.id);
    }
  }

  // Run the GreedyFusion pass.
  // *) First pass through the nodes fuses single-use producer nodes into their
  //    unique consumer.
  // *) Second pass fuses sibling nodes which share no dependence edges.
  // *) Third pass fuses any remaining producer nodes into their users.
  void run() {
    // TODO(andydavis) Run this repeatedly until a fixed-point is reached.
    fuseProducerConsumerNodes(/*maxSrcUserCount=*/1);
    fuseSiblingNodes();
    fuseProducerConsumerNodes(
        /*maxSrcUserCount=*/std::numeric_limits<unsigned>::max());

```
### Line 1469-1601
```
    while (!worklist.empty()) {
      unsigned dstId = worklist.back();
      worklist.pop_back();
      worklistSet.erase(dstId);

      // Skip if this node was removed (fused into another node).
      if (mdg->nodes.count(dstId) == 0)
        continue;
      // Get 'dstNode' into which to attempt fusion.
      auto *dstNode = mdg->getNode(dstId);
      // Skip if 'dstNode' is not a loop nest.
      if (!isa<AffineForOp>(dstNode->op))
        continue;
      // Sink sequential loops in 'dstNode' (and thus raise parallel loops)
      // while preserving relative order. This can increase the maximum loop
      // depth at which we can fuse a slice of a producer loop nest into a
      // consumer loop nest.
      sinkSequentialLoops(dstNode);

      SmallVector<Operation *, 4> loads = dstNode->loads;
      SmallVector<Operation *, 4> dstLoadOpInsts;
      DenseSet<Value *> visitedMemrefs;
      while (!loads.empty()) {
        // Get memref of load on top of the stack.
        auto *memref = cast<AffineLoadOp>(loads.back()).getMemRef();
        if (visitedMemrefs.count(memref) > 0)
          continue;
        visitedMemrefs.insert(memref);
        // Move all loads in 'loads' accessing 'memref' to 'dstLoadOpInsts'.
        moveLoadsAccessingMemrefTo(memref, &loads, &dstLoadOpInsts);
        // Skip if no input edges along which to fuse.
        if (mdg->inEdges.count(dstId) == 0)
          continue;
        // Iterate through in-edges for 'dstId' and src node id for any
        // edges on 'memref'.
        SmallVector<unsigned, 2> srcNodeIds;
        for (auto &srcEdge : mdg->inEdges[dstId]) {
          // Skip 'srcEdge' if not for 'memref'.
          if (srcEdge.value != memref)
            continue;
          srcNodeIds.push_back(srcEdge.id);
        }
        for (unsigned srcId : srcNodeIds) {
          // Skip if this node was removed (fused into another node).
          if (mdg->nodes.count(srcId) == 0)
            continue;
          // Get 'srcNode' from which to attempt fusion into 'dstNode'.
          auto *srcNode = mdg->getNode(srcId);
          // Skip if 'srcNode' is not a loop nest.
          if (!isa<AffineForOp>(srcNode->op))
            continue;
          // Skip if 'srcNode' has more than one live-out store to a
          // function-local memref.
          // TODO(andydavis) Support more generic multi-output src loop nests
          // fusion.
          auto srcStoreOp = mdg->getUniqueOutgoingStore(srcNode);
          if (!srcStoreOp)
            continue;
          // Unique outgoing store found must write to 'memref' since 'memref'
          // is the one that established the producer-consumer relationship
          // between 'srcNode' and 'dstNode'.
          assert(srcStoreOp.getMemRef() == memref &&
                 "Found store to unexpected memref");

          // Skip if 'srcNode' writes to any live in or escaping memrefs,
          // and cannot be fused.
          bool writesToLiveInOrOut =
              mdg->writesToLiveInOrEscapingMemrefs(srcNode->id);
          if (writesToLiveInOrOut &&
              !canFuseSrcWhichWritesToLiveOut(srcId, dstId, srcStoreOp, mdg))
            continue;

          // Skip if 'srcNode' out edge count on 'memref' > 'maxSrcUserCount'.
          if (mdg->getOutEdgeCount(srcNode->id, memref) > maxSrcUserCount)
            continue;

          // Compute an operation list insertion point for the fused loop
          // nest which preserves dependences.
          Operation *insertPointInst =
              mdg->getFusedLoopNestInsertionPoint(srcNode->id, dstNode->id);
          if (insertPointInst == nullptr)
            continue;

          // Gather 'dstNode' store ops to 'memref'.
          SmallVector<Operation *, 2> dstStoreOpInsts;
          for (auto *storeOpInst : dstNode->stores)
            if (cast<AffineStoreOp>(storeOpInst).getMemRef() == memref)
              dstStoreOpInsts.push_back(storeOpInst);

          unsigned bestDstLoopDepth;
          mlir::ComputationSliceState sliceState;
          // Check if fusion would be profitable.
          if (!isFusionProfitable(srcStoreOp, srcStoreOp, dstLoadOpInsts,
                                  dstStoreOpInsts, &sliceState,
                                  &bestDstLoopDepth, maximalFusion))
            continue;
          // TODO(andydavis) Remove the following test code when canFuseLoops
          // is fully functional.
          mlir::ComputationSliceState sliceUnion;
          if (!maximalFusion) {
            FusionResult result = mlir::canFuseLoops(
                cast<AffineForOp>(srcNode->op), cast<AffineForOp>(dstNode->op),
                bestDstLoopDepth, &sliceUnion);
            assert(result.value == FusionResult::Success);
            (void)result;
          }
          // Fuse computation slice of 'srcLoopNest' into 'dstLoopNest'.
          auto sliceLoopNest = mlir::insertBackwardComputationSlice(
              srcStoreOp, dstLoadOpInsts[0], bestDstLoopDepth, &sliceState);
          if (sliceLoopNest) {
            LLVM_DEBUG(llvm::dbgs() << "\tslice loop nest:\n"
                                    << *sliceLoopNest.getOperation() << "\n");
            // Move 'dstAffineForOp' before 'insertPointInst' if needed.
            auto dstAffineForOp = cast<AffineForOp>(dstNode->op);
            if (insertPointInst != dstAffineForOp.getOperation()) {
              dstAffineForOp.getOperation()->moveBefore(insertPointInst);
            }
            // Update edges between 'srcNode' and 'dstNode'.
            mdg->updateEdges(srcNode->id, dstNode->id, memref);

            // Collect slice loop stats.
            LoopNestStateCollector sliceCollector;
            sliceCollector.collect(sliceLoopNest.getOperation());
            // Promote single iteration slice loops to single IV value.
            for (auto forOp : sliceCollector.forOps) {
              promoteIfSingleIteration(forOp);
            }
            if (!writesToLiveInOrOut) {
              // Create private memref for 'memref' in 'dstAffineForOp'.
              SmallVector<Operation *, 4> storesForMemref;
              for (auto *storeOpInst : sliceCollector.storeOpInsts) {
                if (cast<AffineStoreOp>(storeOpInst).getMemRef() == memref)
                  storesForMemref.push_back(storeOpInst);

```
### Line 1603-1648
```
              assert(storesForMemref.size() == 1);
              auto *newMemRef = createPrivateMemRef(
                  dstAffineForOp, storesForMemref[0], bestDstLoopDepth,
                  fastMemorySpace, localBufSizeThreshold);
              visitedMemrefs.insert(newMemRef);
              // Create new node in dependence graph for 'newMemRef' alloc op.
              unsigned newMemRefNodeId =
                  mdg->addNode(newMemRef->getDefiningOp());
              // Add edge from 'newMemRef' node to dstNode.
              mdg->addEdge(newMemRefNodeId, dstId, newMemRef);
            }

            // Collect dst loop stats after memref privatization transformation.
            LoopNestStateCollector dstLoopCollector;
            dstLoopCollector.collect(dstAffineForOp.getOperation());

            // Add new load ops to current Node load op list 'loads' to
            // continue fusing based on new operands.
            for (auto *loadOpInst : dstLoopCollector.loadOpInsts) {
              auto *loadMemRef = cast<AffineLoadOp>(loadOpInst).getMemRef();
              if (visitedMemrefs.count(loadMemRef) == 0)
                loads.push_back(loadOpInst);
            }

            // Clear and add back loads and stores.
            mdg->clearNodeLoadAndStores(dstNode->id);
            mdg->addToNode(dstId, dstLoopCollector.loadOpInsts,
                           dstLoopCollector.storeOpInsts);
            // Remove old src loop nest if it no longer has outgoing dependence
            // edges, and if it does not write to a memref which escapes the
            // function. If 'writesToLiveInOrOut' is true, then 'srcNode' has
            // been fused into 'dstNode' and write region of 'dstNode' covers
            // the write region of 'srcNode', and 'srcNode' has no other users
            // so it is safe to remove.
            if (writesToLiveInOrOut || mdg->canRemoveNode(srcNode->id)) {
              mdg->removeNode(srcNode->id);
              srcNode->op->erase();
            } else {
              // Add remaining users of 'oldMemRef' back on the worklist (if not
              // already there), as its replacement with a local/private memref
              // has reduced dependences on 'oldMemRef' which may have created
              // new fusion opportunities.
              if (mdg->outEdges.count(srcNode->id) > 0) {
                SmallVector<MemRefDependenceGraph::Edge, 2> oldOutEdges =
                    mdg->outEdges[srcNode->id];
                for (auto &outEdge : oldOutEdges) {

```
### Line 1658-1781
```
        }
      }
    }
  }

  // Visits each node in the graph, and for each node, attempts to fuse it with
  // its sibling nodes (nodes which share a parent, but no dependence edges).
  void fuseSiblingNodes() {
    init();
    while (!worklist.empty()) {
      unsigned dstId = worklist.back();
      worklist.pop_back();
      worklistSet.erase(dstId);

      // Skip if this node was removed (fused into another node).
      if (mdg->nodes.count(dstId) == 0)
        continue;
      // Get 'dstNode' into which to attempt fusion.
      auto *dstNode = mdg->getNode(dstId);
      // Skip if 'dstNode' is not a loop nest.
      if (!isa<AffineForOp>(dstNode->op))
        continue;
      // Attempt to fuse 'dstNode' with its sibling nodes in the graph.
      fuseWithSiblingNodes(dstNode);
    }
  }

  // Attempt to fuse 'dstNode' with sibling nodes in the graph.
  void fuseWithSiblingNodes(Node *dstNode) {
    DenseSet<unsigned> visitedSibNodeIds;
    std::pair<unsigned, Value *> idAndMemref;
    while (findSiblingNodeToFuse(dstNode, &visitedSibNodeIds, &idAndMemref)) {
      unsigned sibId = idAndMemref.first;
      Value *memref = idAndMemref.second;
      // TODO(andydavis) Check that 'sibStoreOpInst' post-dominates all other
      // stores to the same memref in 'sibNode' loop nest.
      auto *sibNode = mdg->getNode(sibId);
      // Compute an operation list insertion point for the fused loop
      // nest which preserves dependences.
      assert(sibNode->op->getBlock() == dstNode->op->getBlock());
      Operation *insertPointInst =
          sibNode->op->isBeforeInBlock(dstNode->op)
              ? mdg->getFusedLoopNestInsertionPoint(sibNode->id, dstNode->id)
              : mdg->getFusedLoopNestInsertionPoint(dstNode->id, sibNode->id);
      if (insertPointInst == nullptr)
        continue;

      // Check if fusion would be profitable and at what depth.

      // Get unique 'sibNode' load op to 'memref'.
      SmallVector<Operation *, 2> sibLoadOpInsts;
      sibNode->getLoadOpsForMemref(memref, &sibLoadOpInsts);
      // Currently findSiblingNodeToFuse searches for siblings with one load.
      assert(sibLoadOpInsts.size() == 1);
      Operation *sibLoadOpInst = sibLoadOpInsts[0];
      assert(!sibNode->stores.empty());
      // TODO(andydavis) Choose the store which postdominates all other stores.
      auto *sibStoreOpInst = sibNode->stores.back();

      // Gather 'dstNode' load ops to 'memref'.
      SmallVector<Operation *, 2> dstLoadOpInsts;
      dstNode->getLoadOpsForMemref(memref, &dstLoadOpInsts);

      // Gather 'dstNode' store ops to 'memref'.
      SmallVector<Operation *, 2> dstStoreOpInsts;
      dstNode->getStoreOpsForMemref(memref, &dstStoreOpInsts);

      unsigned bestDstLoopDepth;
      mlir::ComputationSliceState sliceState;

      // Check if fusion would be profitable.
      if (!isFusionProfitable(sibLoadOpInst, sibStoreOpInst, dstLoadOpInsts,
                              dstStoreOpInsts, &sliceState, &bestDstLoopDepth,
                              maximalFusion))
        continue;

      // Fuse computation slice of 'sibLoopNest' into 'dstLoopNest'.
      auto sliceLoopNest = mlir::insertBackwardComputationSlice(
          sibLoadOpInst, dstLoadOpInsts[0], bestDstLoopDepth, &sliceState);
      if (sliceLoopNest != nullptr) {
        auto dstForInst = cast<AffineForOp>(dstNode->op);
        // Update operation position of fused loop nest (if needed).
        if (insertPointInst != dstForInst.getOperation()) {
          dstForInst.getOperation()->moveBefore(insertPointInst);
        }
        // Update data dependence graph state post fusion.
        updateStateAfterSiblingFusion(sliceLoopNest, sibNode, dstNode);
      }
    }
  }

  // Searches function argument uses and the graph from 'dstNode' looking for a
  // fusion candidate sibling node which shares no dependences with 'dstNode'
  // but which loads from the same memref. Returns true and sets
  // 'idAndMemrefToFuse' on success. Returns false otherwise.
  bool findSiblingNodeToFuse(Node *dstNode,
                             DenseSet<unsigned> *visitedSibNodeIds,
                             std::pair<unsigned, Value *> *idAndMemrefToFuse) {
    // Returns true if 'sibNode' can be fused with 'dstNode' for input reuse
    // on 'memref'.
    auto canFuseWithSibNode = [&](Node *sibNode, Value *memref) {
      // Skip if 'outEdge' is not a read-after-write dependence.
      // TODO(andydavis) Remove restrict to single load op restriction.
      if (sibNode->getLoadOpCount(memref) != 1)
        return false;
      // Skip if there exists a path of dependent edges between
      // 'sibNode' and 'dstNode'.
      if (mdg->hasDependencePath(sibNode->id, dstNode->id) ||
          mdg->hasDependencePath(dstNode->id, sibNode->id))
        return false;
      // Skip sib node if it loads to (and stores from) the same memref on
      // which it also has an input dependence edge.
      DenseSet<Value *> loadAndStoreMemrefSet;
      sibNode->getLoadAndStoreMemrefSet(&loadAndStoreMemrefSet);
      if (llvm::any_of(loadAndStoreMemrefSet, [=](Value *memref) {
            return mdg->getIncomingMemRefAccesses(sibNode->id, memref) > 0;
          }))
        return false;

      // Check that all stores are to the same memref.
      DenseSet<Value *> storeMemrefs;
      for (auto *storeOpInst : sibNode->stores) {
        storeMemrefs.insert(cast<AffineStoreOp>(storeOpInst).getMemRef());
      }

```
### Line 1782-1814
```
      if (storeMemrefs.size() != 1)
        return false;
      return true;
    };

    // Search for siblings which load the same memref function argument.
    auto fn = dstNode->op->getParentOfType<FuncOp>();
    for (unsigned i = 0, e = fn.getNumArguments(); i != e; ++i) {
      for (auto *user : fn.getArgument(i)->getUsers()) {
        if (auto loadOp = dyn_cast<AffineLoadOp>(user)) {
          // Gather loops surrounding 'use'.
          SmallVector<AffineForOp, 4> loops;
          getLoopIVs(*user, &loops);
          // Skip 'use' if it is not within a loop nest.
          if (loops.empty())
            continue;
          Node *sibNode = mdg->getForOpNode(loops[0]);
          assert(sibNode != nullptr);
          // Skip 'use' if it not a sibling to 'dstNode'.
          if (sibNode->id == dstNode->id)
            continue;
          // Skip 'use' if it has been visited.
          if (visitedSibNodeIds->count(sibNode->id) > 0)
            continue;
          // Skip 'use' if it does not load from the same memref as 'dstNode'.
          auto *memref = loadOp.getMemRef();
          if (dstNode->getLoadOpCount(memref) == 0)
            continue;
          // Check if 'sibNode/dstNode' can be input-reuse fused on 'memref'.
          if (canFuseWithSibNode(sibNode, memref)) {
            visitedSibNodeIds->insert(sibNode->id);
            idAndMemrefToFuse->first = sibNode->id;
            idAndMemrefToFuse->second = memref;

```
### Line 1816-1859
```
          }
        }
      }
    }

    // Search for siblings by following edges through an intermediate src node.
    // Collect candidate 'dstNode' input edges in 'inEdges'.
    SmallVector<MemRefDependenceGraph::Edge, 2> inEdges;
    mdg->forEachMemRefInputEdge(
        dstNode->id, [&](MemRefDependenceGraph::Edge inEdge) {
          // Add 'inEdge' if it is a read-after-write dependence.
          if (dstNode->getLoadOpCount(inEdge.value) > 0 &&
              mdg->getNode(inEdge.id)->getStoreOpCount(inEdge.value) > 0)
            inEdges.push_back(inEdge);
        });

    // Search for sibling nodes to fuse by visiting output edges from each input
    // edge in 'inEdges'.
    for (auto &inEdge : inEdges) {
      // Collect candidate output edges from each node 'inEdge.id' in 'inEdges'.
      SmallVector<MemRefDependenceGraph::Edge, 2> outEdges;
      mdg->forEachMemRefOutputEdge(
          inEdge.id, [&](MemRefDependenceGraph::Edge outEdge) {
            unsigned sibNodeId = outEdge.id;
            if (visitedSibNodeIds->count(sibNodeId) > 0)
              return;
            // Skip output edge if not a sibling using the same memref.
            if (outEdge.id == dstNode->id || outEdge.value != inEdge.value)
              return;
            auto *sibNode = mdg->getNode(sibNodeId);
            if (!isa<AffineForOp>(sibNode->op))
              return;
            // Check if 'sibNode/dstNode' can be input-reuse fused on 'memref'.
            if (canFuseWithSibNode(sibNode, outEdge.value)) {
              // Add candidate 'outEdge' to sibling node.
              outEdges.push_back(outEdge);
            }
          });

      // Add first candidate if any were returned.
      if (!outEdges.empty()) {
        visitedSibNodeIds->insert(outEdges[0].id);
        idAndMemrefToFuse->first = outEdges[0].id;
        idAndMemrefToFuse->second = outEdges[0].value;

```
### Line 1863-1909
```
    return false;
  }

  void updateStateAfterSiblingFusion(AffineForOp sliceLoopNest, Node *sibNode,
                                     Node *dstNode) {
    // Update 'sibNode' and 'dstNode' input/output edges to reflect fusion.
    mdg->updateEdges(sibNode->id, dstNode->id);

    // Collect slice loop stats.
    LoopNestStateCollector sliceCollector;
    sliceCollector.collect(sliceLoopNest.getOperation());
    // Promote single iteration slice loops to single IV value.
    for (auto forOp : sliceCollector.forOps) {
      promoteIfSingleIteration(forOp);
    }

    // Collect dst loop stats after memref privatization transformation.
    auto dstForInst = cast<AffineForOp>(dstNode->op);
    LoopNestStateCollector dstLoopCollector;
    dstLoopCollector.collect(dstForInst.getOperation());
    // Clear and add back loads and stores
    mdg->clearNodeLoadAndStores(dstNode->id);
    mdg->addToNode(dstNode->id, dstLoopCollector.loadOpInsts,
                   dstLoopCollector.storeOpInsts);
    // Remove old sibling loop nest if it no longer has outgoing dependence
    // edges, and it does not write to a memref which escapes the
    // function.
    if (mdg->getOutEdgeCount(sibNode->id) == 0) {
      mdg->removeNode(sibNode->id);
      sibNode->op->erase();
    }
  }

  // Clean up any allocs with no users.
  void eraseUnusedMemRefAllocations() {
    for (auto &pair : mdg->memrefEdgeCount) {
      if (pair.second > 0)
        continue;
      auto *memref = pair.first;
      // Skip if there exist other uses (return operation or function calls).
      if (!memref->use_empty())
        continue;
      // Use list expected to match the dep graph info.
      auto *op = memref->getDefiningOp();
      if (isa_and_nonnull<AllocOp>(op))
        op->erase();
    }

```
### Line 1911-1925
```
};

} // end anonymous namespace

void LoopFusion::runOnFunction() {
  // Override if a command line argument was provided.
  if (clFusionFastMemorySpace.getNumOccurrences() > 0) {
    fastMemorySpace = clFusionFastMemorySpace.getValue();
  }

  // Override if a command line argument was provided.
  if (clFusionLocalBufThreshold.getNumOccurrences() > 0) {
    localBufSizeThreshold = clFusionLocalBufThreshold * 1024;
  }


```

## _tensorflow_python_framework_composite_tensor_test_py
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
"""Tests for tensorflow.python.framework.composite_tensor."""

from __future__ import absolute_import
from __future__ import division

```
### Line 79-89
```
    return (type(self) is type(other) and
            self.components == other.components and
            self.metadata == other.metadata)


# Another test CompositeTensor class.  `tf.nest` should treat different CT
# classes as different structure types (e.g. for assert_same_structure).
class CTSpec2(CTSpec):
  pass



```
### Line 219-236
```
  ])  # pyformat: disable
  def testNestAssertSameStructureCompositeMismatch(self,
                                                   s1,
                                                   s2,
                                                   error=ValueError):
    # s1 and s2 have the same structure if expand_composites=False; but
    # different structures if expand_composites=True.
    nest.assert_same_structure(s1, s2, expand_composites=False)
    nest.assert_shallow_structure(s1, s2, expand_composites=False)
    with self.assertRaises(error):  # pylint: disable=g-error-prone-assert-raises
      nest.assert_same_structure(s1, s2, expand_composites=True)

  @parameterized.parameters([
      # Note: there are additional test cases in testNestAssertSameStructure.
      {'s1': [1], 's2': [CT(1)]},
      {'s1': [[CT([1, 2, 3])], 100, {'y': CT([5, 6])}],
       's2': [[CT([1, 2, 3])], 100, {'y': CT([CT([4, 5]), 6])}],
       'expand_composites': False},

```
### Line 240-250
```
  ])  # pyformat: disable
  def testNestAssertShallowStructure(self, s1, s2, expand_composites=True):
    nest.assert_shallow_structure(s1, s2, expand_composites=expand_composites)

  @parameterized.parameters([
      # Note: there are additional test cases in
      # testNestAssertSameStructureCompositeMismatch.
      {'s1': [[CT([1, 2, 3])], 100, {'y': CT([CT([4, 5]), 6])}],
       's2': [[CT([1, 2, 3])], 100, {'y': CT([5, 6])}]},
      {'s1': CT([1, 2, 3]),
       's2': [1, 2, 3],

```
### Line 304-313
```

    result = nest.map_structure_with_paths(
        func1, structure, expand_composites=expand_composites)
    self.assertEqual(result, expected)

    # Use the same test cases for map_structure_with_tuple_paths.
    def func2(tuple_path, x):
      return '%s:%s' % ('/'.join(str(v) for v in tuple_path), x)

    result = nest.map_structure_with_tuple_paths(

```
### Line 339-361
```
        func, structure, expand_composites=True)
    expected = [CT([True, True], metadata='A'), False]
    self.assertEqual(result, expected)

  def testMemoryIsFreed(self):
    # Note: we use `np.array` values for CT and `set` values for
    # metadata because we need to construct weakrefs to them.  Other builtin
    # types, such as `list` and `tuple`, do not support weakrefs.
    ct1 = CT(np.array([1, 2]), set(['no', 'leaks']))
    ct2 = CT(np.array([3, 4]), set(['no', 'leaks']))
    ct3 = CT(np.array([5, 6]), set(['other', 'metadata']))

    # Note: map_structure exercises flatten, pack_sequence_as, and
    # assert_same_structure.
    func = lambda x, y: x + y
    ct4 = nest.map_structure(func, ct1, ct2, expand_composites=True)

    # Check that the exception-raising path in assert_same_structure
    # doesn't leak any objects.
    with self.assertRaises(ValueError):
      nest.map_structure(func, ct2, ct3, expand_composites=True)
    if hasattr(sys, 'exc_clear'):
      sys.exc_clear()  # Remove any references in exception stack traces.

```
### Line 373-382
```
    del ct1, ct2, ct3, ct4
    gc.collect()
    for ref in refs:
      self.assertIsNone(ref())

  # pylint: disable=g-long-lambda
  @parameterized.named_parameters([
      ('IndexedSlicesNoDenseShape', lambda: ops.IndexedSlices(
          constant_op.constant([1, 2, 3]), constant_op.constant([2, 8, 4]))),
      ('IndexedSlicesInt32DenseShape', lambda: ops.IndexedSlices(

```

# Issues
## 27789
Title:
```

        The text generation tutorial doesn't seem to be passing along hidden state while generating text
      
```
Author:
```
lwander
```
Text:
```

System information

TensorFlow version: tensorflow-gpu==1.10.1
Doc Link: https://www.tensorflow.org/tutorials/sequences/text_generation#the_prediction_loop

Describe the documentation issue
I followed the text generation tutorial, and trained my model until it achieved a cross entropy loss of ~0.5 after 30 epochs; however, the generated text was mostly garbage. Reading the code linked in the section above, I saw:
      # We pass the predicted word as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)
which doesn't make sense to me. The comment says we're passing along the hidden state (which maybe the model is doing for us?) but the only text that's passed along is the last predicted character. After modifying the text generation function to pass to the model last at most seq_length generated characters, the output text started to look like actual Shakespeare/English.
My question is: is the model supposed to implicitly propagate hidden state, (and I've done something wrong following the tutorial), or is the tutorial accidentally omitting the part where we pass along the last set of generated text?

Note: Since I'm running tensorflow 1.10, and the tutorial seems to require 1.13 I had to replace the loss function with tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits). I don't think that change is related, but is it possible that tf 1.10 doesn't propagate the hidden state in the model?

We welcome contributions by users. Will you be able to update submit a PR (use the doc style guide) to fix the doc Issue?
I'm happy to contribute my code changes to the tutorial, but want to make sure I'm understanding what's going wrong first.

```
Author:
```
ymodak
```
Text:
```

For running locally, tutorial requires TF >=1.11 You can also use google colab to execute this tutorial. It hosts TF 1.13.1 by default.

```
Author:
```
lwander
```
Text:
```

Does this mean the behavior of
      predictions = model(input_eval)
changes between tensorflow 1.10 & 1.11? Namely, does the GRU cell not pass forward hidden state in tensorflow 1.10?

```
Author:
```
qlzh727
```
Text:
```

The stateful RNN behavior hasn't been update/change for long time, the hidden state is attached to the model instance, and is just as initial state when the new input is coming.
The line of input_eval is just using the previous output and make it the new input. As long as the model.reset_state() is not called, the hidden state will always be attached to the model, and been updated when the calculation is performed.

```
Author:
```
lwander
```
Text:
```

Yeah, that's what I had assumed, which is why I was so surprised at how different the results were when explicitly passing past characters into the model vs. only passing the last generated character.  model.reset_state() is only called once before we start feeding the model any characters.
Trained to a loss of ~0.5, and with a temperature of 1.0
here is what the code generates without any modifications:
ROMEO:
SIERING thed.
Foro yo an whizeve wick.

CLo he ost.
DUERESUSthoupinaio micore helell ghacheer ofismyo hin inghisicalir whice SI st thire aree f byondeminie, hindathe prd t'
RDurrin ve if aft wea IORWhis dat, aile boomeceanant ighea bustad, che Katauind, d wendowhelld lde chiom dwotasis whench we he

here is what the code generates with the modification described above:
ROMEO:
Good Paulina,
Who hast deep a sinner to the crown?

KING RICHARD III:
Nor newt before him, we have comes consorn.

KING HENRY VI:
Then know, I'll tell thee for thy sacred blood rich groat;
And when thou fail'st--as God again; my brother's son
It rawn his convent and dispatch with him.

Is there any way I can inspect the models hidden state?

```
Author:
```
qlzh727
```
Text:
```

Since the model is built with return_sequence=True, it should intake sequences and output sequences. So when you ask model to generate new test, the input should be previously generated words or sequences, not just the last char it previous generated.
To exam the hidden state of the model, specially for the GRU layer, you can get the state by gru_layer.states.

```
Author:
```
qlzh727
```
Text:
```

Also adding Mark who works on documentation.

```
Author:
```
lwander
```
Text:
```


Since the model is built with return_sequence=True, it should intake sequences and output sequences. So when you ask model to generate new test, the input should be previously generated words or sequences, not just the last char it previous generated.

If I remove return_sequences=true from the GRU layer, should the tutorial work as shown? (I'll try that right now).

To exam the hidden state of the model, specially for the GRU layer, you can get the state by gru_layer.states.

Sorry, I don't exactly follow, where is gru_layer defined?

```
Author:
```
lwander
```
Text:
```

Removing return_sequences=True causes a dimension mismatch:
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding (Embedding)        (64, None, 256)           16640
_________________________________________________________________
cu_dnngru (CuDNNGRU)         (64, 1024)                3938304
_________________________________________________________________
dense (Dense)                (64, 65)                  66625
=================================================================
Total params: 4,021,569
Trainable params: 4,021,569
Non-trainable params: 0
_________________________________________________________________
Epoch 1/10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "shakespeare.py", line 88, in train
    history = model.fit(dataset.repeat(), epochs=epochs, steps_per_epoch=steps_per_epoch, callbacks=[checkpoint_callback])
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training.py", line 1348, in fit
    validation_steps=validation_steps)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training_eager.py", line 1040, in fit_loop
    do_validation=do_validation)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training_eager.py", line 284, in iterator_fit_loop
    model, x, y, sample_weights=sample_weights, training=True)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training_eager.py", line 794, in _process_single_batch
    training=training)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training_eager.py", line 155, in _model_loss
    targets[i], outs[i], weights, mask=mask)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training_utils.py", line 437, in weighted
    score_array = fn(y_true, y_pred)
  File "shakespeare.py", line 70, in loss
    return tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits)
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/ops/nn_ops.py", line 2053, in sparse_softmax_cross_entropy_with_logits
    (labels_static_shape.ndims, logits.get_shape().ndims))
ValueError: Rank mismatch: Rank of labels (received 2) should equal rank of logits minus 1 (received 2).

Note, I'm using sparse_softmax_cross_entropy_with_logits due to my TF version being 1.10

```
Author:
```
qlzh727
```
Text:
```

The return_sequence is definitely needed, otherwise it will return the output with last timestep instead of all timesteps.
For gru_layer, you created it within the build_model, you can access the model.layers which should contain all the layers in the model, and gru layer should be one of them.

```

## 15238
Title:
```

        CPU usage drops after several steps
      
```
Author:
```
bachiraoun
```
Text:
```

I am running a tensorflow computation graph. The same graph was running fine before but all of a sudden I noticed that after several steps and checkpoint the CPU usage drops from more than 600% to 100% for the rest of the session. It seems like all executors are dying (when saving maybe) and the computation keeps running on only 1 Core shooting up and down from 100 to 200%.
I also posted the issue on stack overflow: https://stackoverflow.com/questions/47720893/tensor-flow-cpu-usage-drops-after-saving

```
Author:
```
drpngx
```
Text:
```

Any logs? I'm assuming this is training? Single machine? What does nvidia-smi say? Can you fill out the template with system arch etc?

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
bachiraoun
```
Text:
```

Thank you.
here are the info
Have I written custom code:
YES
OS Platform and Distribution:
MacBook Pro (Retina, 15-inch, Mid 2015)
Processor 2.8 GHz Intel Core i7
Memory 16 GB 1600 MHz DDR3
TensorFlow installed from
using pip
TensorFlow version
1.4.1
Bazel version
Build label: 0.4.4-homebrew
Build target: bazel-out/local-opt/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar
Build time: Thu Feb 2 01:06:46 2017 (1485997606)
Build timestamp: 1485997606
Build timestamp as int: 1485997606
CUDA/cuDNN version
N/A
GPU model and memory
N/A
Exact command to reproduce
I provided the code.
I was running very similar code on jupiter notebook for maybe 1 month. All of a sudden I started having the CPU dropping issues. Those issues are not persistent and I am getting no error message or warning.
Any logs? No or not sure where to get them
I'm assuming this is training?  Yes
Single machine?  Yes
Thank you.

```
Author:
```
andydavis1
```
Text:
```

Can you post code that reproduces the problem?

```
Author:
```
tensorflowbutler
```
Text:
```

It has been 14 days with no activity and the awaiting response label was assigned. Is this still an issue? Please update the label and/or status accordingly.

```
Author:
```
bachiraoun
```
Text:
```

Sorry for not replying earlier. The code producing the drop to 1 core is attached in the first message.
But regardless please close the issue thread because for whatever reason now it's been working without any issue for more than a week. magic !

```

## 17910
Title:
```

        Timeline Logging Duplicates of Operations
      
```
Author:
```
xilenteyex
```
Text:
```

System information

Have I written custom code (as opposed to using a stock example script provided in TensorFlow): No
OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Linux Ubuntu 16.04
TensorFlow installed from (source or binary): source
TensorFlow version (use command below): 1.6.0-rc1
Python version: 2.7
Bazel version (if compiling from source): 0.11.0
GCC/Compiler version (if compiling from source): 5.4
CUDA/cuDNN version: 9.1/7.0
GPU model and memory: Tesla k80 (11441MiB)
Exact command to reproduce: python cifar10_train.py

Describe the problem
I used timeline to profile the time taken by each operation of the standard cifar10 model available in tensorflow/models repo. After looking at the logfile, it looks like logs of some of the operations are duplicated i.e. it looks like some of the operations in the graph are ran multiple times over the single run of the complete graph. For example, Operation "gradients/conv2/Conv2D_grad/Conv2DBackpropFilter" (link to logfile : https://gist.github.com/xilenteyex/d54305e0448e1aa3d878872c45b8ed3a#file-timeline-1-json-L2270) is logged multiple times. Is this some sort of bug or am I missing something?
Thanks a lot for looking into this issue!
Source code / logs
cifar10 example : https://github.com/tensorflow/models/tree/master/tutorials/image/cifar10
here is a the link to my modified version of cifar10_train.py in which I added logging :
https://gist.github.com/xilenteyex/b6fab3a5abdb65bf674aa7d0a4ec4b5c
one of the sample log files is : https://gist.github.com/xilenteyex/d54305e0448e1aa3d878872c45b8ed3a

```
Author:
```
aselle
```
Text:
```

@prb12, PTAL.

```
Author:
```
xilenteyex
```
Text:
```

Any sort of Input is much appreciated.
Thanks!

```
Author:
```
prb12
```
Text:
```

Well, it's very hard to see what the problem might be from the "modified code" link you sent because the timeline capturing code is commented out in a way that obfuscates the original control-flow:
      #run_metadata = tf.RunMetadata()
      #count = 0
      while not mon_sess.should_stop():
#        mon_sess.run(train_op, options=tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE), run_metadata=run_metadata)
        mon_sess.run(train_op)
#        from tensorflow.python.client import timeline
#        trace = timeline.Timeline(step_stats=run_metadata.step_stats)
#        trace_file = open('timeline_%d_cifar10_cpu.ctf.json' % (count), 'w')
#        trace_file.write(trace.generate_chrome_trace_format())
#        count += 1

But... the fact that you create the tf.RunMetadata protobuf outside the loop and potentially reuse it many times means that you quite probably have merged a bunch of StepStats into the same protobuf.  The Timeline code would be very confused by this.
To debug, I would suggest writing step_stats to a file, or printing it out.  If there are numerous copies of the same step/ops in there then its not a timeline problem.
But first I would try making a new tf.RunMetadata object for each sess.run call, make sure you just trace a single step and only write the trace file once.
Failing any of those, I would suspect maybe something funny with the CUPTI library version and/or GPU driver-  but that seems very unlikely.

```
Author:
```
xilenteyex
```
Text:
```

Hi @prb12 ,
Thanks for replying.
I am trying to understand logging in tensorflow in depth. I think cifar is slightly a bigger model to start with. Now, I am using a MNIST example. Script that I ran can be found (here). Following is the list of issues:


I made sure that run_metadata is called separately for every sess.run call. I am still seeing multiple entries for the same operation in the same thread . For example, op named "train/Adam/update_layer2/weights/Variable/ApplyAdam" is logged three times in pid = '11'. Does this really mean that my model is designed in such a way that it requires "train/Adam/update_layer2/weights/Variable/ApplyAdam" op to be executed three times for each sess.run call ? (step_stats can be found here and timline can be found here)


According to my understanding (please correct me, if I am wrong). There are 4 threads running on GPU, one is responsible for MEMCPYHtoD, one for MEMCPYDtoH, one for MEMCPYPtoP and one thread for execution of compute nodes. But, I see a lot of GPU streams in the timeline, is this just an artifact of timeline to enable it to be visualized in the timeline or it has some other significance ?


Also, reading ur comments, on other issues, I understand that the pid named : "/job:localhost/replica:0/task:0/device:GPU:0 Compute" just logs the time it takes to launch the kernel on the GPU. Actual execution time is logged in the streams named "/device:GPU:0/stream:* Compute". But after looking at the timestamps and the duration, it looks like "/job:localhost/replica:0/task:0/device:GPU:0 Compute" is actually logging the total time (kernel launch + actual compute node execution time on GPU) e.g.
for the op "train/Adam/update_layer2/weights/Variable/ApplyAdam", there is one entry in "/job:localhost/replica:0/task:0/device:GPU:0 Compute" (pid : 9) which starts at timestamp : 1536530947160930 and ends at 1536530947161023, but there are three entries in the pid : 11, named : "/device:GPU:0/stream:22 Compute". These three entries start and end with timestamps as follows:
(start, end)
(1536530947160982, 1536530947160984)
(1536530947160999, 1536530947161001)
(1536530947161016, 1536530947161021)
All three of these have starting time after the start timestamp of "/job:localhost/replica:0/task:0/device:GPU:0 Compute" and ends before the end timestamp of "/job:localhost/replica:0/task:0/device:GPU:0 Compute". What does this really mean ? What does these gaps in these three timeslots show? Also, I expect actual execution to start after the kernel has been queued. These timestamps show otherwise. Am I missing something ? Also, if they are executed three times, I expect three kernels to be queued, but "/job:localhost/replica:0/task:0/device:GPU:0 Compute" process has only one entry.
Also, what is the difference between two GPU streams "/device:GPU:0/stream:22 Compute" (pid: 11) and "/device:GPU:0/stream:all Compute" (pid: 7)


In pid: "5" named "/device:GPU:0/memcpy Compute", I assumed that it will only contain memcpy nvidia cuda operations. But, there is an op of type "Assign" in this stream. Is this the expected behavior ?


In order to log the time it takes to send a tensor from one one device to another, is it enough to look at the duration and timestamps of memcpy ops ? or do i need to enable logging of send/recv op nodes using the hack as discussed in this github issue ? If those memcpy ops report the correct times and we don't really need the hack to enable the send/recv ops. Is there a way to map MEMCPY ops to tensors ?


Also, whats the purpose of "/device:GPU:0/stream:* Tensors" and "/job:localhost/replica:0/task:0/device:GPU:0 Tensors" processes ?


Overall, for a given tensorflow graph, I am interested in creating a timeline programmatically (not UI, raw values), using which I can find the time at which an op (compute as well as communication op) started and the time it took to complete. Do you think tensorflow.timeline is the right way to go about doing this ?


P.S. : I am sorry, I know this is not a discussion forum and lack of documentation about usage and what each field represents about logging, I am unable to figure out how to use this exactly. I tried asking the same thing over stackoverflow a few times, but my questions remained unanswered. I am stuck at this for almost 3 months now. If you can clarify all these things, that wil be awesome!
Thanks a lot for looking into this.

```
Author:
```
xilenteyex
```
Text:
```

@prb12 ,  it will be great if you can look into this.
Thanks!

```

## 5250
Title:
```

        NaN gradient after py_func call
      
```
Author:
```
Heungwoo
```
Text:
```

Hello,
I did implemented faster rcnn with py_func op.

py-func is placed in the middle of graph. And there are the other path in parallel with py_func node.
I did not add any gradient function for it, So it should ignore gradient path through py_func. And gradient calculation should done with connection from the other path.

It works fine in tensorflow r0.9 version.
But, in the tensorflow version > r0.9, the node before py_func get NaN error when writing histogram summary. .
I did check several version: r0.10, r0.11, all of them does not worked.
Is there any change in gradient calculation for the node which have connection with py_func node ?
Or should I use py-func in different way?
Any advice will be helpful for me.
Thanks in advance.

```
Author:
```
drpngx
```
Text:
```

Do you happen to have a small repro case?

```
Author:
```
Heungwoo
```
Text:
```

It is not the pyfunc which makes NaN value.
Softmax_with_cross_entropy funcution was changed in version 0.10 and it return NaN if label gt is not in valid label value range. I did you "-1" label as ignore-label in version 0.9 and just use valid index value to calculate loss. But migrating it to upper version, it makes NaN loss.
Sorry to make mistake.

```
Author:
```
drpngx
```
Text:
```

Good to know. Glad you figured it out!

```

## 20092
Title:
```

        Tensorflow Website XSRF Token missing or incorrect
      
```
Author:
```
MellonGuan
```
Text:
```

The error occurs when I click develop button in "www.tensorflow.org/programmers_guide/variables" or in everywhere. My default lang is set to English(but it does not matter and has influence only on the bottom menu). But when I'm trying to change the language to Chinese I get the following error message:

XSRF Token missing or incorrect



Windows 10
Version 67.0.3396.87 (Official Build) (64-bit)

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
asimshankar
```
Text:
```

@wolffg - mind taking a look?

```
Author:
```
wolffg
```
Text:
```

There are XSRF issues with switching languages if you are signed in with multiple accounts.  Is that the case here?

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @wolffg: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
wolffg
```
Text:
```

Given there's been no followup in two weeks, I'm closing this.  We are aware of a bug with XSRF and multi-login, and I assume this is was what happened here.  The site eng team is working on it.
If it wasn't please reopen or refile.  Thanks!

```

## 548
Title:
```

        Latest dev release actually slower than 0.5
      
```
Author:
```
nryant
```
Text:
```

After updating TensorFlow to the most recent source yesterday (I'm at b1cabed), I've noticed that while GPU utilization frequently appears much higher in nividia-smi than in prior releases, my actual code is much slower. Some sequence to sequence models I was training began taking 3-4 times as long per step, despite GPU utilization hovering between 60 and 99%, which is much higher than I have observed in the past. As I have code for benchmarking fully connected feedforward networks on MNIST in various frameworks, I dusted that off and, again, slower. Previously, training a network with three hidden layers of 2,048 rectified linear units + dropout (input + hidden) took 1.78 seconds per epoch (averaged over 10 epochs)  when trained using vanilla SGD with momentum and a minibatch size of 256. That is now up to 65.2 seconds. This holds across different combinations of hidden layer sizes and minibatch sizes. On the other hand, convolutional net performance does not seem to be affected as when I run Soumith's convolutional net benchmarks, I get numbers close to what he originally reported using the same test setup.
So to summarize, I've been recompiling TensorFlow regularly (every few days since its release) and after the most recent compile noticed a quite substantial performance hit for vanilla fully connected feedforward and recurrent architectures, but not for convolutional networks. This is all with TensorFlow running on a Titan X with no other processes running and using the most recent versions of CUDA, cuDNN (well, I have v3 installed, not the release candidate for v4), cuBLAS, etc.

```
Author:
```
zheng-xq
```
Text:
```

@nryant, we will look into this problem. But to make sure we are looking at
the same problem, could you provide some more reproducing details? It will
be very helpful if you can point us to a model either comes with TF, or
written by you, that is confirmed to be slower on TF-0.6 and faster on
TF-0.5.
On Fri, Dec 18, 2015 at 8:10 AM, Martin Wicke notifications@github.com
wrote:

Assigned #548 #548 to
@zheng-xq https://github.com/zheng-xq.
—
Reply to this email directly or view it on GitHub
#548 (comment).


```
Author:
```
nryant
```
Text:
```

Over the weekend I can put up a repo on github containing code to reproduce the fully connected model I mentioned. I'll also try downgrading to a previous version to see if I can replicate the timings I recorded a few weeks ago. Would that be sufficient?

```
Author:
```
zheng-xq
```
Text:
```

That would be very helpful! Thanks.
On Fri, Dec 18, 2015 at 9:46 AM, nryant notifications@github.com wrote:

Over the weekend I can put up a repo on github containing code to
reproduce the fully connected model I mentioned. I'll also try downgrading
to a previous version to see if I can replicate the timings I recorded a
few weeks ago. Would that be sufficient?
—
Reply to this email directly or view it on GitHub
#548 (comment)
.


```
Author:
```
benoitsteiner
```
Text:
```

We used to compile with our own version of Eigen. We started using the upstream version of Eigen last week, and it turns out that a couple optimizations are missing. I'll fix the upstream version as soon as possible to get back to where we were performance-wise.

```
Author:
```
ebrevdo
```
Text:
```

Benoit, is the correct tanh implementation upstream?
On Dec 21, 2015 12:17 PM, "Benoit Steiner" notifications@github.com wrote:

We used to compile with our own version of Eigen. We started using the
upstream version of Eigen last week, and it turns out that a couple
optimizations are missing. I'll fix the upstream version as soon as
possible to get back to where we were performance-wise.
—
Reply to this email directly or view it on GitHub
#548 (comment)
.


```
Author:
```
nryant
```
Text:
```

The promised repo is at
https://github.com/nryant/tensorflow_mnist_examples/tree/master
and the benchmark located under the feedforward_bench/ directory therein. When run, feedforward_bench/bench.py will spit out to a file average time to complete an epoch (averaged over ten epochs) over MNIST for a fully connected feedforward model with 3 layers and varying layer sizes and minibatch sizes. I've included output from runs using the official 0.60 release and the more recent release cited upthread (see the .txt files). I've also included log files for each run containing device placement for the operations.
As you can see, the more recent release is FAR slower, though rather interestingly nvidia-smi shows much higher GPU utilization for it.

```
Author:
```
JianbangZ
```
Text:
```

is the fix upstream?

```
Author:
```
benoitsteiner
```
Text:
```

I have cheked in several improvements to the upstream eigen repository such as this one. I have also updated the TensorFlow codebase to pull a recent version of Eigen that contains these improvements. This should fix the performance regression issue.

```
Author:
```
nryant
```
Text:
```

As of d1b8333, this performance issue appears resolved. See:
https://github.com/nryant/tensorflow_mnist_examples/blob/master/feedforward_bench/d1b8333_timings.txt

```
Author:
```
benoitsteiner
```
Text:
```

Thanks for verifying the fixes. I'm closing this issue.

```

## 7621
Title:
```

        After installation error
      
```
Author:
```
prabhant
```
Text:
```

Im getting this output



import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))



E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "BestSplits" device_type: "CPU"') fo
r unknown op: BestSplits
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "CountExtremelyRandomStats" device_t
ype: "CPU"') for unknown op: CountExtremelyRandomStats
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "FinishedNodes" device_type: "CPU"')
for unknown op: FinishedNodes
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "GrowTree" device_type: "CPU"') for
unknown op: GrowTree
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "ReinterpretStringToFloat" device_ty
pe: "CPU"') for unknown op: ReinterpretStringToFloat
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "SampleInputs" device_type: "CPU"')
for unknown op: SampleInputs
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "ScatterAddNdim" device_type: "CPU"'
) for unknown op: ScatterAddNdim
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "TopNInsert" device_type: "CPU"') fo
r unknown op: TopNInsert
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "TopNRemove" device_type: "CPU"') fo
r unknown op: TopNRemove
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "TreePredictions" device_type: "CPU"
') for unknown op: TreePredictions
E c:\tf_jenkins\home\workspace\release-win\device\cpu\os\windows\tensorflow\core
\framework\op_kernel.cc:943] OpKernel ('op: "UpdateFertileSlots" device_type: "C
PU"') for unknown op: UpdateFertileSlots
b'Hello, Tensorflow'
But when i run



import tensorflow as tf
#4 line gap
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))



then the output is



b'Hello, TensorFlow!'



so i think its a bug in Tensorflow

```
Author:
```
kaufManu
```
Text:
```

Duplicate with #7500

```
Author:
```
aselle
```
Text:
```

Thanks for pointing this out as a dup @kaufManu .  I'm closing it since #7500 is resolved in nightlies.

```
Author:
```
costa974
```
Text:
```

Python sux

```

## 30874
Title:
```

        base64 strings contains  " "
      
```
Author:
```
gison93
```
Text:
```

URL(s) with the issue:
https://www.tensorflow.org/api_docs/python/tf/io/decode_base64
Description of issue (what needs changing):
Some base64 strings contains  " ".
Clear description
It could be useful to add this information after this paragraph:

Input may or may not have padding at the end. See EncodeBase64 for padding. Web-safe means that input must use - and _ instead of + and  /.


```
Author:
```
ymodak
```
Text:
```

Argument input should cover all string cases.
https://www.tensorflow.org/api_docs/python/tf/io/decode_base64#args
Perhaps you can elaborate more for your doc request? Thanks!

```
Author:
```
gison93
```
Text:
```

My input argument is a base64 string containing spaces.
The standard library base64 is able to decode (ignoring the spaces since are used just for readability) while tf.io.decode_base64 does not recognize that string as a base64 string.
When the spaces are eliminated everything works fine.
I think add a warning on this could be useful:

Input may or may not have padding at the end. See EncodeBase64 for padding. Web-safe means that input must use - and _ instead of + and /.
Input cannot contain " ".


```
Author:
```
ymodak
```
Text:
```

Thanks for elaborating. Its clear now.  Would you like to send a PR to add the message?

```
Author:
```
ymodak
```
Text:
```

tf.io.decode_base64 ignores spaces in the string too. I made a toy example to elaborate;
Tested with TF 1.14.0

String without space

tf.io.decode_base64(input='mystring',name=None) 
<tf.Tensor 'DecodeBase64_14:0' shape=() dtype=string>

String with space

tf.io.decode_base64(input='my string',name=None)
<tf.Tensor 'DecodeBase64_15:0' shape=() dtype=string>
Thanks!

```

## 842
Title:
```

        Tool request: Deep Visualization Toolbox for TensorFlow
      
```
Author:
```
cesarsalgado
```
Text:
```

I would like TensorFlow to have an official tool similar to this https://github.com/yosinski/deep-visualization-toolbox.
It would be helpful to check if our CNNs were learning useful features, to debug, and to have better insights.
Check this video: https://www.youtube.com/watch?v=AgkfIQ4IGaM
Thoughts?

```
Author:
```
bhack
```
Text:
```

👍

```
Author:
```
mathetes87
```
Text:
```

+1
It would be amazing!

```
Author:
```
jeandut
```
Text:
```

+1

```
Author:
```
decentralion
```
Text:
```

This would be really cool to add! It's not on my roadmap for this quarter, but if anyone wants to implement it I'd be happy to discuss design and guide through the process.

```
Author:
```
barneypell
```
Text:
```

+1

```
Author:
```
shendiaomo
```
Text:
```

This quarter is nearly over, how about do it in Q2:-)？@danmane

```
Author:
```
BENMFeng
```
Text:
```

+1

```
Author:
```
decentralion
```
Text:
```

@shendiaomo - sorry, still not on my near or medium term agenda :)

```
Author:
```
kingtaurus
```
Text:
```

Quick workaround;
I believe some of visualization features of this tool can be handled directly within tensorflow (and combined with tensorboard) with a bit of effort.
Issues:

the layout is not ideal (and there are issues with layout of images in general);
extra code means an increased chance for mistakes;
it seems to make the processing much slower :);
it doesn't take into account max_pooling (or other spatial contracting operations);

This provides visualization of output images of each layer (which is part of the requirements - but is in-efficient  👎 );
W_conv1 = weight_variable([3,3,1,128])
#f_x,f_y,depth, number of filters
b_conv1 = bias_variable([128])
cnn_layer_1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

W_conv2 = weight_variable([3,3,128,128])
b_conv2 = bias_variable([128])
cnn_layer_2 = tf.nn.relu(conv2d(cnn_layer_1, W_conv2) + b_conv2)

W_conv3 = weight_variable([3,3,128,128])
b_conv3 = bias_variable([128])
cnn_layer_3 = tf.nn.relu(conv2d(cnn_layer_2, W_conv3) + b_conv3)

#grab only the first element of the batch and 16 filters
layer1_image1 = cnn_layer_1[0:1, :, :, 0:16]
layer2_image1 = cnn_layer_2[0:1, :, :, 0:16]
layer3_image1 = cnn_layer_3[0:1, :, :, 0:16]

layer1_image1 = tf.transpose(layer1_image1, perm=[3,1,2,0])
layer2_image1 = tf.transpose(layer2_image1, perm=[3,1,2,0])
layer3_image1 = tf.transpose(layer3_image1, perm=[3,1,2,0])

layer_combine_1 = tf.concat(2, [layer3_image1, layer2_image1, layer1_image1])
list_lc1 = tf.split(0, 16, layer_combine_1)
layer_combine_1 = tf.concat(1, list_lc1)

tf.image_summary("filtered_images_1", layer_combine_1)
# combine this summary with tensorboard (and you get a decent output);

Looks like (using MNIST):

The other parts would requires a little bit more work (some involve backprop).

```
Author:
```
dyelax
```
Text:
```

Has anyone started working on this? I might take a shot at it if there are no ongoing efforts

```
Author:
```
decentralion
```
Text:
```

@dyelax Feel free to take a shot. If you build it as a standalone Polymer component that would make it easier to integrate into TensorBoard as a new tab. You could try forking one of the existing dashboards and adding the functionality you need.
We plan to make it possible for TensorBoard to request raw Tensor data directly from the backend (i.e. from a tf.summary.tensor_summary) which may be helpful.

```
Author:
```
tarrencev
```
Text:
```

@dandelionmane would it make sense to leverage the existing image summaries for this instead of creating a new summary type?

```
Author:
```
BhagyeshVikani
```
Text:
```

Hi!
We have done some work on this and implemented the algorithm for convolutional neural networks visualization described in http://www.cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf and something similar to https://github.com/yosinski/deep-visualization-toolbox but using Tensorflow instead of caffe. However, we are not yet familiar with the TF codebase/ API to integrate it into the ImageSummary tab of tensorboard. We would like to make it into a part of tensorboard. Could someone suggest a good starting point of how we go about doing this?
Here's how far we've progressed: Given any CNN, we can get the reconstructed images from deconvolution for all the layers in the network as described in the paper above.

```
Author:
```
micahstubbs
```
Text:
```

@BhagyeshVikani that sounds cool! wrapping what you have in a Polymer custom element might be a good strategy. Eager to hear an official answer from the TensorBoard team
https://www.polymer-project.org/1.0/

```
Author:
```
micahstubbs
```
Text:
```

@BhagyeshVikani @dandelionmane did mention a future TensorBoard plugin format recently at #TFDevSummit.
when that plugin format is published, I imagine that's the way to go

```
Author:
```
BhagyeshVikani
```
Text:
```

We have developed a  cool new API for visualizing images reconstructed (as per Visualizing and Understanding Convolutional Networks) from CNN layers using TensorFlow.  Results are written to TensorBoard Images tab as suggested above. Feel free to play around with it and contact us with bugs or hugs- https://github.com/InFoCusp/tf_cnnvis.
Please suggest next steps for integrating it with TensorFlow.
A small glimpse of our results:


```
Author:
```
BhagyeshVikani
```
Text:
```

We also added Deep dream to the arsenal:

















Carbonara
Ibex
Elephant
Ostrich








Cheese burger
Tennis ball
Fountain pen
Clock tower








Cauliflower
Baby Milk bottle
Sea lion
Dolphin




```
Author:
```
wchargin
```
Text:
```

Happy to see that this is such a popular request! It sounds like this would be a perfect fit to be implemented as a new plugin/dashboard (like the scalars dashboard or image dashboard). We're actively working on a new plugin system that will make it easy for external contributors to create such plugins, either to use for themselves or share back to TensorBoard core. Keep an eye out in the coming months!
I've migrated this issue to our new repository at tensorflow/tensorboard#81. Please feel free to continue discussion there.

```
Author:
```
partus
```
Text:
```

We have created a platform for real time visualization  of networks in keras/tensorflow https://github.com/cyberneuron/RT-CNN-Vis . It's similar in concept with deep-visualization-toolbox. It can be used with almost any keras/tensorflow model and it's extendable with other visualization algorithms.

```

## 23290
Title:
```

        Object detection and vibration
      
```
Author:
```
da-iyoulin
```
Text:
```

Please make sure that this is a feature request. As per our GitHub Policy, we only address code/doc bugs, performance issues, feature requests and build/installation issues on GitHub. tag:feature_template
System information

TensorFlow version (you are using):1.9.0
Are you willing to contribute it (Yes/No):NO

Describe the feature and the current behavior/state.
I want to Object detection, if  Object name is equal to stop vibration , else cancel.
Will this change the current api? How?  NO change
Who will benefit with this feature?
Any Other info.
my code：
Vibrator vb = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
if (getLocalClassName() == "STOP")
vb.vibrate(5000);
else if (getLocalClassName() == "turnright")
vb.cancel();
my IDE：android studio
code source：https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/android/src/org/tensorflow/demo/DetectorActivity.java
I have build APK, but detection "STOP"  no vibration.

```
Author:
```
pkulzc
```
Text:
```

This seems to be an android development question instead of model feature.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @Harshini-Gadige: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
jvishnuvardhan
```
Text:
```

As mentioned by @pkulzc, this looks like support question on android development to implement object detection. Please ask support questions in Stackoverflow community. Closing this issue due to lack of recent activity. Please open new ticket if you see similar issue. Thanks!

```

## 13090
Title:
```

        Session creation silently failing on iOS when loading a SavedModel
      
```
Author:
```
justinshapiro
```
Text:
```

Issue:
I am trying to integrate a TensorFlow solution into my iOS apps, but inference doesn't seem to work when I try to run simple graphs created in Python. In fact, the tensorflow_inception_graph from the examples is the only graph that seems to work with iOS inference. Every other inference attempt is met with the following error:

Invalid argument: Session was not created with a graph before Run()!

So what I'm finding is that on mobile if we try to run a canned neural network like the tensorflow_inception_graph, inference works perfectly but if we try to run any kind of custom model like 1 + 1 = 2, the graph won't run.
To demonstrate this, I used Python to write and export to a SavedModel the simplest graph I can think of: it just adds 1 + 1:
g = tf.Graph()
with g.as_default():
    output = tf.add(tf.constant(1), 1, name="output_tensor")

builder = tf.saved_model.builder.SavedModelBuilder('/path/to/export')
with tf.Session(graph=g) as sess:
    builder.add_meta_graph_and_variables(sess, tags=[])

builder.save()

Now to test that inference is actually possible, I reload the saved_model.pb into Python:
with tf.Session() as sess:
    tf.saved_model.loader.load(sess, [], '/path/to/export')

    print(sess.run('output_tensor:0')) // prints 2

Following in the footsteps of the simple example located at https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/ios, I go to perform inference on iOS using the static C++ library built using the makefile and the instructions provided at the link.
using namespace tensorflow;
using namespace std;
using namespace ::google::protobuf;
using namespace ::google::protobuf::io;

SessionOptions options;
Session* session_pointer = nullptr;
Status session_status = NewSession(options, &session_pointer);

cout << session_status.ToString() << endl; // prints OK

unique_ptr<Session> session(session_pointer);
    
GraphDef model_graph;
NSString* model_path = FilePathForResourceName(@"saved_model", @"pb");
PortableReadFileToProto([model_path UTF8String], &model_graph);
    
Status session_init = session->Create(model_graph);

cout << session_init.ToString() << endl; // prints OK, proves the graph was indeed created before run

vector<Tensor> outputs;
Status session_run = session->Run({}, {"output_tensor:0"}, {}, &outputs);

cout << session_run.ToString() << endl; // prints Invalid argument: Session was not created with a graph before Run()!

Troubleshooting:
I've tried rebuilding multiple times from 1.3.0 (latest, nightly), 1.2.1 and tried using the TensorFlow-experimental Pod. (I also tried using the TensorFlow-iOS pod, but it seems to be empty.)
There are (unanswered) Stack Overflow questions that refer to this issue occurring on both platforms:


Android: https://stackoverflow.com/questions/41252122/tensorflow-on-android-error-during-inference-invalid-argument-session-was-not


iOS: https://stackoverflow.com/questions/46201109/inference-error-with-tensorflow-c-on-ios-invalid-argument-session-was-not-c


On GitHub, there's been several issues related to this reported over the last year: #7088, #5553, #3480, #6806, and #3352. None of the resolutions (if any) for these issues provide a concrete answer of how to get around this problem.
However, found in the comments of #3480 , @petewarden's post about using optimize_for_inference, quantize_graph, and convert_graphdef_memmapped_format on the model before running inference present a possible solution. So I ran those three commands and got the same error:

google.protobuf.message.DecodeError: Truncated message.

Since we can perform successful inference on the model in Python (as shown above), the possibility of the model being corrupt (as @petewarden suggested in #3002) is ruled out. Therefore, the above "Truncated Error" message may point to where the problem is on mobile: Unsuccessful parsing of general models stored in protobuf files.
Closing thoughts on issue:
The point is this: The error message "Invalid argument: Session was not created with a graph before Run()!" doesn't provide any information to me regarding what should be debugged in my implementation. Additionally, it appears to not even point to the source of the error as I have verified three things:

All arguments passed to the session and graph are valid (Invalid Argument)
Session was created with a graph before Run() and the Status was reported to be OK (Session was not created with a graph before Run()!)
The error is likely triggered due to unsuccessful parsing on mobile devices of custom models serialized in protobuf files

Library Versions:
TensorFlow Python version: ('v1.3.0-rc2-20-g0787eee', '1.3.0')
TensorFlow C++ version: 1.3.0, built using build_all_ios.sh. Also tried with version 1.2.1 and TensorFlow-experimental pod
System information:
== cat /etc/issue ===============================================
Darwin mbmagenic12 16.5.0 Darwin Kernel Version 16.5.0: Fri Mar  3 16:52:33 PST 2017; root:xnu-3789.51.2~3/RELEASE_X86_64 x86_64
Mac OS X 10.12.4

== are we in docker =============================================
No

== compiler =====================================================
Apple LLVM version 8.1.0 (clang-802.0.42)
Target: x86_64-apple-darwin16.5.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin

== uname -a =====================================================
Darwin mbmagenic12 16.5.0 Darwin Kernel Version 16.5.0: Fri Mar  3 16:52:33 PST 2017; root:xnu-3789.51.2~3/RELEASE_X86_64 x86_64

== check pips ===================================================
numpy (1.13.1)
protobuf (3.1.0.post1)
tensorflow (1.3.0)

== check for virtualenv =========================================
False

== tensorflow import ============================================
tf.VERSION = 1.3.0
tf.GIT_VERSION = v1.3.0-rc2-20-g0787eee
tf.COMPILER_VERSION = v1.3.0-rc2-20-g0787eee
Sanity check: array([1], dtype=int32)

== env ==========================================================
LD_LIBRARY_PATH is unset
DYLD_LIBRARY_PATH is unset

== nvidia-smi ===================================================
./tf.sh: line 105: nvidia-smi: command not found

== cuda libs  ===================================================


```
Author:
```
mrry
```
Text:
```

I think the problem is that you're trying to load a file in the SavedModel format into a GraphDef protobuf message, and this is silently failing. While a SavedModel may contain one or more GraphDef messages, they are not equivalent.

Based on a quick look at the DirectSession::Create() code, the behavior you're seeing could be explained if model_graph were empty after this line:
PortableReadFileToProto([model_path UTF8String], &model_graph);
Can you try the following two things?

Can you check whether or not model_graph contains any nodes after you read the file? Printing model_graph.node_size() and checking whether it is greater than 0 should suffice.
From the code it looks like PortableReadFileToProto() returns a bool to indicate success or failure. Can you check its value?


```
Author:
```
justinshapiro
```
Text:
```

Yes, it does look like the session creation is silently failing. I modified the code as follows:
GraphDef model_graph;
NSString* model_path = FilePathForResourceName(@"saved_model", @"pb");
bool success = PortableReadFileToProto([model_path UTF8String], &model_graph);
    
cout << "PortableReadFileToProto bool: " << success << endl;
    
cout << "Number of nodes in model_graph: " << model_graph.node_size() << endl;
    
Status session_init = session->Create(model_graph);
    
cout << "Session creation Status: " << session_init.ToString() << endl;

This prints:
PortableReadFileToProto bool: 0
Number of nodes in model_graph: 0
Session creation Status: OK

This indicates certain failure to parse the protobuf file, but session creation is being reported as succeeded.
Is there a C++/iOS equivalent to tf.saved_model.loader.load?

```
Author:
```
mrry
```
Text:
```

It's valid to create a session with an empty graph, because you can subsequently call Extend() on it.
There's a C API for loading a session from a SavedModel, called TF_LoadSessionFromSavedModel(). Note that the C API's TF_Session is slightly different from the C++ API's tensorflow::Session, but they support the same operations. To use the C API, you'd need to modify your Session::Run() call to use TF_SessionRun() instead. Alternatively, the implementatoin of TF_LoadSessionFromSavedModel() is fairly simple, and you might be able to make the same sequence of calls against the C++ Session API.

```

## 7684
Title:
```

        embedding variable in ptb_word_lm.py
      
```
Author:
```
sharod
```
Text:
```

In ptb_word_lm.py I see that for word2vec vectors we are doing:
embedding = tf.get_variable(
"embedding", [vocab_size, size], dtype=data_type())
inputs = tf.nn.embedding_lookup(embedding, input_.input_data)
but where is the variable embedding created? Is it random or is it pretrained?

```
Author:
```
krayush07
```
Text:
```

Hi @sharod
tf.get_variable() creates the 'embedding' variable and initializes it using a random initializer during training time as var scope for training is set to 'None'.
So, during training the word embedding is initialized and further trained since 'trainable' parameter is set to True. While during, validation or testing, the trained embeddings are retrieved as variable reuse is set to True.
Also, please use Stackoverflow for these kind of questions.

```

## 18980
Title:
```

        error when comiling Tensorflow 1.8
      
```
Author:
```
kerolos
```
Text:
```

System information

**Have I written custom code (as opposed to using a stock example script provided in TensorFlow) N/A:
**OS Platform and Distribution:Linux Debian 9.1:
**TensorFlow installed from (source or binary) bazel:
**TensorFlow version (use command below) v1.8.0:
**Python version 3.7:
**Bazel version (if compiling from source)0.11:
**GCC/Compiler version (if compiling from source) 6.3 and 4.9:
**CUDA/cuDNN version 7.1:
**GPU model and memory GTX 1080 TI, 11GB, 48GB:
**Exact command to reproduce: gcc:

Describe the problem
I could not able to install Tensorflow V1.8.0 on my machine. I used different gcc and g++ versions 4.9 and 6.1 in Debian 9. Furthermore, I got the same errors.
Error:
ERROR: /home/pm/local/cpp/TENSOR_FLOW_180/tensorflow/tensorflow/core/kernels/BUILD:1864:1: output 'tensorflow/core/kernels/_objs/eye_functor_gpu/tensorflow/core/kernels/eye_functor_gpu.cu.pic.o' was not created
ERROR: /home/pm/local/cpp/TENSOR_FLOW_180/tensorflow/tensorflow/core/kernels/BUILD:1864:1: not all outputs were created or valid
Target //tensorflow:libtensorflow_cc.so failed to build
Use --verbose_failures to see the command lines of failed build steps.
INFO: Elapsed time: 66.847s, Critical Path: 57.74s
FAILED: Build did NOT complete successfully

```
Author:
```
Frederick888
```
Text:
```

Same error here. Tried different versions of Bazel (0.12.0/0.11.1) and GCC (7.3.1/6.4.1) but the issue persisted.
I was building TF against CUDA 9.1, CuDNN 7.2 and NCCL 2.1.15.
Perhaps related to #18522?
Edit: Btw, Arch already has the _BITS_FLOATN_H patch in their official repo.

```
Author:
```
achalshah20
```
Text:
```

I am also facing the same issue. I am using similar software versions as @Frederick888

```
Author:
```
karmel
```
Text:
```

@annarev Any ideas here?

```
Author:
```
annarev
```
Text:
```

@Frederick888 can you try an earlier version of gcc? gcc 6.4 and later are not listed in compatibility table for cuda 9.1: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements.

```
Author:
```
gunan
```
Text:
```

The error messages you copied are helpful, but does not contain the actual failure message.
Could you copy your full terminal output to pastebin and share here?
Also, as @annarev stated CUDA does not seem to support GCC 6.4. As we are building on top of CUDA, there is not much we can do until cuda fully supports the gcc version.

```
Author:
```
Frederick888
```
Text:
```

Tried GCC 5.5.0 and failed with
INFO: From Compiling tensorflow/core/kernels/adjust_saturation_op_gpu.cu.cc:
/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9220): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9231): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9244): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9255): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9268): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9279): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9292): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9303): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9316): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9327): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9340): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9352): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9365): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9376): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9389): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9401): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9410): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9419): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9428): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9437): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9445): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9454): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9463): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9472): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9481): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9490): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9499): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9508): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9517): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9526): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9535): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512fintrin.h(9544): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(55): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(63): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(73): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(81): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(91): error: argument of type "void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(100): error: argument of type "void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(109): error: argument of type "void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(117): error: argument of type "void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(127): error: argument of type "void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(136): error: argument of type "void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(145): error: argument of type "void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512pfintrin.h(153): error: argument of type "void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10799): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10811): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10823): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10835): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10847): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10859): error: argument of type "const void *" is incompatible with parameter of type "const float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10871): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10883): error: argument of type "const void *" is incompatible with parameter of type "const double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10895): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10907): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10919): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10931): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10943): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10955): error: argument of type "const void *" is incompatible with parameter of type "const int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10967): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10979): error: argument of type "const void *" is incompatible with parameter of type "const long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(10989): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11000): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11009): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11020): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11029): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11040): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11049): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11060): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11069): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11080): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11089): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11100): error: argument of type "void *" is incompatible with parameter of type "float *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11109): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11120): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11129): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11140): error: argument of type "void *" is incompatible with parameter of type "double *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11149): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11160): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11169): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11180): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11189): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11200): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11209): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11220): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11229): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11240): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11249): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11260): error: argument of type "void *" is incompatible with parameter of type "int *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11269): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11280): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11289): error: argument of type "void *" is incompatible with parameter of type "long long *"

/usr/lib/gcc/x86_64-pc-linux-gnu/5.5.0/include/avx512vlintrin.h(11300): error: argument of type "void *" is incompatible with parameter of type "long long *"

92 errors detected in the compilation of "/tmp/tmpxft_00005ce1_00000000-6_adjust_saturation_op_gpu.cu.cpp1.ii".
ERROR: /home/frederick/.virtualenvs/pylab/tensorflow/tensorflow/core/kernels/BUILD:2091:1: output 'tensorflow/core/kernels/_objs/adjust_saturation_op_gpu/tensorflow/core/kernels/adjust_saturation_op_gpu.cu.o' was not created
ERROR: /home/frederick/.virtualenvs/pylab/tensorflow/tensorflow/core/kernels/BUILD:2091:1: not all outputs were created or valid
Target //tensorflow/tools/pip_package:build_pip_package failed to build
Use --verbose_failures to see the command lines of failed build steps.
INFO: Elapsed time: 472.571s, Critical Path: 42.11s
FAILED: Build did NOT complete successfully

...should I get a GCC copy of exactly 6.3.0?

```
Author:
```
gunan
```
Text:
```

You are trying to build with avx512 support I think.
That is still not officially supported.

```
Author:
```
emerali
```
Text:
```

building with avx512 not being officially supported is a bit weird given that it's done automatically if you use the -march=native configuration option woops, just realized that the -march=native option is passed directly to gcc as opposed to being something that bazel processes itself
i get the same error as @Frederick888 when I compile the r1.7 branch with GCC 5.5.0 (CUDA 9.1, cuDNN 7.1, Bazel 0.13.0) (I was also getting the same error on r1.8)

```
Author:
```
Frederick888
```
Text:
```

@gunan You meant that I should disable it via any arguments?
FYI my build command was
bazel build --config=opt --config=cuda --copt=-march=native --copt=-msse4.1 --copt=-msse4.2 --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" //tensorflow/tools/pip_package:build_pip_package


```
Author:
```
dketterer
```
Text:
```

I have the same issue on mac os with LLVM 8.1.0, XCode 8.3.3, CUDA 9.0 and cuDNN 7.0

```
Author:
```
gunan
```
Text:
```

if you add --config=opt on a machine that has AVX512 instruction set, you will still get the error.
So I recommend:
bazel build --config=cuda --copt=-msse4.1 --copt=-msse4.2 --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" //tensorflow/tools/pip_package:build_pip_package


```
Author:
```
Frederick888
```
Text:
```

@gunan Same error with this build command :(

```
Author:
```
emerali
```
Text:
```

i managed to get it to build with gcc-4.8, and using the build command:
bazel build --config=cuda --verbose_failures //tensorflow/tools/pip_package:build_pip_package

unfortunately, this doesn't perform any additional compiler optimizations :(
UPDATE: ok so i managed to get it to build (under gcc-4.8) with --config=opt as well (using the default -march=native configuration option)
for the record, i'm using bazel 0.12.0, cuDNN 7.1, CUDA 9.1
not sure if this fixes OP's original issue, but it does fix the avx512fintrin.h issue

```
Author:
```
Frederick888
```
Text:
```

@emerali Thanks for the info! I also successfully compiled with the following setup:
Bazel          0.13.0
CUDA           9.1.85.3
cuDNN          7.1.2
NCCL           2.1.15
ComputeCpp-CE  0.7.0
GCC            4.9.4

bazel build --config=opt --config=cuda --copt=-march=native --copt=-msse4.1 --copt=-msse4.2 --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" //tensorflow/tools/pip_package:build_pip_package


```
Author:
```
Mukundan314
```
Text:
```

I was able to sucessfully compile with:
Bazel      0.13.0
CUDA       9.1.85.3
cuDNN      7.1.3
NCCL       2.1.15
GCC        5.4 (5.5 did not work)

./configure
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package 


```
Author:
```
tensorflowbutler
```
Text:
```

It has been 16 days with no activity and the awaiting response label was assigned. Is this still an issue?

```

## 2286
Title:
```

        Why resize_image_with_crop_or_pad require fully defined image?
      
```
Author:
```
ziky90
```
Text:
```

I would like to ask, why tensorflow.image.resize_image_with_crop_or_pad require fully defined image? Wouldn't it be better to have some function that is more general and that can handle dynamically created tensor?
I am currently playing with this function and I would like to use it for not fully defined Tensors.
Is there some plan to implement some more complex crop_tensor function that would work with dynamic tensors? And that would possibly be able to handle #2284

```
Author:
```
girving
```
Text:
```

I'm going to merge this thread into the extremely related #1029.  We'd be happy to accept PRs for either one.

```

# Pull
## 9510
Title:
```

        Fix Bazel CI / TensorFlow project
      
```
Author:
```
laszlocsomor
```
Text:
```

See bazelbuild/bazel#2892

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
martinwicke
```
Text:
```

Jenkins, test this please.

```
Author:
```
vrv
```
Text:
```

Unfortunately there is a merge conflict, can you try resolving the conflict?

```
Author:
```
laszlocsomor
```
Text:
```

@vrv : Done, PTAL
@martinwicke : FYi @meteorcloudy is on vacation, that's why I worked on this bug in the first place

```
Author:
```
vrv
```
Text:
```

@tensorflow-jenkins test this please

```

## 3398
Title:
```

        Added debugging information for Pi errors
      
```
Author:
```
petewarden
```
Text:
```


No description provided.


```

## 27359
Title:
```

        [INTEL MKL] Revert changes in mkl_concat_op. 
      
```
Author:
```
LakshayT
```
Text:
```

Temporarily reverting changes to workaround the squeeze op failure in SSD-Mobilenet.

```
Author:
```
penpornk
```
Text:
```

Thank you for your PR!

```

## 6051
Title:
```

        Branch 140903864
      
```
Author:
```
benoitsteiner
```
Text:
```


No description provided.


```
Author:
```
gunan
```
Text:
```

Windows failure looks legit.
@mrry It looks like some cuda stuff is leaking into non-cuda build?

```
Author:
```
mrry
```
Text:
```

Apparently yes. I don't recognize the symbols CudaRoot and LibdeviceRoot… perhaps they're new and whatever CL added them will make it clear what's wrong. (I'm not sure why this wouldn't fail to link on Linux CMake CPU as well, but maybe MSVC is more strict about unused symbols?)

```
Author:
```
mrry
```
Text:
```

Maybe this one?
benoitsteiner@e1f44d8

```
Author:
```
mrry
```
Text:
```

It'd probably be possible to fix this up by moving this file https://github.com/benoitsteiner/tensorflow/blob/e1f44d854e9e6db6ce1f7c70b81d0fef03e4a932/tensorflow/core/platform/posix/cuda_libdevice_path.cc to ../default (and modifying the necessary paths in the build config).

```
Author:
```
benoitsteiner
```
Text:
```

I've fixed the CudaRoot and LibdeviceRoot compilation errors on windows.

```
Author:
```
gunan
```
Text:
```

Jenkins, test this please.

```
Author:
```
gunan
```
Text:
```

@martinwicke I see experiment_test failures here.
Maybe this PR does not contain the rollback?

```
Author:
```
martinwicke
```
Text:
```

Not included. Was waiting for LGTMs -- it's being submitted now.

```
Author:
```
benoitsteiner
```
Text:
```

Andrew will push the changes

```
Author:
```
yorkie
```
Text:
```

Hi @benoitsteiner Could you just explain a bit why we need this parameter, if the abort with exit_without_error=true, the user actually should use the exit op?

```

## 17005
Title:
```

        Fix cmake for MacOS
      
```
Author:
```
tedhtchang
```
Text:
```

This change address cmake build issues for MacOS.

```
Author:
```
tedhtchang
```
Text:
```

Built on:
macOS v10.13.2
gcc version
Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 9.0.0 (clang-900.0.39.2)
Target: x86_64-apple-darwin17.3.0
Python 2.7.10
Command:
mkdir ~/tensorflow/tensorflow/contrib/cmake/build
cd ~/tensorflow/tensorflow/contrib/cmake/build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j8 tf_python_build_pip_package
pip install tf_python/dist/tensorflow-1.6.0rc0-cp27-cp27m-macosx_10_13_intel.whl
Python
Python 2.7.10 (default, Jul 15 2017, 17:16:57)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
Hello, TensorFlow!

```
Author:
```
yifeif
```
Text:
```

Thanks for the PR @tedhtchang. Could you add some explanation on what was causing the macOS cmake to fail and how does this PR fix the issue? Thanks!

```
Author:
```
tedhtchang
```
Text:
```

@yifeif I added detailed explanation for each change and also updated the gemmlowp_URL.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @yifeif: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
yifeif
```
Text:
```

Sorry for the delay and thanks for adding the comments @tedhtchang.

```
Author:
```
jhseu
```
Text:
```

Mind looking at the conflicts?

```
Author:
```
tedhtchang
```
Text:
```

@jhseu Sure I will resolve the conflict.

```
Author:
```
tensorflowbutler
```
Text:
```

Nagging Assignee @yifeif: It has been 14 days with no activity and this issue has an assignee. Please update the label and/or status accordingly.

```
Author:
```
tedhtchang
```
Text:
```

Windows doesn't build with newer version of gemmlowp library. I will take a look this failure.
If anyone wants see the error,  here are the messages:
INFO: Build completed, 1 test FAILED, 6 total actions
1564
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\internal../internal/platform.h(57): error C3861: '_aligned_malloc': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_matmul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1565
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\internal../internal/platform.h(60): error C3861: '_aligned_free': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_matmul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1566
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantize_down_and_shrink_range.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1567
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantize_down_and_shrink_range.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1568
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_activation_ops.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1569
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_activation_ops.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1570
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_add_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1571
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_add_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1572
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantize_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1573
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantize_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1574
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_bias_add_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1575
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_bias_add_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1576
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_matmul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1577
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_matmul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1578
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_conv_ops.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1579
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_conv_ops.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1580
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_mul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1581
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\quantized_mul_op.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1582
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C2065: '_SC_NPROCESSORS_ONLN': undeclared identifier (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\requantize.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1583
t:\src\github\tensorflow\cmake_build\gemmlowp\src\gemmlowp\meta\multi_thread_common.h(26): error C3861: 'sysconf': identifier not found (compiling source file T:\src\github\tensorflow\tensorflow\core\kernels\requantize.cc) [T:\src\github\tensorflow\cmake_build\tf_core_kernels.vcxproj]
1584
1585
423 Warning(s)
1586
24 Error(s)
1587

```
Author:
```
tedhtchang
```
Text:
```

@yifeif looks like gemmlow hash was updated by other PR recently. Could you start a Windows CMake CI test?

```
Author:
```
tedhtchang
```
Text:
```

@yifeif Failed //tensorflow/python/keras:cudnn_recurrent_test  but I don't think it's related to my change.

```

## 15787
Title:
```

        order quantized table by value for ease of reading
      
```
Author:
```
Atlas7
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
caisq
```
Text:
```

Closing duplicate PR in favor of #15786.

```

