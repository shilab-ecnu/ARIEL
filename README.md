# ARIEL: full Title

## Introduction
We develop a fast, omics-driven sample integration tool called ARIEL, which enables effortless landmark detection, spatial alignment and information transfer for multi-sample spatial transcriptomic data. ARIEL can be applied in diverse situation, including cross-individual, cross-platform, cross-resolution, cross-omics, and cross-disease scenarios. The main program of ARIEL can be summarized in the figure:

![Outline](/docs/source/_static/ARIEL_hippo12.png)

## Installation
We developed the ARIEL package based on Python 3.9.
ARIEL now is available on PyPI. To install it, run this command in the terminal:

`pip install ariel-srt`

The full package dependencies of ARIEL can be found in docs/requirements.txt, and the code is available at: https://github.com/shilab-ecnu/ARIEL-SRT.

## Usage
We provide four examples to demonstrate the application of ARIEL.

For data preprocessing, We first normalizes the expression for spots, then obtain embeddings using Profast or PCA to achieve data dimensionality reduction and eliminate potential batch effects. Specifically, when the samples are sourced from different slices, Profast is employed to eliminate batch effects(check data_processing/across_omics, data_processing/DLPFC, data_processing/hippo and the Visium dataset processing in data processing/hepatic lobule for details); while PCA is used when the samples are sourced from the same slices(check data_processing/hepatic lobule/Cosmx preprocessing for details).

Due to file size restrictions at GitHub, we cannot upload datasets associated with the demos. You can download the datasets that used in the paper in: https://figshare.com/articles/dataset/ARIEL-data/30425062. 
The detailed analysis procedures and results with jupyter notebook presented in this paper are available on the Read the Docs tutorial website: https://ariel-document.readthedocs.io/.


### DLPFC(Alignment)
In this Demo, we demonstrate the automatically generated landmarks by ARIEL under varying landmark quantities and their corresponding alignment results. Additionally, we apply spatial transformations such as rotation and mirroring to the slices to showcase the stability of the ARIEL.

### Hippocampus
In this Demo, we use a Visium slice as the reference and integrate two Slide-SeqV2 slices with it via ARIEL.

Specifically, we use ARIEL to identify landmarks between two Slide-SeqV2 samples and the reference sample, and perform spatial alignment using these landmarks. We then employ Gaussian processes to transfer the expression information from Slide-SeqV2 sample to the reference. 

Based on this approach, we achieve multi-sample information integration and generate several meaningful outputs. For instance, we constructe spatial gene expression maps based on the average gene information in the reference across the three samples, reflecting the common spatial expression characteristics of genes shared by all samples. Additionally, we achieve favorable spot clustering results using the averaged spatial expression data.

### Brain
In this Demo, we integrate two adjacent brain slices from RIBOmap and STARmap technological platforms using ARIEL. 

We use the RIBOmap sample as the reference and perform landmark identification, spatial alignment, and information transfer between the two slices through ARIEL. We use the transferred gene (information from the STARmap sample) to predict the protein (information from the RIBOmap sample). Compared to the baseline using single information source, incorporating gene information with ARIEL improves the accuracy of protein prediction for both randomly missing situation and regionally missing situation.

### Hepatic lobule
In this Demo, we first integrate information from 10 Cosmx hepatic lobules to create landmark library and a spatial gene expression atlas of the lobules. We then introduce two Visium liver slices with different health states and use ARIEL to assist in lobule localization and analysis. By performing correlation analysis with the Cosmx atlas, we identify genes potentially associated with fatty liver disease.


## Reference

## Development