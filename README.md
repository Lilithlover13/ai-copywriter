AI Product Content Generator

An intelligent web application powered by the Google Gemini API that automates content creation—including product descriptions, social media posts, SEO articles, and marketing copy—based on input product data and specifications.

Key Features

Automated Product Descriptions: Generate detailed and engaging descriptions by simply inputting the product name, key features, and target keywords.

Multi-platform Optimization: Create tailored content specifically structured for:

E-commerce platforms (Amazon, Shopify, Shopee, Lazada, TikTok Shop)

Social media channels (Facebook Ads, Instagram Captions, TikTok video scripts)

SEO-optimized blog posts and website copy

Product launch and promotional emails

Customizable Tone of Voice: Adjust the writing style to be professional, persuasive, humorous, luxury-oriented, or casual.

Multimodal Image Analysis: Upload product images to allow Gemini to automatically detect visual attributes and generate relevant copy.

Real-time Streaming Responses: View the generated text in real time as the AI processes the request.

Content Management and Export: Copy text with a single click, export content to Markdown or TXT formats, and save generation history.

Tech Stack

(Modify this section to match your actual project implementation)

Frontend: React.js / Next.js, Tailwind CSS

Backend: Node.js (Express) / Next.js API Routes / Python (FastAPI)

AI Model: Google Gemini API (@google/genai) using gemini-2.5-flash or gemini-2.5-pro

Database (Optional): MongoDB / PostgreSQL / Firebase (for storing generation history and product templates)

Getting Started

1. Prerequisites

Node.js (version 18.x or higher)

npm or yarn

Google Gemini API Key (Obtain one from Google AI Studio)

2. Installation

Step 1: Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Step 2: Install dependencies

npm install
# or
yarn install


Step 3: Configure environment variables
Create a .env (or .env.local) file in the root directory of the project and add your API key:

GEMINI_API_KEY=your_google_gemini_api_key_here
PORT=3000


Step 4: Run the application

npm run dev
# or
yarn dev


Open http://localhost:3000 in your browser to access the application.

Workflow

Product Data Input: Users enter product details into the form (Product Name, Category, Key Features, Target Audience, Pricing/Promotions) or upload a CSV file / product image.

Content Configuration: Users select the target platform, desired word count, output language, and tone of voice.

Prompt Processing and API Call: The backend compiles the input data into a structured prompt and sends the request to the Google Gemini API.

Output and Refinement: The generated copy is displayed in the editor, where users can manually edit the text or request revisions from the AI.

Project Structure

├── public/                 # Static assets (images, favicon, etc.)
├── src/
│   ├── components/         # UI components (Input forms, Result editor, etc.)
│   ├── pages/ (or app/)    # Application views and API routes
│   ├── services/           # Gemini API configuration and request handlers
│   ├── utils/              # Helper functions and structured prompt templates
│   └── styles/             # Global stylesheets and Tailwind configuration
├── .env.example            # Example environment variables file
├── package.json            # Project dependencies and scripts
└── README.md               # Project documentation


Contributing

Contributions to improve the project are welcome. Please follow these steps:

Fork the repository.

Create a new feature branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add YourFeatureName').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

Author: [Your Name]

Email: your.email@example.com

GitHub: https://github.com/your-username
