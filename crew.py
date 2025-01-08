from crewai import Agent, Crew, Process, Task
from crewai_tools import PDFSearchTool, FirecrawlSearchTool
from pydantic import BaseModel, Field
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()

# --- Pydantic Schema ---

class ContentFormatInfo(BaseModel):
    Post_Title: Optional[str] = Field(..., description="Attractive topic or headline that grabs attention")
    Heading_with_valuable_hook: Optional[str] = Field(None, description="Sentence with a compelling hook (e.g., FREE, EASY, NEW, or something controversial)")
    Intrigue_Line: Optional[str] = Field(None, description="Line that builds curiosity and encourages the reader to click 'See More'")
    Content_Body: Optional[str] = Field(None, description="Main content of the post with valuable insights, stories, or updates")
    Call_to_Action_CTA: Optional[str] = Field(None, description="A strong call to action prompting engagement (e.g., comment, share, etc.)")
    Hashtags: Optional[str] = Field(None, description="Relevant hashtags to improve discoverability")
    Poll_or_Question: Optional[str] = Field(None, description="Engagement tool like a poll or question")
    Story_or_Insight: Optional[str] = Field(None, description="Personal story, insight, or anecdote for relatability")
    # Media_Type: Optional[str] = Field(None, description="Optional use of media like images, videos, or documents")
    # Visual_Appeal: Optional[str] = Field(None, description="Ensures the post is visually appealing with high-quality images or videos")

# --- Tools ---
pdf_search_tool = PDFSearchTool()
fire_crawl_search_tool = FirecrawlSearchTool()

# --- Agents ---
general_research_agent = Agent(
    role="General Research Agent",
    goal="Search the PDF and web to gather content for creating post on the required {topic} with help from the pdf file provided and populate the ContentFormatInfo model.",
    allow_delegation=False,
    backstory=(
    """
    The research agent is a highly skilled and resourceful individual, proficient in navigating both digital documents 
    and the web to gather valuable content. With a sharp eye for detail and an extensive understanding of how to extract 
    and validate relevant information, this agent ensures that no stone is left unturned. Whether it's combing through 
    documents, performing targeted web searches, or utilizing advanced tools, the research agent is committed to gathering 
    the precise data needed to create a compelling and informative LinkedIn post. Their expertise in content aggregation 
    ensures that all necessary details are accurate, relevant, and ready for the post-creation process.
    """
    ),
    verbose=True,
    tools=[pdf_search_tool, fire_crawl_search_tool],
)

linkedin_post_generator_agent = Agent(
    role="LinkedIn Post Generator Agent",
    goal="Craft an engaging LinkedIn post using the ContentFormatInfo model.",
    allow_delegation=False,
    backstory=(
        """
        The professional writer agent is a creative expert with a knack for transforming data into clear, concise, and engaging content. 
        They possess excellent writing skills and have a deep understanding of how to connect with the audience. The agent will use 
        their abilities to craft an engaging LinkedIn post based on the research agent's findings. They are adept at maintaining 
        professionalism while also ensuring the content resonates with the target audience.
        """
    ),

    verbose=True,
)

seo_agent = Agent(
    role="SEO Optimization Agent",
    goal="Optimize the LinkedIn post for SEO by incorporating relevant keywords, hashtags, and improving readability.",
    allow_delegation=False,
    backstory=(
    """
    The SEO agent is a meticulous and strategic thinker with an in-depth understanding of how search engines work. 
    They are always up-to-date with the latest SEO practices and algorithms, ensuring that every piece of content is optimized 
    for maximum discoverability. The SEO agent will ensure that the LinkedIn post includes keywords and structure that can help 
    it rank higher in search results and attract more attention.
    """
    ),

    verbose=True,
)

tone_style_optimizer_agent = Agent(
    role="Tone & Style Optimizer Agent",
    goal="Refine the LinkedIn post's tone and style to align with professional standards and audience expectations.",
    allow_delegation=False,
    backstory=(
    """
    The tone and style optimizer agent is a language expert, well-versed in adapting the tone of content to suit different 
    audiences and platforms. They understand how tone can influence the reader's perception and engagement. This agent will 
    carefully fine-tune the style and voice of the LinkedIn post, ensuring it aligns with the target audience's expectations 
    while maintaining a professional yet approachable tone.
    """
    ),

    verbose=True,
)

