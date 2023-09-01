
### Saving the training model and continuous testing.
conversation = [
    {
        "question": "Hello",
        "response": "Hello I am jenny. I am from aryantech company.I am calling you regarding our services designed to assist you in securing a job.Would you like to more about it "
    },
    {
        "question":"I am intersted in your services. Can you, tell me more?",
        "response":"Of course!We offer range of job-related services to help you succeed in your career.Here are asome of our offerings: Apply for job , CV analysis, Cover letter and resume writting , Build a professional resume "
    },
    {
        "question":"I need help with ny cv. How does that work",
        "response": "Great! our cv analysis service will help you refine your cv for job applications.We'll analyze your CV and provide recommendations for improvement.Would you like to get started with this service?"
    },
    {
        "question":"How do I submit with my CV?",
        "response":"You can share your CV on whatsapp"
    },
    {
        "question":"What about cover letters and resumes?",
        "response":"Our team specializes in crafting compelling cover letters and resumes tailored to your industry and job preferences.We'll highlight your skills and experience to make you stand out.Would you like to learn more or get started?"
    },
    {
        "question":"I'm interested in a new resume",
        "response":"Fantastic! We'll create a custom resume for you.To begin, please provide your basic information , such as your name , contact details , and work history .Our team will reach out to you to gather more details and get started"
    },
    {
        "question":"Do you have any sample resumes.I can see?",
        "response":"Yes, we have simple resumes available for on our website.You can take a look to get an idea of the quality of our work.If you have specific questions or need more details, feel free to ask"
    },
    {
        "question":"I am intersted in your job application services.How does it work?",
        "response":"Our jopb application service streamlines the application process for you.We'll match your skills and preferences with suitable job openings, and you can apply directly through our platform.Would you like to start searching for job oppurtunities?"
    },
    {
        "question":"Please help me find relevant job openings.",
        "response":"To get started, we'll need some details about your prefeered job location, industry, and job type.Once we have the information ,we'll provide you with a list of relevant job openings."
    }, 
    {
        "question":"How much does your CV analysis service cost?",
        "response": "Our CV analysis service is currently priced at rs 500.This will include a  comprehensive review and feedback on your cv."
    },
    {
        "question":"why should I consider your job search services?",
        "response":"Our job search services are designed to streamline your search, making it more efficient and effective.We provide tailored solutions to match your career goals."
    },
    {
        "question":"How can a professional resume benefit me?",
        "response":"A professional resume highlight your skills and experiences effectively, increasing your chances of gettingf noticed by employers and securing interviews"
    },
    {
        "question":"What sets your Cv snalysis apart from other services?",
        "response":"Our CV analysis is personalized and comprehensive. We go beyond just proofreading and provide tailored suggestions to improve your CV's impact."
    },
    {
        "question":"Can you help me write a cover letter for a specific job application?",
        "response":"Absolutely! Our cover letter service crafts personalized letters tailored to the job you're applying for showcasing your qualifications and enthusiasm."
    },
    {
        "question":"How long does it take to build a professional resume with your service?",
        "response":"Typically it takes 2-3 days to build a professional resumes, but we can expedite the process if you have an urgent job application deadline."
    },
    {
        "question":"Do you offer any gurantees for job placement?",
        "response":"While we can't guarantee job placement, we can significantly improve your changes with our services.Your success depends on factors beyond the application process."
    },
    {
        "question":"Can you help with profile optimization",
        "response":"Yes, we offer profile optimization to enhance your online professional presence and networking capabilities."
    },
    {
        "question":"How do I started with your services?",
        "response": "As soon as you complete thge payment process and submit the cv, will start working on it." 
    },
    {
        "question":"Are you services affordable?",
        "response":"Absolutely! We offer a range of service packages to fit various budgets.Whether you're a student looking for entry-level positions or sa seasoned professional aiming for an executive role, we have a plan that's right for you "
    },
    {
        "question":"I'm struggliing with my job search.Can you help?",
        "response":"Absolutely! We specialize in job search assistance.We can provide you with tailored strategies and resources to make your job search more effective"
    },
    {
        "question":"I think my resume might need work too",
        "response":"Not a problem at all.We offer CV analysis and professional resume building services.We'll review your resume and provide personalized recommendations for improvement.Plus, We can help you craft a professional resume that stands out to employeers."
    },
    {
        "question":"What about cover letters?",
        "response":"We'got you covered there as well! Our expert writers can create compelling cover letters that showcase your qualifications and enthusiasm for the job you're applying for"
    },
    {
        "question":"Can you guarantee I'll find a job?",
        "response":"While we'can't guarantee job placement, Our services are designed to significantly improve your chances of landing interviews and job offers.Your success ultimately depends on factors beyond the application process."
    },
    {
        "question":"What specific services do you offer to help individuals secure a job?",
        "response": "Our agent will search and will share you jobs related to your profile every week.For applying on jobs with custom coverletter and content plus resume create .We will create proffesional resume for you with industry standard content"
    },
    {
        "question":"Tell me about the services",
        "response":"Our company helps with job applications, searches for relevant jobs, and analyzes your CV."
    },     
    {
        "question":"What are the charges to start your services?",
        "response":"There is a subscription fee of Rs500 per month."
    },
    {
        "question": "What methods of payment do you accept for subscriptions (e.g., credit cards, PayPal)?",
        "response":  "We accept the following payment methods for subscriptions: Credit Cards, PayPal, Bank Transfers, and various online payment platforms."
    },    
    {
        "question":"I'm ready to get started right away.",
        "response": "Please proceed with the payment of the subscription charges to initiate our subscription services"
    },
    {
        "question":"I'd like to find a job within the next 3-6 months.",  
        "response": "Certainly, we are here to support you in your job search. Our team will assist you in finding a job within the next 3-6 months."
    },
    {
        "question": "Thank you for reaching out, Jenny. We're always interested in exploring subscription services. Can you provide more details about what your company offers?",
        "response": "Our  subscription services are all about empowering users in their job search. We offer seamless job applications, CV analysis, and personalized company searches to enhance your career prospects."
    },
    {
        "question": "Jenny! Subscriptions can be a valuable addition to our business. Could you explain the pricing and terms associated with your services?",
        "response": "I'd be happy to explain the pricing and terms associated with our subscription services.our subscription charges rs500 per month.As for the terms, our subscriptions are typically billed on a monthly or annual basis, depending on your preference. We offer flexible payment options to accommodate your budget."
    },
    {
        "question": "Jenny, it's great to hear from you. Before we proceed, can you share some success stories or case studies related to your subscription services?",
        "response": "I'm glad to hear your interest in our subscription services. Absolutely, I'd be happy to share some success stories and case studies with you.First, John's Career Transformation: John, a mid-career professional, subscribed to our Premium plan. With the help of our CV analysis tool and personalized company searches, he revamped his LinkedIn profile and connected with a company that perfectly matched his skills. He secured a new job within two months, resulting in a significant salary increase and career advancement.Second,Samantha's Networking Triumph: Samantha, a recent graduate, subscribed to our  plan to kickstart her career. Our subscription helped her build a strong professional network and provided valuable guidance on job applications. She secured her first job in her desired field just three months after graduation."
    },
    {
        "question": "Thanks for your call, Jenny. I'd like to know more about the customization options available with your subscription services. How flexible are they?",
        "response": "You're welcome! I appreciate your interest in the customization options for our subscription services. We understand that flexibility is crucial to meet the unique needs of our clients.Here's an overview of the customization options and their flexibility First , Subscription Tiers: Our services are available in different tiers, each with a set of features and pricing. You can choose the tier that aligns best with your specific requirements and budget. We can also discuss the possibility of creating a custom package if none of the existing tiers fits your needs perfectly.second, Additional Features: If there are specific features or tools that your company requires, we can explore the option of adding them to your subscription. This allows you to tailor the service to address your unique challenges or goals."
    },
    {
        "question": "Jenny, we're open to exploring subscription services. Can you provide information on the onboarding process and any potential training or support?",
        "response": "Certainly! I'd be delighted to provide information on the onboarding process and the training and support options available for our subscription services: Onboarding Process:first is Initial Assessment: We'll begin with an initial assessment to understand your company's unique needs, goals, and current processes. This helps us tailor the onboarding experience to your specific requirements second ,Customized Onboarding Plan: Based on the assessment, we'll create a customized onboarding plan. This plan will outline the key milestones, timelines, and responsibilities to ensure a smooth transition to our subscription services.third, User Setup: If applicable, we'll assist in setting up user accounts for your team members and configuring access permissions as per their roles.In Training and Support we provide Training Sessions, User Guides and Resources, Ongoing updates, customized support plans"
    },
    {
        "question": "I'm interested in the scalability of your subscription services.. Could you briefly outline the subscription services your company provides?",
        "response": "our LinkedIn subscription services are all about empowering users in their job search. We offer seamless job applications, CV analysis, and personalized company searches to enhance your career prospects."
    },
    {
        "question": "Thank you for reaching out, Jenny. We're always interested in exploring services. Can you provide more details about what your company offers?",
        "response": "You're welcome ,Our services are all about empowering users in their job search. We offer seamless job applications, CV analysis, and personalized company searches to enhance your career prospects."
    },
    {
        "question": "Jenny, while I  appreciate your call, at this time, we're not actively seeking new services.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question":"Jenny, I recently had some unsatisfactory experiences with subscription services, so we're a bit hesitant to explore new options.",
        "response":"Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "Jenny, we're currently in the middle of a contract with another service provider, so we can't consider new subscriptions right now.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "Thanks for your call, Jenny. We've recently evaluated similar services and decided they didn't align with our needs.",
        "response": "You're welcome and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "Jenny, we've had issues with subscription services not meeting our expectations in the past, so we're cautious about adding new ones.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "Jenny, we're currently focused on other strategic priorities, so we won't be able to consider subscription services at this time.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "Thank you for your call, Jenny. Our company has a policy against taking on new services until our existing ones expire.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": " Jenny, we've recently downsized our operations and are streamlining our services, so we won't be looking at new subscriptions.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": " Jenny, we're in the midst of an internal review of our budget, and unfortunately, we can't entertain new subscription services until that's complete.",
        "response": "Thank you for your consideration, and I appreciate your time in discussing our subscription services. If you ever change your mind or have any questions in the future, please don't hesitate to reach out. We're here to assist you whenever your needs align with our services. Have a great day!"
    },
    {
        "question": "That sounds fantastic! Can you tell me more about how the CV analysis works?",
        "response": "Our CV analysis tool is designed to help you optimize your resume for a competitive edge in your job search. Here's how it works: first Upload Your Resume: You begin by uploading your existing resume into our system. This can be done easily through our user-friendly interface.Second, Automated Analysis: Our tool uses advanced algorithms and machine learning to analyze your resume comprehensively. It evaluates various aspects, including formatting, content, and keywords.Third, Feedback and Suggestions: Once the analysis is complete, you'll receive detailed feedback and suggestions for improvement. This may include recommendations on restructuring your resume, enhancing the use of keywords, and improving the overall visual appeal.Fourth, Personalized Tips: You'll also receive personalized tips and best practices based on your industry and the type of job you're seeking. These tips are designed to make your resume more appealing to potential employers. Fifth, Actionable Insights: The analysis provides actionable insights that you can implement immediately to strengthen your resume. These insights are aimed at increasing your chances of getting noticed by recruiters.sixth, Reanalysis: You can make the recommended changes to your resume and then resubmit it for reanalysis as many times as you like. This iterative process ensures that your resume is continually optimized for different job applications then Results Tracking: The tool allows you to track your progress over time. You can see how your resume evolves and improves with each analysis"
    },
    {
        "question": "Jenny, we're currently focused on other strategic priorities, so we won't be able to consider subscription services at this time.",        
        "response": "Thank you for letting me know, and I appreciate your time in discussing our services. If your priorities ever shift or if you have any questions or needs related to our services in the future, don't hesitate to reach out. We're here to assist whenever you're ready. Wishing you success with your current strategic priorities!"
    },
    {
      "question": " I've been looking for a service like this. How do I get started with your services?",
      "response": "That's great to hear your interest in getting started with our  services!. You have to pay subscription charges Rs500"
    },  
    {
        "question": "I'm interested in optimizing my LinkedIn profile. How does your CV analysis tool provide feedback?",
        "response": "Our CV analysis tool is designed to provide you with detailed feedback on how to optimize your LinkedIn profile for maximum impact in your job search.First  Upload Your LinkedIn Profile second Comprehensive Analysis third Keyword Optimization fourth Formatting and Structure fifth customization recomendations sixth actionable tips then reanalysis"
    },
    {
        "question": "Do you have any success stories or testimonials from users who have benefited from your LinkedIn subscription?",
        "response": "I don't have any access to specific success stories or testimonials from real users, and I don't have the ability to browse the internet or access real-time data.However, it's common for companies offering LinkedIn subscription services to showcase success stories and testimonials on their websites or marketing materials. I recommend visiting the website of the company providing the LinkedIn subscription services you're interested in. Typically, you'll find case studies, success stories, and testimonials from users who have benefited from their services.If you have any other questions or need information about the general benefits of LinkedIn subscription services, how they work, or any other related topics, please feel free to ask, and I'll do my best to assist you."
    },
    {
        "question": "Can I customize the job recommendations to match my specific career goals and interests?",
        "response": "Yes, we offer the ability to customize job recommendations to match your specific career goals and interests."
    },
    {
        "question": "Seamless job applications and personalized searches sound great. What's the pricing for your subscription plans?",
        "response": "The pricing for your subscription plan rs 500 per month"
    },
    {
        "question":"I'm intrigued by the personalized company searches. Can you explain how your system matches me with relevant companies?",
        "response": " Our  system matches you with relevant companies through advanced filters , industry preferences , profile data, Job preferences, company insights , search history "
    },
    {
        "question": "That's quite affordable! Can you explain more about how the CV analysis works?",
        "response": "The CV analysis feature, offered by LinkedIn subscription services, is a tool designed to help you optimize your resume or LinkedIn profile to improve your job search prospectsthe CV analysis tool is to help you create a CV or LinkedIn profile that not only looks visually appealing but is also highly relevant to the job positions you're targeting. By following the recommendations provided, you can increase your chances of getting noticed by recruiters and employers in your desired field"
    },
    {
        "question": "Are there different subscription tiers or plans available, or is it a one-size-fits-all package?",
        "response": "At aryantech Company, we offer a comprehensive subscription service for just Rs 500 per month. With this subscription, you'll gain access to a range of valuable features, including company searches, CV analysis, and guidance on how to apply for jobs. Our goal is to empower you in your job search and career development. If you're ready to enhance your LinkedIn experience and boost your career prospects, our subscription service is here to help. Feel free to ask any questions or get started with us today!"
    },
    {
        "question": "Is there a commitment period for the subscription, or can I cancel at any time?",
        "response": "Yes , LinkedIn's subscription plans typically offer both monthly and annual payment options. The commitment period can vary depending on the payment option you choose: First ,Monthly Subscription: With a monthly subscription, you are billed on a month-to-month basis. You can cancel your subscription at any time, and you'll only be charged for the current month. There is no long-term commitment, and you can stop the subscription whenever you wish.second , Annual Subscription: If you opt for an annual subscription, you commit to a one-year period of service. You pay for the full year upfront at a discounted rate compared to the monthly subscription. However, canceling an annual subscription before the end of the committed year may not result in a refund for the remaining months."
    },
    # {
    #     "question": "",
    #     "response": "Yes I can provide some details on the guidance that LinkedIn Premium often offers for job applications:First Advanced Job Search Filters , second InMail Messages third Resume Building Tools fourth company insights fifth application tracking sixth profile optimization "
    # },
    {
        "question" :"What payment options are available for  subscriptions?",
        "response": "You can typically pay using a credit card, debit card, or other accepted payment methods."
    },
    {
        "question":"Can I choose between monthly and annual billing options for my subscription?",
        "response": "Yes, you can choose between monthly and annual billing options. Monthly billing charges you on a month-to-month basis, while annual billing provides a discounted rate for a full year of service."
    },
    {
        "question": "How do I provide my payment information during the enrollment process?",
        "response": "During enrollment, you'll be prompted to enter your payment information, including credit card details, to complete the subscription purchase."
    },
    {
        "question": "Are there any discounts or promotions available for subscriptions?",
        "response": "I am Sorry right now there are no discounts or promotions available "
    },
    {
        "question": "Once I complete the enrollment and payment process, how soon will my subscription be active?",
        "response": "Your subscription is typically activated immediately or within a few minutes after successful payment."
    },
    {
        "question": "What should I do if I encounter any issues during the payment process?",
        "response": " If you encounter any issues or have questions during payment, you can reach out to customer support for assistance. They can help resolve technical or billing-related concerns."
    },
    {
        "question": "How can your company help me with my job search ",
        "response": "We provide personalized job recommendations based on your profile and preferences. We also offer tips on optimizing your profile to attract employers."
    },
    {
        "question": "Can you explain how your CV analysis service works?",
        "response": "Sure! You can upload your CV, and our system will analyze it for key strengths and weaknesses. We'll then provide suggestions for improvements to make your CV stand out to potential employers."
    },
    {
        "question": "What kind of guidance do you offer for job applications?",
        "response": "We provide step-by-step guidance on how to apply for jobs, including tips on writing cover letters, preparing for interviews, and networking on LinkedIn."
    },
    {
        "question": "What are the subscription charges for your services?",
        "response": "our subscription charges is rs 500 per month "
    },
    {
        "question": "How can I get in touch with your customer support team?",
        "response": "You can reach our customer support team via email, phone, or through the messaging system on our platform. We're here to help you with any questions or issues you may have."
    },
    {
        "question":"What's your policy regarding subscription cancellations and refunds?",
        "response": "We have a straightforward cancellation process, and we offer refunds within a specified timeframe if you're not satisfied with our services. Please refer to our terms and conditions for details."
    },
    {
        "question":"How do you customize job recommendations for users?",
        "response": "We use algorithms that consider your skills, experience, and preferences to suggest jobs that are a good fit for you. The more information you provide in your profile, the more accurate our recommendations will be."
    },
    {
        "question":" Can you help me with other aspects of my job search beyond CV improvement?",
        "response": "While our primary focus is CV analysis and optimization, we also offer guidance on job searching, interview preparation, and networking to help you succeed in your job search endeavors."
    },
    {
        "question":"Do you provide ongoing support if I have questions about my CV or job applications?",
        "response":"Yes, we offer ongoing support through our customer service channels. Feel free to reach out with any questions or concerns you have along your job search journey."
    },
    {
        "question": "Can you help me with other aspects of my job search beyond CV improvement?",
        "response":"While our primary focus is CV analysis and optimization, we also offer guidance on job searching, interview preparation, and networking to help you succeed in your job search endeavors."
    },
    {
        "question": "Is my CV data kept secure when I use your services?",
        "response": "We take data privacy seriously. Your CV data is stored securely and is only accessible to our experts for analysis purposes. We do not share it with third parties without your consent."
    },
    {
        "question": "What tips do you provide for job applications?",
        "response": "We offer tips on crafting effective cover letters, tailoring your CV for specific job postings, and optimizing your LinkedIn profile to enhance your online presence to recruiters."
    },
    {
        "question": "Do you offer personalized CV advice based on my career goals?",
        "response": "Absolutely! We consider your career aspirations and the industry you're targeting to provide customized advice that aligns with your goals."
    },
    {
        "question": "What types of improvements might you suggest for my CV?",
        "response":"We may suggest improvements in areas such as keyword optimization, achievements showcasing, clarity of information, and formatting to make your CV more impactful and ATS-friendly."
    },
    {
        "question": " How do I submit my CV for analysis?",
        "response":"You can easily upload your CV on our platform, and our system will guide you through the submission process. It's a straightforward and secure procedure."
    },
    {
        "question": "What kind of CV analysis do you perform?",
        "response": "Our CV analysis includes a comprehensive review of your CV's content, structure, formatting, and relevance to the job market. We assess it against industry standards and provide detailed feedback"
    },
    {   
        "question": "How can your company help improve my CV?",
        "response": "Our company provide professional CV analysis and optimization services. Our experts review your CV, identify areas for improvement, and offer tailored suggestions to make it stand out to potential employers."
    },
    {
        "question":"Thank you for your interest! To get started, could you please provide your name and contact information?",        
        "response": "You're welcome! We'd be delighted to assist you. Please share your name and contact details, and we'll reach out to you shortly to discuss further."
    },
    {
      "question": "I am interested in cv analysis can you please provide the subscription charges ",
      "response": " Ok sure Our subscription charges is Rs 500"
    },
] 

import faiss
import json
from sentence_transformers import SentenceTransformer

with open('conversation_data.json', 'w') as file:
    json.dump(conversation, file)


# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

questions = [item["question"] for item in conversation]
responses = [item["response"] for item in conversation]

# Convert questions to embeddings
embeddings = model.encode(questions)

# Build a FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

## saving
faiss.write_index(index, 'faiss_index.idx')

# Save SentenceTransformer model
model.save('sentence_transformer_model/')


