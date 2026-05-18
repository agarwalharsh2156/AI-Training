Starting with Langchain.
# 1 Refering this Youtube Vide
https://www.youtube.com/watch?v=8BV9TW490nQ

following the topics explained in the video.
- LangChain Overview & QuickStart (1:14 - 8:43):

Understanding what LangChain is and why it is used to build LLM applications by connecting them with external data and computation.
Environment setup for developing in a Colab notebook.

- Chains, Prompts & Loaders (8:43 - 15:00):

Introduction to Chains as sequences of components (pipelines).
Using Prompt Templates to structure input for models.
Utilizing Document Loaders (like the YouTube loader) to ingest external data into your chains.

- LangChain Expression Language (LCEL) & Runnables (15:00 - 23:22):

Understanding the Runnable Protocol (invoke, batch, stream).
Mastering core components: RunnableSequence, RunnableLambda (for custom functions), RunnablePassthrough, and RunnableParallel (for branching logic).

- Splitters & Retrievers (23:22 - 29:45):

Chunking data using Text Splitters (like RecursiveCharacterTextSplitter).
Setting up a Vector Store (using Redis) and creating a retriever to fetch relevant context based on queries.

- Building a RAG Chain (29:45 - 33:53):

Combining previous concepts to build a Retrieval Augmented Generation (RAG) chain that answers questions using your specific data as context.

- Tools & Toolkits (33:53 - 37:20):

Defining Tools as interfaces for models to interact with the world.
Binding tools to LLMs so they can search the web or execute specific tasks.

- Building Agents with Tool Access (37:20 - 41:27):

Transitioning from hardcoded chains to Agents that use reasoning to decide which tools to use and when.
Creating a flexible agent capable of searching and transcribing YouTube videos.