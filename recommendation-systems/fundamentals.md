1. Recommendation systems are techniques or systems that recommend or suggest a particular product, service, or entity. These systems can be categorized into a prediction problem or a ranking problem. 
    
    1. Prediction problem 
        - The goal is to predict the missing values in the sparse user-item matrix. If it is able to predict the missing values accurately, it will be able to give great recommendations. For example, if user i has not used item
        $j$, but our system predicts a very high rating (denoted by $i,j$), it is highly likely
        that $i$ will love $j$ should they discover it through the system.


    2. Ranking problem
        - The goal is to produce an ordered list of items (top-K) to provide to a given user. It is not about predicting how much the user will like each item but more about deciding which items should appear ahead of others. The system cares about the relative order, not predicted value.
        - Ranking metrics such as NDCG@K, MAP@K, Recall@K measure ordering quality.
        - Ranking is the real problem because users are not seeing predicted scores but rather a sorted list (of recommendations).
        - 	A perfect predictor is not required to produce a perfect ranking. Even inaccurate predictions can yield good rankings if relative order is correct.
   
    3. If we are able to predict missing values, we can extract the top values
        and display them as our results.

4.  Prediction accuracy ≠ recommendation quality. A model can predict ratings with low RMSE but produce terrible rankings.
    - The Netflix Prize (2006) challenged teams to beat Netflix’s movie-rating predictor by 10% RMSE. Teams spent years improving prediction accuracy, yet the winning algorithms never went into production because better RMSE didn’t necessarily improve actual user experience. 
        - One key lesson was that explicit ratings are sparse and don’t capture many signals that matter in practice
        - implicit feedback (plays, pauses, searches, dwell time) provides richer and more abundant data but reflects observing behavior rather than direct preference. 
        - Models must interpret implicit signals carefully (e.g., a skipped video could mean disinterest or lack of time). So, even though the contest optimized a rating-prediction metric, the real-world value at Netflix came from modeling implicit feedback and optimizing ranking or personalization experiences tied to engagement.

# Other
1. A tuple is an ordered, fixed-length collection of values. You create one with parentheses like ("movie", 4.5, True). Because it’s immutable, the items and length can’t change after creation. It’s handy for bundling related values together when you don’t need to modify the grouping—for example, returning multiple objects from a function as a single result.