final_reviewer_agent = Agent(
    role="Final Reviewer Agent",
    goal=(
        "Review the LinkedIn post to ensure it conforms to the `ContentFormatInfo` schema, "
        "making sure all sections are complete, accurate, and adhere to the described format."
    ),
    allow_delegation=False,
    backstory=(
    """
    The final reviewer agent is a detail-oriented perfectionist who specializes in ensuring that content meets the highest 
    standards of quality. With an eagle eye for consistency and structure, this agent will review the entire LinkedIn post, 
    comparing it with the ContentFormatInfo schema to ensure all elements are properly filled out. They will confirm the post 
    is visually appealing, impactful, and aligned with all necessary guidelines before it is finalized for publishing.
    """
    ),

    verbose=True,
)

# --- Tasks ---
find_initial_information_task = Task(
    description="""Populate the `ContentFormatInfo` model with structured information extracted from the PDF file
    using pdf_search_tool with path as {pdf_path} and if info is good enough for post use only pdf search tool
    else if and only if info of pdf is useless for the required topic then go for web search
    on {topic} using fire_crawl_search_tool with page limit = 1.
    
    Try to use pdf only if possible 
    If you hit a rate limit, sleep for the specified time then retry again.
    """,
    expected_output="""
    Fill out the `ContentFormatInfo` model with as much information as possible. 
    Ensure all information is accurate and comes from the searches. 
    If any information is not found, leave it as None.
    """,

    tools=[pdf_search_tool, fire_crawl_search_tool],
    agent=general_research_agent,
    output_pydantic=ContentFormatInfo,
)

generate_linkedin_post_task = Task(
    description="Create a LinkedIn post using the populated `ContentFormatInfo` model.",
    expected_output="""
    Optimize the LinkedIn post's content by ensuring it follows SEO best practices. 
    Focus on keyword density, readability, and structure while maintaining a natural flow of language. 
    Ensure that the post includes relevant industry keywords without overstuffing. 
    The optimized content should be ready for publishing and maximize reach and engagement.
    """,

    agent=linkedin_post_generator_agent,
    
)

seo_optimization_task = Task(
    description="Enhance the LinkedIn post for SEO by adding keywords, hashtags, and improving readability.",
    expected_output="""
    Optimize the LinkedIn post's content by ensuring it follows SEO best practices. 
    Focus on keyword density, readability, and structure while maintaining a natural flow of language. 
    Ensure that the post includes relevant industry keywords without overstuffing. 
    The optimized content should be ready for publishing and maximize reach and engagement.
    """,

    agent=seo_agent,
)

tone_style_optimization_task = Task(
    description="Adjust the LinkedIn post's tone and style for professional standards and audience alignment.",
    agent=tone_style_optimizer_agent,
    expected_output="""
    Modify the LinkedIn post to enhance its tone and style, ensuring it aligns with the target audience’s expectations. 
    The post should be engaging, professional, and encourage action. Adjust the language to match the desired tone 
    (informative, casual, authoritative, etc.) while keeping the content aligned with the post's goal. 
    Ensure the post feels natural and resonates with readers.
    """

)

review_post_task = Task(
    description=(
        "Verify that the LinkedIn post adheres to the `ContentFormatInfo` schema, "
        "ensuring all sections are complete, consistent, and engaging."
    ),
    expected_output="""
    Review the final LinkedIn post and ensure it aligns with the `ContentFormatInfo` model. 
    Check that the post includes a compelling title, valuable hook, intrigue line, informative content body, 
    strong call to action, relevant hashtags, and any optional media or interactive elements. 
    Confirm that all sections of the post are complete and coherent, and make sure the formatting aligns with 
    best practices for LinkedIn posts. The post should be ready for publishing with all required details.
    """,

    agent=final_reviewer_agent,
    output_pydantic=ContentFormatInfo
)

# --- Crew ---
crew = Crew(
    agents=[
        general_research_agent,
        linkedin_post_generator_agent,
        seo_agent,
        tone_style_optimizer_agent,
        final_reviewer_agent,
    ],
    tasks=[
        find_initial_information_task,
        generate_linkedin_post_task,
        seo_optimization_task,
        tone_style_optimization_task,
        review_post_task,
    ],
    process=Process.sequential,
)

# --- Input ---
pdf_path= input("Enter the path to your PDF file: ")
topic = input("Enter the topic for the LinkedIn post: ")

# --- Execution ---
result = crew.kickoff(inputs={"pdf_path": pdf_path, "topic": topic})
print("Final LinkedIn Post:")
print(result)


# /home/divi/crewai-rag-deep-dive/linkedin_crew.py/genai-principles.pdf
