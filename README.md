# LinkedIn Post Creator

This repository contains a modular and automated system for generating professional LinkedIn posts from a given PDF document and topic. The system leverages Crew AI for orchestration and includes agents with specific roles and tasks to ensure the generated post is well-researched, SEO-optimized, and tailored to a professional audience.

---

## Features
- **PDF and Topic-Based Content Creation**: Input a PDF file and a topic, and the system generates a LinkedIn post based on the content.
- **Multi-Agent Collaboration**: Dedicated agents for research, writing, SEO optimization, tone and style refinement, and final review.
- **Dynamic Pydantic Models**: Tasks ensure output conforms to structured schemas for consistency and quality.
- **Modular Design**: Easily extendable agents and tasks for additional functionality.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/divyansh-tripathi7/linkedin-post-creator.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd linkedin-post-creator
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   OTHER_ENV_VARIABLES=values
   ```

---

## Usage

### Step 1: Provide Inputs

Run the script and provide the required inputs:
- Path to the PDF file.
- Topic for the LinkedIn post.

```bash
python main.py
```

You will be prompted to enter:
- `Enter the path to your PDF file:`
- `Enter the topic for the LinkedIn post:`

### Step 2: Output
The system will generate a LinkedIn post that includes:
- A catchy headline.
- Intriguing opening lines.
- The main body of the post.
- A clear call to action (CTA).
- Relevant hashtags.

The post will be displayed in the terminal and can be saved for further use.

---

## System Architecture

### Agents
1. **Research Agent**: Extracts relevant information from the PDF and additional online sources.
2. **Professional Writer Agent**: Drafts a coherent and professional post using the research agent's findings.
3. **SEO Optimization Agent**: Enhances the post for discoverability with targeted keywords and hashtags.
4. **Tone and Style Optimization Agent**: Ensures the post aligns with a professional tone and style.
5. **Final Reviewer Agent**: Verifies the final post meets the required schema (`ContentFormatInfo`).

### Tasks
1. **Find Initial Information**: Extracts key details from the PDF.
2. **Generate Post Content**: Drafts the initial version of the LinkedIn post.
3. **Optimize for SEO**: Improves the post's search engine optimization.
4. **Refine Tone and Style**: Ensures the post is polished and professional.
5. **Review Final Post**: Validates the output against the `ContentFormatInfo` schema.

---

## Key Schemas

### `ContentFormatInfo`
A Pydantic schema for the LinkedIn post structure:
```python
class ContentFormatInfo(BaseModel):
    Post Title: Optional[str]
    Heading with valuable hook: Optional[str]
    Intrigue Line: Optional[str]
    Content Body: Optional[str]
    Call to Action (CTA): Optional[str]
    Hashtags: Optional[str]
    Media Type: Optional[str]
    Poll or Question (optional): Optional[str]
    Story or Insight: Optional[str]
    Visual Appeal: Optional[str]
```

---

## Example

Input:
- PDF File: `example.pdf`
- Topic: "Emerging Trends in AI"

Output:
```
Post Title: "5 Trends in AI That Are Changing the World"
Heading with valuable hook: "**FREE insights** into the latest AI advancements!"
Intrigue Line: "Want to stay ahead of the curve? Here are 5 trends you need to know."
Content Body: "AI is evolving faster than ever. From generative models to explainable AI, here are the key advancements..."
Call to Action (CTA): "What do you think? Share your insights in the comments below!"
Hashtags: "#AI #Technology #Innovation"
```

---

## Contributing

We welcome contributions! If you have ideas for improving the system, feel free to submit a pull request or open an issue.

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or support, please contact:
- **Your Name**
- Email: your. divyanshbro7@gmail.com
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/divyansh-tripathi7)

