{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Explainer Notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 0. Motivation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The dataset for the Naruto network analysis project consists of information related to character interactions, affiliations, and events within the Naruto anime series. It includes data on characters, their attributes and key points, and their relation to other characters, synopsis of each episode, summary of the arcs, and key plot points involving various characters.\n",
    "\n",
    "The Naruto dataset was chosen due to its popularity and the complexity of its character universe. with over 1400 characters and 1000 episodes, and rich and shifting character interactions throughout the series, Naruto universe is an ideal subject for network analysis.\n",
    "\n",
    "Even though our analysis spans over a broader range of questions, our main problem of interest is whether it is possible to systematically find the interchanging importance of the characters and the temporal patterns that emerge throughout the episodes in the series by applying tools from network science."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Data Fetching and Preprocessing Choices for Naruto Network Analysis\n",
    "\n",
    "The main data source for the Naruto network analysis project is the Naruto Wiki Fandom page. The data extraction process involves web scraping using Beautiful Soup to gather information about the characters, their attributes, relationships with other characters, affiliations with villages, and involvement in episodes and arcs. The code and detailed information about the fetching and preprocessing of each type of data can be found in the notebooks under the folder named \"data_fetching.\"\n",
    "\n",
    "1. **Web Scraping with Beautiful Soup:**\n",
    "\n",
    "    Web scraping was employed to extract data from the Naruto Wiki Fandom page. Beautiful Soup is used for the parsing of the webpage's HTML structure.\n",
    "\n",
    "2. **Characters:**\n",
    "\n",
    "    The attributes of each character, such as name, role, abilities, and status, were extracted and organized. Furthermore, character's analysis on their respective wiki page was extracted for textual analysis. Cleaning involved handling missing or inconsistent information to ensure a uniform dataset. For more information, refer to [Character Data Fetching Notebook](./data_fetching/download_character_data.ipynb)\n",
    "\n",
    "3. **Village Affiliations:**\n",
    "\n",
    "    Information about the villages each character is affiliated with was gathered. Cleaning addressed discrepancies in village names, ensuring consistency in the dataset. For more information, please refer to [Village Data Fetching Notebook](./data_fetching/download_village_data.ipynb)\n",
    "\n",
    "4. **Episodes and Arcs:**\n",
    "\n",
    "    Data related to character involvement in episodes and arcs were collected. This involved extracting episode lists and the haracters that participated in. Furthermore, synopsis of each episode is collected for textual analysis. For more information, please refer to [Episode Data Fetching Notebook](./data_fetching/download_episode_data_updated.ipynb) and [Arc Data Fetching Notebook](./data_fetching/download_arc_data.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Network information & Statistics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Episode Development Networks\n",
    "\n",
    "We constructed individual networks for each episode in the season, where nodes represent characters that have appeared in the series up to that specific episode. An edge exists between two nodes if the characters have appeared together in an episode. The edge weights of the graphs indicate the number of co-occurrences of the mentioned characters up to the episode on which the network is built. These networks are cumulative, meaning that the network of episode 'n' corresponds to the characters' co-occurrence data from episode 1 up to episode 'n'. This approach allows us to track the development of the series and dynamic character interactions as the storyline progresses.\n",
    "\n",
    "### Cumulative Network Statistics\n",
    "\n",
    "- **Total Nodes:** 1448\n",
    "- **Total Edges:** 21576\n",
    "\n",
    "For more detailed network statistics, we encourage you to explore the [Episode Development Network Notebook](./network_analysis/episode_development_network.ipynb).\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Tools, Theory, Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.1. Network Analysis\n",
    "\n",
    "For our network analysis, we employed statistical methods such as the degree distribution of the networks throughout the episodes, centrality measures of important characters, and community analysis of the networks throughout the episodes. Furthermore, to have a clear overview on the most important characters in the series, we employ a seperate analysis on the co-occurance networks with a constraint of a minimum co-occurance. \n",
    "\n",
    "Detailed information about the statistical analysis of the cumulative character co-occurance networks can be found in the following notebooks:\n",
    "\n",
    "- Statistical analysis of the final cumulative network: [Episode Development Network Notebook](./network_analysis/episode_development_network.ipynb)\n",
    "\n",
    "- Analysis of the temporal evolution of the series with minimum co-occurence threshold: [Filtered Episode Development Network Notebook](./network_analysis/filtered_episode_development_network.ipynb)\n",
    "\n",
    "- For the graph partitioning and community analysis: [Community Detection Notebook](./network_analysis/community_detection.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.2. Textual Analysis\n",
    "\n",
    "The textual analysis was conducted on the episode and character descriptions. We used the NLTK package for text cleaning and preproccesing, and LabMT wordlist for calculating the sentiment scores of the episode and the characters. Wordclouds for each season was also computed\n",
    "\n",
    "Detalied information about the sentiment analysis and wordclouds can be found in the following notebook:\n",
    "\n",
    "- Sentiment scores and analysis: [Sentiment Analysis Notebook](./text_analysis/Sentiment_analysis.ipynb)\n",
    "\n",
    "- Wordclouds: [Wordclouds Notebook](./text_analysis/wordclouds.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Discussion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Limitations\n",
    "\n",
    "- **Edge Weight Subjectivity:** The assignment of edge\n",
    "weights based on character co-occurrences introduces a\n",
    "level of subjectivity. While we experimented with different\n",
    "levels of thresholds, and concluded that a threshold level\n",
    "of 100 delivered the clearest visilibility of the, the choice\n",
    "of a threshold (e.g., 100) may impact the interpretation \n",
    "of character significance, and alternative threshold values\n",
    "could lead to different network structures. Striking a balance\n",
    "between inclusivity and focus is challenging and requires\n",
    "careful consideration\n",
    "\n",
    "- **Community Detection Sensitivity:** Community detection algorithms, while powerful, are sensitive to parameter\n",
    "settings. The Louvain algorithm employed in this analysis\n",
    "may produce different results with variations in resolution\n",
    "parameters, potentially influencing community assignments.\n",
    "\n",
    "- **Attribute-Based Partitioning Challenges:** The manual partitioning of the network based on character attributes,\n",
    "such as village affiliation, introduces its own set of challenges.\n",
    "Ambiguities in character allegiance or the lack of observation\n",
    "of latent variables may affect the accuracy of the partitioning.\n",
    "\n",
    "- **Sentiment Analysis Complexity:** The sentiment analysis captures the emotional tone of both the characters and\n",
    "the episodes. However, the inherent complexity of language\n",
    "and context limits the granularity of sentiment scores and\n",
    "their respective interpretation, both on the character level,\n",
    "and but also on the episode level.\n",
    "\n",
    "### Possible Future Work\n",
    "\n",
    "- **Dynamic Edge Weight Thresholding:** Future research\n",
    "could explore dynamic edge weight thresholds that adapt\n",
    "to the evolving narrative of the series. This approach\n",
    "may provide a more nuanced understanding of character\n",
    "significance over different story arcs.\n",
    "\n",
    "- **Algorithm Sensitivity Analysis:** Conducting a sensitivity analysis on community detection algorithms, including parameter variations, could enhance the robustness\n",
    "of partitioning results. Exploring alternative algorithms\n",
    "may provide additional insights into community structures.\n",
    "Furthermore, other advanced clustering algorithms on vector\n",
    "representations of the nodes and their respective attributes\n",
    "can be explored.\n",
    "\n",
    "- **Attribute-Based Partitioning Refinement:** Improving the accuracy of attribute-based partitioning involves refining character attribute annotations and considering additional\n",
    "attributes such as character roles or power levels. This could\n",
    "lead to more accurate community assignments. With help\n",
    "of statistical learning algorithms, the most important node\n",
    "attributes can be detected and explored.\n",
    "\n",
    "- **Fine-Tuning Sentiment Analysis:** Developing a more\n",
    "sophisticated sentiment analysis model that considers context\n",
    "and character relationships may yield richer insights into the\n",
    "emotional dynamics of the series. This could involve natural\n",
    "language processing techniques beyond word clouds. Neural\n",
    "networks for sequential data or other statistical learning\n",
    "algorithms for NLP can be employed to predict more accurate\n",
    "sentiment results.\n",
    "\n",
    "- **Incorporating Episode Scripts:** Incorporating a textual analysis of the actual scripts of each episode rather\n",
    "than their synopsis may deliver interesting insights about the\n",
    "character interactions and evolution of the series that are\n",
    "otherwise not detectable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Contributions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The assignment can be divided into three primary groups, namely 'Data Fetching', 'Network Analysis', and 'Text Analysis'. All group members contributed to everything, but the overall distribution of the responsibilities is as follows:\n",
    "\n",
    "- **Data Fetching:** Lukas (s194642) & Ata (s231859)\n",
    "\n",
    "- **Network Analysis:** Mona (s204226) & Ata (s231859)\n",
    "\n",
    "- **Text Analysis:** Lukas (s194642)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
