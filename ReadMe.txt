Here is a list of my machine learning experience in business, healthcare, hypersecurity, visualization, documentation (wikipedia), ... etc (using Python and scikit packege) with supervised, unsupervised and semi-supervised learning problems using SVM, clustering, regression, bayes, .....

1- Loading datasets
a) Pen-Based Recognition of Handwritten Digits Data Set: A digit database by collecting 250 samples from 44 writers. The samples written by 30 writers are used for training, cross-validation and writer dependent testing, and the digits written by the other 14 are used for writer independent testing 
b) The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by Sir Ronald Fisher (1936) as an example of discriminant analysis.
################### Supervised Vector Machine Learning #####
2- plot_digits_classification: Recognizes images of hand-written digits from a dataset of 1797 8x8 images (1.a) (Suppervised Vector Machine, SVM).
3- newsgroups_text_classification: A dataset of 18000 newsgroups posts on 20 topics (unsupervised)
4- model_persistance: saves the model (SVM and pickle)
5- plot_randomly_generated_classification_dataset: Plot several randomly generated 2D classification datasets
6- plot_iris_dataset: 3D plot of trainign data sets consists 50 samples of 3 different types of irises
################### Decision Tree ########
7- plot_decisiontree_regression: Fit 1D regression with decision tree and predict and plot the outcomes (Desicion tree algorithm, 1D regression)
8- plot_decisiontree_regressor_multioutput: multi-output regression with decision tree (Decision tree, multi output, regression)
9- plot_decision_surface_of_tree: Plots the decision surface of a decision tree trained on pairs of features of the iris dataset. the decision tree learns decision boundaries made of combinations of simple thresholding rules inferred from the training samples (Decision tree, classification)
10- plot_outofcore_classification: Reuter text document classification using HashingVectorizer, with output image. 
11- plot_prediction_latency: predicts latency of various scikit-learn estimators

################# Unsupervised Learning ##########
12- analyze_wikipedia_page_eigenvector: analyze the graph of links inside wikipedia articles to rank articles by relative importance according to this eigenvector centrality (Randomized SVM algorithm, power iteration method.
13- plot_color_quantization: Performs a pixel-wise Vector Quantization (VQ) of an image, 
reducing the number of colors from 96,615 unique colors to 64, while preserving the overall appearance quality (Unsupervised, Clustering, KMeans algorithm).
14- plot_stock_market: Extracts the stock market structure from variations in historical quotes. The quantity that we use is the daily variation in quote price: quotes that are linked tend to cofluctuate during a day (Unsupervised learning)
15- plot_entropy_modeling_geographic_distribution: Models the geographic distribution of two south american mammals given past observations and 14 environmental variables (OneClassSVM)
16- plot_model_complexity_influence: Demonstrating how model complexity influences both prediction accuracy and computational performance. Dataset is the Boston Housing dataset (resp. 20 Newsgroups) for regression (resp. classification).
17- topic_extraction_with_nmf: topic extraction in a corpus of 20 newsgroups dataset (Negative Matrix Factorization)
18- outlier_detection: Detecting outlier and understanding data structure; the first example illustrates how robust covariance estimation can help concentrating on a relevant cluster when another one exists. The second example shows the ability of the Minimum Covariance Determinant robust estimator of covariance to concentrate on the main mode of the data distribution
19- plot_ct_reconstruction: Reconstruction of an image from a set of parallel projections, acquired along different angles (Lasso and Ridge algorithms)
20- face_recognition: recognize 8 faces from 966 faces (unsupervised feature extraction, dimensionality reduction, using eigen face and SVM)
#################### Semi-supervised learning ################
21- plot_label_propagation_structure: Learning a complex internal structure to demonstrate “manifold learning” (semi-supervised)
22- plot_label_prpogation_vs_svm: Comparison for decision boundary generated on iris dataset between (Label Propagation and SVM).
23- plot_label_propogation_digit: training a Label Spreading model to classify handwritten digits with sets of very few labels (supervised)
24- plot_label_propogation_digit_active_learning: active learning technique to learn handwritten digits using label propagation (semi_supervised, propogation). 
