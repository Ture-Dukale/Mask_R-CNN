import argparse


def parse_args():
    """
    Parse command-line arguments to train and evaluate a multimodal network for activity recognition on MM-Fit.
    :return: Populated namespace.
    """
    parser = argparse.ArgumentParser(description='baseline Mask R-CNN')
    parser.add_argument('/kaggle/input/train-val-imgs/data', required=True,
                        metavar="/path/to/dataset/",
                        help='Directory of the dataset')
    parser.add_argument('--continue_train', type=str, required=False, default='None',
                        metavar="/path/to/latest/weights.h5", help="Path to lastest training weights .h5 file")
    parser.add_argument('/kaggle/working/Mask_R-CNN/mobile_mask_rcnn_coco.h5', required=False,
                        metavar='/path/to/pretrained/weight.h5', help="Path to trained weight")
    parser.add_argument('--image', required=False,
                        metavar='/path/to/testing/image/directory', help="Path to testing image directory")
    parser.add_argument('--video', required=False,
                        metavar='/path/to/testing/image/directory', help="Path to testing image directory")
    return parser.parse_args()
