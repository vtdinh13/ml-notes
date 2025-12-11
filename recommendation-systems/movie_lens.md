1. `value_counts(normalize=True)` normalizes by dividing each count by the total to get proportions that sum up to 1. It does not standardize so no mean subtraction or variance scaling.
    - Normalize when you need proportions or probabilities (e.g., how a category distributes within a sample).
    - `value_counts()` only counts; `normalize=True` converts counts to proportions. There’s no built-in parameter to standardize those values.
2. Standardization is important when a model’s behavior depends on feature scale. 
    - Standardize when you need zero-mean, unit-variance numeric features for distance-based models or gradient-based methods sensitive to feature scale. 
    - You generally skip standardization for one‑hot categorical features, tree‑based models that rely on splits, or when the scale itself carries meaning (e.g., counts you want the model to treat literally).
    - Typical cases:
        
        1. Gradient‑based models: Linear/logistic regression, neural nets, even some tree ensembles converge faster and avoid weight dominance when features sit on comparable scales (zero mean, unit variance). Otherwise learning rates must adapt per feature.
        2. Distance/similarity methods: k‑NN, k‑means, kernel methods, PCA/SVD. If one feature has a much larger variance, it swamps the distance metric and the model effectively ignores smaller‑scale signals. Standardizing ensures each numeric feature contributes proportionally.
        3. Regularization: L1/L2 penalties assume comparable feature scales. Without standardization, coefficients on large‑scale features get penalized more harshly.
        4. Projection/latent factor models: Matrix factorization, embedding learning, and PCA rely on variance structure; standardizing raw numeric side features (e.g., age, price) makes latent factors more stable.
        5. Online/streaming models: Keeps numeric features bounded, limiting gradient explosion or saturation as data distribution drifts.
3. When to center: subtract mean so values represent deviation from average. 
    - Typical cases:

        1. Linear models with interaction terms or polynomials: centering reduces multicollinearity between main and interaction effects, making coefficients more interpretable.
        2. PCA or any covariance-based method: subtracting the mean is required so the covariance captures variance around zero.
        3. Regularized models with intercepts: centering allows you to drop/interpret intercept separately, and it stabilizes optimization by keeping features around zero.
        4. Visualization/feature engineering: highlighting how far each observation sits from “typical” value without distorting units (e.g., residual plots, anomaly detection thresholds).
