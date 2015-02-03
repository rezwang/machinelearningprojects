Here is a list of my machine learning experience in business, healthcare, hypersecurity, visualization, documentation (wikipedia), ... etc (using Python and scikit packege) with supervised, unsupervised and semi-supervised learning problems using SVM, clustering, regression, bayes, .....

*- Loading datasets
a) Pen-Based Recognition of Handwritten Digits Data Set: A digit database by collecting 250 samples from 44 writers. The samples written by 30 writers are used for training, cross-validation and writer dependent testing, and the digits written by the other 14 are used for writer independent testing 
b) The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by Sir Ronald Fisher (1936) as an example of discriminant analysis.

################### Support Vector Machine #####
*- plot_digits_classification: Recognizes images of hand-written digits from a dataset of 1797 8x8 images (1.a) (Suppervised Vector Machine, SVM).
*- model_persistance: saves the model (SVM and pickle)
*- plot_randomly_generated_classification_dataset: Plot several randomly generated 2D classification datasets
*- plot_iris_dataset: 3D plot of trainign data sets consists 50 samples of 3 different types of irises

################### Decision Tree ########
*- plot_decisiontree_regression: Fit 1D regression with decision tree and predict and plot the outcomes (Desicion tree algorithm, 1D regression)
*- plot_decisiontree_regressor_multioutput: multi-output regression with decision tree (Decision tree, multi output, regression)
*- plot_decision_surface_of_tree: Plots the decision surface of a decision tree trained on pairs of features of the iris dataset. the decision tree learns decision boundaries made of combinations of simple thresholding rules inferred from the training samples (Decision tree, classification)
*- plot_outofcore_classification: Reuter text document classification using HashingVectorizer, with output image. 
*- plot_prediction_latency: predicts latency of various scikit-learn estimators

################# Unsupervised Learning ##########
*- 3- newsgroups_text_classification: A dataset of 18000 newsgroups posts on 20 topics (unsupervised)
*- analyze_wikipedia_page_eigenvector: analyze the graph of links inside wikipedia articles to rank articles by relative importance according to this eigenvector centrality (Randomized SVM algorithm, power iteration method.
*- plot_color_quantization: Performs a pixel-wise Vector Quantization (VQ) of an image, 
reducing the number of colors from 96,615 unique colors to 64, while preserving the overall appearance quality (Unsupervised, Clustering, KMeans algorithm).
*- plot_stock_market: Extracts the stock market structure from variations in historical quotes. The quantity that we use is the daily variation in quote price: quotes that are linked tend to cofluctuate during a day (Unsupervised learning)
*- plot_entropy_modeling_geographic_distribution: Models the geographic distribution of two south american mammals given past observations and 14 environmental variables (OneClassSVM)
*- plot_model_complexity_influence: Demonstrating how model complexity influences both prediction accuracy and computational performance. Dataset is the Boston Housing dataset (resp. 20 Newsgroups) for regression (resp. classification).
*- topic_extraction_with_nmf: topic extraction in a corpus of 20 newsgroups dataset (Negative Matrix Factorization)
*- outlier_detection: Detecting outlier and understanding data structure; the first example illustrates how robust covariance estimation can help concentrating on a relevant cluster when another one exists. The second example shows the ability of the Minimum Covariance Determinant robust estimator of covariance to concentrate on the main mode of the data distribution
*- plot_ct_reconstruction: Reconstruction of an image from a set of parallel projections, acquired along different angles (Lasso and Ridge algorithms)
*- face_recognition: recognize 8 faces from 966 faces (unsupervised feature extraction, dimensionality reduction, using eigen face and SVM)

#################### Semi-supervised learning ################
*- plot_label_propagation_structure: Learning a complex internal structure to demonstrate “manifold learning” (semi-supervised)
*- plot_label_prpogation_vs_svm: Comparison for decision boundary generated on iris dataset between (Label Propagation and SVM).
*- plot_label_propogation_digit: training a Label Spreading model to classify handwritten digits with sets of very few labels (supervised)
*- plot_label_propogation_digit_active_learning: active learning technique to learn handwritten digits using label propagation (semi_supervised, propogation)

################## Generalized Linear Model, supervised #########
*- plotting logistic-regression classifiers decision boundaries on the iris dataset (supervides, logistic regression, classifier)
*- 2D plot of linear regression of dieabetes data set. he coefficients, the residual sum of squares and the variance score are also calculated (linear regression, supervised)