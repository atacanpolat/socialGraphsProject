# Explainer Notebook

## 0. Motivation

The dataset for the Naruto network analysis project consists of information related to character interactions, affiliations, and events within the Naruto anime series. It includes data on characters, their attributes and key points, and their relation to other characters, synopsis of each episode, summary of the arcs, and key plot points involving various characters.

The Naruto dataset was chosen due to its popularity and the complexity of its character universe, with over 1400 characters and 1000 episodes, and rich and shifting character interactions throughout the series. The Naruto universe is an ideal subject for network analysis.

Even though our analysis spans over a broader range of questions, our main problem of interest is whether it is possible to systematically find the interchanging importance of the characters and the temporal patterns that emerge throughout the episodes in the series by applying tools from network science.

## 1. Data Fetching and Preprocessing Choices for Naruto Network Analysis

The main data source for the Naruto network analysis project is the Naruto Wiki Fandom page. The data extraction process involves web scraping using Beautiful Soup to gather information about the characters, their attributes, relationships with other characters, affiliations with villages, and involvement in episodes and arcs. The code and detailed information about the fetching and preprocessing of each type of data can be found in the notebooks under the folder named "data_fetching."

1. **Web Scraping with Beautiful Soup:**
   
   Web scraping was employed to extract data from the Naruto Wiki Fandom page. Beautiful Soup is used for the parsing of the webpage's HTML structure.

2. **Characters:**
   
   The attributes of each character, such as name, role, abilities, and status, were extracted and organized. Furthermore, character's analysis on their respective wiki page was extracted for textual analysis. Cleaning involved handling missing or inconsistent information to ensure a uniform dataset. For more information, refer to [Character Data Fetching Notebook](./data_fetching/download_character_data.ipynb)

3. **Village Affiliations:**
   
   Information about the villages each character is affiliated with was gathered. Cleaning addressed discrepancies in village names, ensuring consistency in the dataset. For more information, please refer to [Village Data Fetching Notebook](./data_fetching/download_village_data.ipynb)

4. **Episodes and Arcs:**
   
   Data related to character involvement in episodes and arcs were collected. This involved extracting episode lists and the characters that participated in. Furthermore, a synopsis of each episode is collected for textual analysis. For more information, please refer to [Episode Data Fetching Notebook](./data_fetching/download_episode_data_updated.ipynb) and [Arc Data Fetching Notebook](./data_fetching/download_arc_data.ipynb)

## 2. Network Information & Statistics

### Episode Development Networks

We constructed individual networks for each episode in the season, where nodes represent characters that have appeared in the series up to that specific episode. An edge exists between two nodes if the characters have appeared together in an episode. The edge weights of the graphs indicate the number of co-occurrences of the mentioned characters up to the episode on which the network is built. These networks are cumulative, meaning that the network of episode 'n' corresponds to the characters' co-occurrence data from episode 1 up to episode 'n'. This approach allows us to track the development of the series and dynamic character interactions as the storyline progresses.

### Cumulative Network Statistics

- **Total Nodes:** 1448
- **Total Edges:** 21576

For more detailed network statistics, we encourage you to explore the [Episode Development Network Notebook](./network_analysis/episode_development_network.ipynb).

## 3. Tools, Theory, Analysis

### 3.1. Network Analysis

For our network analysis, we employed statistical methods such as the degree distribution of the networks throughout the episodes, centrality measures of important characters, and community analysis of the networks throughout the episodes. Furthermore, to have a clear overview of the most important characters in the series, we employ a separate analysis on the co-occurrence networks with a constraint of a minimum co-occurrence.

Detailed information about the statistical analysis of the cumulative character co-occurrence networks can be found in the following notebooks:

- Statistical analysis of the final cumulative network: [Episode Development Network Notebook](./network_analysis/episode_development_network.ipynb)

- Analysis of the temporal evolution of the series with a minimum co-occurrence threshold: [Filtered Episode Development Network Notebook](./network_analysis/filtered_episode_development_network.ipynb)

- For graph partitioning and community analysis: [Community Detection Notebook](./network_analysis/community_detection.ipynb)

### 3.2. Textual Analysis

The textual analysis was conducted on the episode and character descriptions. We used the NLTK package for text cleaning and preprocessing, and LabMT wordlist for calculating the sentiment scores of the episode and the characters. Word clouds for each season were also computed.

Detailed information about the sentiment analysis and word clouds can be found in the following notebook:

- Sentiment scores and analysis: [Sentiment Analysis Notebook](./text_analysis/Sentiment_analysis.ipynb)

- Word clouds: [Wordclouds Notebook](./text_analysis/wordclouds.ipynb)

## 4. Discussion

### Limitations

- **Edge Weight Subjectivity:**
  The assignment of edge weights based on character co-occurrences introduces a level of subjectivity. While we experimented with different levels of thresholds, and concluded that a threshold level of 100 delivered the clearest visibility, the choice of a threshold (e.g., 100) may impact the interpretation of character significance, and alternative threshold values could lead to different network structures. Striking a balance between inclusivity and focus is challenging and requires careful consideration.

- **Community Detection Sensitivity:**
  Community detection algorithms, while powerful, are sensitive to parameter settings. The Louvain algorithm employed in this analysis may produce different results with variations in resolution parameters, potentially influencing community assignments.

- **Attribute-Based Partitioning Challenges:**
  The manual partitioning of the network based on character attributes, such as village affiliation, introduces its own set of challenges. Ambiguities in character allegiance or the lack of observation of latent variables may affect the accuracy of the partitioning.

- **Sentiment Analysis Complexity:**
  The sentiment analysis captures the emotional tone of both the characters and the episodes. However, the inherent complexity of language and context limits the granularity of sentiment scores and their respective interpretation, both on the character level and but also on the episode level.

### Possible Future Work

- **Dynamic Edge Weight Thresholding:**
  Future research could explore dynamic edge weight thresholds that adapt to the evolving narrative of the series. This approach may provide a more nuanced understanding of character significance over different story arcs.

- **Algorithm Sensitivity Analysis:**
  Conducting a sensitivity analysis on community detection algorithms, including parameter variations, could enhance the robustness of partitioning results. Exploring alternative algorithms may provide additional insights into community structures. Furthermore, other advanced clustering algorithms on vector representations of the nodes and their respective attributes can be explored.

- **Attribute-Based Partitioning Refinement:**
  Improving the accuracy of attribute-based partitioning involves refining character attribute annotations and considering additional attributes such as character roles or power levels. This could lead to more accurate community assignments. With the help of statistical learning algorithms, the most important node attributes can be detected and explored.

- **Fine-Tuning Sentiment Analysis:**
  Developing a more sophisticated sentiment analysis model that considers context and character relationships may yield richer insights into the emotional dynamics of the series. This could involve natural language processing techniques beyond word clouds. Neural networks for sequential data or other statistical learning algorithms for NLP can be employed to predict more accurate sentiment results.

- **Incorporating Episode Scripts:**
  Incorporating a textual analysis of the actual scripts of each episode rather than their synopsis may deliver interesting insights about the character interactions and evolution of the series that are otherwise not detectable.
