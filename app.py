
import streamlit as st

st.set_page_config(
    page_title="Concept Bridge",
    page_icon="🌉",
    layout="wide"
)

st.sidebar.title("🌉 Concept Bridge")
st.sidebar.caption("Connect What You Know. Discover What You Need.")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Subject Library",
        "Concept Connections",    
        "Knowledge Check",
        "Personalised Learning",
        "Prerequisite Finder",
        "Visual Learning Roadmap",
        "Learning Progress"
    ]
)

if page == "Dashboard":
    st.title("🌉 Welcome to Concept Bridge")
    st.write("Your personalised learning space.")

    name = st.text_input("Enter your name")

    if name:
        st.success(f"Welcome, {name}!")

    st.subheader("Your Learning Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Subjects", "6")
    col2.metric("Topics", "12")
    col3.metric("Completed", "0")

    st.subheader("Explore Your Learning")
    st.write("Discover concepts, connect subjects and identify knowledge gaps.")


elif page == "Subject Library":
    st.title("📚 Subject Library")
    st.write("Explore subjects, discover topics and expand your knowledge.")

    subjects = {
        "Mathematics": [
            "Algebra", "Calculus", "Probability",
            "Statistics", "Trigonometry", "Linear Algebra",
            "Differential Equations", "Discrete Mathematics"
        ],
        "Computer Science": [
            "C Programming", "Python", "Java", "C++",
            "Data Structures", "Algorithms", "Operating Systems",
            "Computer Networks", "Database Management",
            "Web Development"
        ],
        "Physics": [
            "Mechanics", "Electricity", "Magnetism",
            "Optics", "Thermodynamics", "Waves"
        ],
        "Chemistry": [
            "Atomic Structure", "Chemical Bonding",
            "Organic Chemistry", "Inorganic Chemistry",
            "Chemical Reactions", "Thermodynamics"
        ],
        "Artificial Intelligence": [
            "Introduction to AI", "Machine Learning",
            "Deep Learning", "Neural Networks",
            "Natural Language Processing",
            "Computer Vision", "Generative AI"
        ],
        "Biology": [
            "Cell Biology", "Genetics", "Human Anatomy",
            "Ecology", "Microbiology", "Evolution"
        ],
        "Electrical Engineering": [
            "Circuit Theory", "Electrical Machines",
            "Power Systems", "Control Systems"
        ],
        "Electronics": [
            "Digital Electronics", "Analog Electronics",
            "Semiconductor Devices", "Microprocessors"
        ],
        "Mechanical Engineering": [
            "Engineering Mechanics", "Thermodynamics",
            "Fluid Mechanics", "Manufacturing"
        ],
        "Civil Engineering": [
            "Structural Engineering", "Surveying",
            "Building Materials", "Geotechnical Engineering"
        ],
        "English": [
            "Grammar", "Vocabulary", "Communication Skills",
            "Reading Comprehension", "Creative Writing"
        ],
        "Environmental Science": [
            "Ecosystems", "Climate Change",
            "Pollution", "Natural Resources"
        ],
        "Economics": [
            "Microeconomics", "Macroeconomics",
            "Demand and Supply", "Markets"
        ],
        "Psychology": [
            "Human Behaviour", "Memory",
            "Learning", "Cognitive Psychology"
        ]
    }

    search = st.text_input(
        "🔍 Search for a subject or topic",
        placeholder="Example: Python, Algebra, Machine Learning..."
    )

    found = 0

    for subject, topics in subjects.items():
        matching_topics = [
            topic for topic in topics
            if search.lower() in topic.lower()
        ]

        subject_matches = search.lower() in subject.lower()

        if not search or subject_matches or matching_topics:
            with st.expander(f"📘 {subject}"):
                if search and subject_matches:
                    for topic in topics:
                        st.write("•", topic)
                        found += 1
                else:
                    for topic in matching_topics:
                        st.write("•", topic)
                        found += 1

    if search and found == 0:
        st.warning("No matching subject or topic found. Try another search.")

elif page == "Knowledge Check":
    st.title("🧠 Knowledge Check")
    st.write("Test your understanding.")

    question = st.radio(
        "Which symbol is used for a single-line comment in Python?",
        ["//", "#", "/* */", "<!-- -->"]
    )

    if st.button("Check Answer"):
        if question == "#":
            st.success("Correct! # is used for a single-line comment in Python.")
        else:
            st.error("Not quite. Try again!")

elif page == "Concept Connections":
    st.title("🔗 Concept Connections")
    st.write("Discover how concepts from different subjects are connected.")

    concept_map = {
    "Python": {
        "Algorithms": "Python helps us write and execute step-by-step solutions to problems.",
        "Artificial Intelligence": "Python provides libraries and tools used to build AI systems.",
        "Data Science": "Python helps collect, analyse, and visualise data."
    },
    "Algebra": {
        "Linear Algebra": "Algebra introduces mathematical ideas used in vectors and matrices.",
        "Machine Learning": "Algebra helps us understand mathematical calculations in ML models.",
        "Statistics": "Algebra supports equations and calculations used in statistical analysis.",
        "Data Science": "Algebra provides equations and mathematical methods used to analyse datasets."
    },
    "Physics": {
        "Mathematics": "Mathematical equations help describe physical laws and motion.",
        "Electrical Engineering": "Physics explains electricity, voltage, current, and energy.",
        "Computer Science": "Physics explains the electronic components and hardware used in computers.",
        "Artificial Intelligence": "Physics helps AI understand sensor data, motion, and real-world environments." 
    },
    "Biology": {
        "Chemistry": "Chemical reactions explain many processes inside living organisms.",
        "Genetics": "Genetics studies how characteristics are passed from parents to offspring.",
        "Biotechnology": "Biology provides knowledge used in developing biological technologies.",
        "Environmental Science": "Biology helps us understand ecosystems, biodiversity, and how living organisms interact with their environment."
    },
    "Statistics": {
        "Data Science": "Statistics helps us understand patterns and make decisions from data.",
        "Machine Learning": "Statistics helps evaluate patterns and predictions made by ML models."
    },
    "Computer Networks": {
        "Cyber Security": "Network knowledge helps us understand how to protect connected systems.",
        "Internet of Things": "Networks allow smart devices to communicate and exchange data."
    },
    "Chemistry": {
        "Biology": "Chemistry explains molecules and reactions involved in living systems.",
        "Environmental Science": "Chemistry helps us understand pollution and environmental changes.",
    },
    "Ecology": {
        "Biology": "Ecology studies how living organisms interact with one another and their environment.",
        "Environmental Science": "Ecology helps us understand ecosystems, biodiversity, and environmental balance."
    }
}
if page == "Concept Connections":       
    examples = {
        "Python": {
            "Algorithms": "A program sorts student marks from highest to lowest.",
            "Artificial Intelligence": "A chatbot answers students' questions.",
            "Data Science": "A college analyses student performance data."
    },
        "Algebra": {
            "Linear Algebra": "A computer uses vectors to represent data.",
            "Machine Learning": "A model uses mathematical calculations to make predictions.",
            "Statistics": "A teacher calculates the average marks of a class.",
            "Data Science": "A student uses algebraic equations to analyse academic data."
    },
        "Physics": {
            "Mathematics": "Equations help calculate the speed of a moving car.",
            "Electrical Engineering": "Electricity principles help design circuits.",
            "Computer Science": "Physics concepts help explain computing hardware and electronic devices.",
            "Artificial Intelligence": "Physics helps AI systems understand real-world motion, sensors, and physical environments." 
    },
        "Biology": {
            "Chemistry": "Chemical reactions help explain digestion.",
            "Genetics": "DNA helps explain inherited characteristics.",
            "Biotechnology": "Microorganisms are used to make useful products.",
            "Environmental Science": "Students study how forests, plants, and animals interact with their environment."
    },
        "Statistics": {
            "Data Science": "Data analysts study trends in collected information.",
            "Machine Learning": "Prediction models are evaluated using statistical measures."
    },
        "Computer Networks": {
            "Cyber Security": "Network security helps protect college computer systems.",
            "Internet of Things": "Smart devices communicate through a network."
    },
        "Chemistry": {
            "Biology": "Chemical processes help explain how cells function.",
            "Environmental Science": "Scientists analyse pollutants in water samples."
    },
    "Ecology": {
        "Biology": "Students study how plants, animals, and microorganisms interact in an ecosystem.",
        "Environmental Science": "Students learn how ecosystems help maintain environmental balance."
    }
}    
if page == "Concept Connections":
    search_concept = st.text_input(                                                    
         "🔍 Search for a concept:",
         placeholder="Try Python, Algebra, Physics..."
        )
    matching_concepts = [
    concept for concept in concept_map
    if search_concept.lower() in concept.lower()
    or any(search_concept.lower() in connected.lower()
           for connected in concept_map[concept])
]
    if not matching_concepts:
        st.warning("No matching concept found. Try another word.")
    matching_concepts = list(concept_map.keys())

    if "concept_selector" not in st.session_state:
        st.session_state["concept_selector"] = matching_concepts[0]

    if "next_concept" in st.session_state:
        st.session_state["concept_selector"] = st.session_state.pop("next_concept")

    selected_concept = st.selectbox(
        "Choose a concept to explore:",
        matching_concepts,
        key="concept_selector"
)    
    st.subheader(f"Concepts connected to {selected_concept}")

    for connected_concept, explanation in concept_map[selected_concept].items():
        st.markdown(f"### 🔹 {connected_concept}")
        st.write(explanation)
        st.markdown("**🌍 Real-world example:**")
        st.write(examples[selected_concept][connected_concept])
        st.divider() 
    st.info("These connections show how knowledge from one subject helps you understand another.")
    st.subheader("🔗 Related Concept Explorer")

    st.write("Discover how concepts connect across different subjects.")

    direct_connections = set(concept_map[selected_concept].keys())
    related_concepts = []

    for concept, connections in concept_map.items():
        if concept != selected_concept and concept not in direct_connections and any(
            connected in direct_connections
            for connected in connections
        ):
            related_concepts.append(concept)

    if related_concepts:
        st.write("Other subjects connected through shared concepts:")
        for related in related_concepts:
            st.markdown(f"🔹 {related}")
    else:
        st.write("No additional related concepts found.")

    st.subheader("🗺️ Interactive Concept Network")
    st.write("Discover how your selected concept connects with other subjects.")
    st.metric("Direct Connections", len(concept_map[selected_concept]))
    st.metric("Related Concepts", len(related_concepts))
    st.subheader("🧩 Visual Connection Diagram")
    st.write("See how your selected concept connects with other ideas.")

    st.markdown(
        f"""
        <div style="text-align:center; padding:15px;
                    background-color:#253858; color:white;
                    border-radius:12px; font-size:22px;">
            🌟 {selected_concept}
        </div>
        <div style="text-align:center; font-size:25px; padding:8px;">
            ↓
        </div>
        <div style="text-align:center; font-weight:bold;">
            Direct Connections
        </div>
        <div style="display:grid; grid-template-columns:repeat(2,1fr);
                    gap:12px; padding:10px;">
        {''.join([
            f'<div style="padding:14px; background-color:#DCEBFF; color:#17365D; border-radius:10px;"><b>📘 {name}</b><br><small>{explanation}</small></div>'
            for name, explanation in concept_map[selected_concept].items()
        ])}
        </div>
        <div style="text-align:center; font-size:25px; padding:8px;">
            ↓
        </div>
        <div style="text-align:center; font-weight:bold;">
            Related Concepts
        </div>
        <div style="display:grid; grid-template-columns:repeat(2,1fr);
                    gap:12px; padding:10px;">
            {''.join([
                f'<div style="padding:14px; background-color:#E4F5E9; color:#205B35; border-radius:10px;"><b>💡 {name}</b><br><small>Connected through shared concepts</small></div>'
                for name in related_concepts
            ])}
        </div>
                """,
        unsafe_allow_html=True
    )
    # Main concept
    with st.container(border=True):
        st.markdown(f"## 🌟 {selected_concept}")
        st.caption("🎯 Your central learning concept")
        st.write("Explore how this concept connects with other subjects and ideas.")
    # Direct connections
    st.markdown("### 🔗 Direct Connections")
    st.caption("Concepts directly linked to your selected subject.")

    direct_connections = concept_map[selected_concept]
    connection_names = list(direct_connections.keys())

    columns = st.columns(2)

    for i, connected in enumerate(connection_names):
        with columns[i % 2]:
            with st.container(border=True):
                with st.expander(f"📘 {connected}"):
                    st.caption("Directly connected concept")
                    st.write(direct_connections[connected])                            
                    st.markdown("**🌍 Real-world example:**")
                    st.write(examples[selected_concept][connected])
    st.markdown("### 🌐 Related Concepts")
    st.caption("Discover additional concepts through shared connections.")

    if related_concepts:
        columns = st.columns(2)

        for i, related in enumerate(related_concepts):
            shared = set(direct_connections.keys()).intersection(
                concept_map[related].keys()
            )

            with columns[i % 2]:
                with st.expander(f"💡 {related}"):
                     st.caption("Indirectly connected concept")

                     st.markdown("**🔗 Shared concepts:**")
                     st.write(", ".join(sorted(shared)))

                     st.markdown("**📚 How subjects are connected:**")
                     for shared_concept in sorted(shared):
                         st.write(
                             f"{related} connects with {selected_concept} through {shared_concept}."
                         )

                     st.info("Explore this subject in the Subject Library.")

                     if related in concept_map:
                         if st.button(f"Explore {related}", key=f"explore_{related}"):
                            st.session_state["next_concept"] = related
                            st.rerun()
    else:
        st.info("Explore more concepts to discover additional connections.")

elif page == "Personalised Learning":
    st.title("🎯 Personalised Learning")
    st.write("Get a learning path based on your interests and current knowledge.")

    st.subheader("Tell us about your learning goals")

    subject = st.selectbox(
        "Choose your subject:",
        [
            "Mathematics",
            "Computer Science",
            "Physics",
            "Chemistry",
            "Artificial Intelligence",
            "Biology"
        ]
    )

    level = st.selectbox(
        "Choose your current level:",
        ["Beginner", "Intermediate", "Advanced"]
    )

    goal = st.selectbox(
        "What do you want to achieve?",
        [
            "Build Strong Fundamentals",
            "Improve Problem Solving",
            "Learn Advanced Concepts"
        ]
    )
    if "show_personalised_path" not in st.session_state:
        st.session_state.show_personalised_path = False
    if st.button("Generate My Learning Path"):
        st.session_state.show_personalised_path = True
        st.session_state.saved_subject = subject
        st.session_state.saved_level = level
        st.session_state.saved_goal = goal

            
        learning_recommendations = {
            "Mathematics": {
                "Beginner": ["Number Systems", "Algebra Basics", "Geometry"],
                "Intermediate": ["Trigonometry", "Calculus", "Statistics"],
                "Advanced": ["Linear Algebra", "Differential Equations", "Advanced Calculus"]
            },
            "Computer Science": {
                "Beginner": ["Computer Fundamentals", "Python Basics", "Problem Solving"],
                "Intermediate": ["Data Structures", "Algorithms", "Object-Oriented Programming"],
                "Advanced": ["Advanced Algorithms", "Operating Systems", "Database Systems"]
            },
            "Physics": {
                "Beginner": ["Units and Measurements", "Motion", "Force and Laws of Motion"],
                "Intermediate": ["Work and Energy", "Waves", "Electricity and Magnetism"],
                "Advanced": ["Electromagnetic Theory", "Modern Physics", "Quantum Mechanics"]
            },
            "Chemistry": {
                "Beginner": ["Atomic Structure", "Elements and Compounds", "Chemical Bonding"],
                "Intermediate": ["Chemical Reactions", "Thermodynamics", "Organic Chemistry"],
                "Advanced": ["Chemical Kinetics", "Electrochemistry", "Advanced Organic Chemistry"]
            },
            "Artificial Intelligence": {
                "Beginner": ["Python Basics", "Mathematics for AI", "Introduction to AI"],
                "Intermediate": ["Machine Learning", "Data Processing", "Neural Networks"],
                "Advanced": ["Deep Learning", "Natural Language Processing", "Computer Vision"]
            },
            "Biology": {
                "Beginner": ["Cell Biology", "Human Body Systems", "Basic Genetics"],
                "Intermediate": ["Molecular Biology", "Ecology", "Evolution"],
                "Advanced": ["Genetic Engineering", "Biotechnology", "Advanced Genetics"]
            }
        }

        recommended_topics = learning_recommendations[subject][level]
        st.session_state.saved_topics = recommended_topics

    if st.session_state.show_personalised_path:
        saved_subject = st.session_state.saved_subject
        saved_level = st.session_state.saved_level
        saved_goal = st.session_state.saved_goal
        recommended_topics = st.session_state.saved_topics

        st.subheader("📚 Your Recommended Learning Path")

        st.write(f"**Subject:** {saved_subject}")
        st.write(f"**Current Level:** {saved_level}")
        st.write(f"**Learning Goal:** {saved_goal}")

        st.success("Your personalised learning path is ready!")

        st.write("### Follow these topics in order:")
        st.write("### Mark topics as completed:")

        completed_count = 0

        for number, topic in enumerate(recommended_topics, start=1):
            if st.checkbox(
                f"{number}. {topic}",
                key=f"personalised_{saved_subject}_{saved_level}_{topic}"
            ):
                completed_count += 1

        total_topics = len(recommended_topics)
        progress = completed_count / total_topics

        st.subheader("📊 Your Learning Progress")
        st.progress(progress)

        st.write(
            f"{completed_count} out of {total_topics} topics completed ({progress:.0%})"
        )

        if completed_count == total_topics:
            st.success("🎉 Congratulations! You completed your learning path!")

        if saved_goal == "Build Strong Fundamentals":
            st.info("Focus on understanding the basics before moving to difficult topics.")
        elif saved_goal == "Improve Problem Solving":
            st.info("Practise problems and apply each concept through exercises.")
        else:
            st.info("Explore advanced concepts and work on practical applications.")
elif page == "Prerequisite Finder":
    st.title("🔍 Prerequisite Finder")
    st.write("Discover what you should learn before starting a new topic.")

    prerequisites = {
        "Python": ["Basic Mathematics", "Problem Solving"],
        "Machine Learning": ["Python", "Statistics", "Linear Algebra"],
        "Deep Learning": ["Python", "Machine Learning", "Linear Algebra"],
        "Data Science": ["Python", "Statistics", "Basic Mathematics"],
        "Algorithms": ["Basic Mathematics", "Problem Solving"],
        "Artificial Intelligence": ["Python", "Algorithms", "Mathematics"],
        "C Programming": ["Basic Computer Knowledge", "Problem Solving"],
        "Data Structures": ["C Programming", "Basic Programming Concepts"],
        "Java": ["Basic Programming Concepts", "Object-Oriented Programming"],
        "Web Development": ["HTML", "CSS", "JavaScript"],
        "Neural Networks": ["Python", "Linear Algebra", "Machine Learning"],
        "Computer Networks": ["Basic Computer Knowledge", "Internet Fundamentals"]
    }
    prerequisite_explanations = {
        "Python": {
            "Basic Mathematics": "Helps understand calculations and logical operations.",
            "Problem Solving": "Builds the ability to break problems into smaller steps."
        },
        "Machine Learning": {
            "Python": "Used to build and implement machine learning models.",
            "Statistics": "Helps understand data patterns and model predictions.",
            "Linear Algebra": "Helps understand vectors, matrices and model calculations."
        },
        "Deep Learning": {
            "Python": "Used to develop and train deep learning models.",
            "Machine Learning": "Provides the foundation for understanding learning algorithms.",
            "Linear Algebra": "Helps understand neural network calculations."
        },
        "Data Science": {
            "Python": "Helps collect, process and analyse data.",
            "Statistics": "Helps identify patterns and interpret data.",
            "Basic Mathematics": "Supports numerical calculations and data analysis."
        },
        "Algorithms": {
            "Basic Mathematics": "Supports logical and mathematical problem solving.",
            "Problem Solving": "Helps develop step-by-step solutions."
        },
        "Artificial Intelligence": {
            "Python": "Helps implement AI applications.",
            "Algorithms": "Provides methods for solving computational problems.",
            "Mathematics": "Supports the logic and calculations used in AI."
        },
        "C Programming": {
            "Basic Computer Knowledge": "Helps understand how programs interact with computers.",
            "Problem Solving": "Develops logical thinking for writing programs."
        },
        "Data Structures": {
            "C Programming": "Provides programming knowledge to implement data structures.",
            "Basic Programming Concepts": "Helps understand how data is organised and processed."
        },
        "Java": {
            "Basic Programming Concepts": "Builds the foundation for writing Java programs.",
            "Object-Oriented Programming": "Helps understand classes, objects and inheritance."
        },
        "Web Development": {
            "HTML": "Provides the structure of web pages.",
            "CSS": "Controls the appearance and layout of web pages.",
            "JavaScript": "Adds interactivity to websites."
        },
        "Neural Networks": {
            "Python": "Helps implement and train neural network models.",
            "Linear Algebra": "Helps understand vectors and matrix calculations.",
            "Machine Learning": "Provides the foundation for understanding neural networks."
        },
        "Computer Networks": {
            "Basic Computer Knowledge": "Helps understand computers and their communication.",
            "Internet Fundamentals": "Explains how devices communicate over the internet."
        }
    }
    selected_topic = st.selectbox(
        "Choose a topic you want to learn:",
        list(prerequisites.keys())
    )

    st.subheader(f"📚 Prerequisites for {selected_topic}")

    st.write("Learn these concepts first:")
    completed = 0

    for i, topic in enumerate(prerequisites[selected_topic], 1):
        is_completed = st.checkbox(
            f"{i}. {topic}",
            key=f"prereq_{selected_topic}_{topic}"
        )

        if is_completed:
            completed += 1

        st.write(prerequisite_explanations[selected_topic][topic])
        st.divider()

    total = len(prerequisites[selected_topic])

    st.subheader("📊 Your Learning Progress")

    st.progress(completed / total)

    st.write(f"{completed} out of {total} prerequisites completed!")

    if completed == total:
        st.success("🎉 Excellent! You are ready to explore this topic!")
elif page == "Visual Learning Roadmap":
    st.title("🗺️ Visual Learning Roadmap")
    st.write("Follow a step-by-step path from beginner to advanced.")

    learning_paths = {
        "Python to Machine Learning": [
            "Basic Computer Knowledge",
            "Python Basics",
            "Python Programming",
            "Statistics",
            "Linear Algebra",
            "Machine Learning",
            "Deep Learning"
        ],
        "C Programming to Data Structures": [
            "Basic Computer Knowledge",
            "C Programming Basics",
            "Loops and Functions",
            "Arrays and Pointers",
            "Data Structures",
            "Algorithms"
        ],
        "Web Development": [
            "HTML",
            "CSS",
            "JavaScript",
            "Frontend Development",
            "Backend Development",
            "Full Stack Development"
        ]
    }

    selected_path = st.selectbox(
        "Choose your learning path:",
        list(learning_paths.keys())
    )

    st.subheader(f"Your Roadmap: {selected_path}")

    stages = [
        ("01 · BEGINNER", learning_paths[selected_path][:1]),
        ("02 · FOUNDATION", learning_paths[selected_path][1:3]),
        ("03 · INTERMEDIATE", learning_paths[selected_path][3:5]),
        ("04 · ADVANCED", learning_paths[selected_path][5:])
    ]

    completed_topics = 0
    total_topics = len(learning_paths[selected_path])
    for stage_name, topics in stages:
        if topics:
            with st.container(border=True):
                st.subheader(stage_name)

                for topic in topics:
                    is_completed = st.checkbox(
                        f"Completed: {topic}",
    key=f"roadmap_{selected_path}_{topic}"
)

                    if is_completed:
                        completed_topics += 1
        if stage_name != "04 · ADVANCED":
            st.markdown(
                "<div style='text-align:center; font-size:28px;'>⬇️</div>",
                unsafe_allow_html=True
            )
    progress = completed_topics / total_topics

    st.subheader("📊 Roadmap Progress")
    st.progress(progress)

    st.write(
        f"{completed_topics} out of {total_topics} topics completed ({progress:.0%})"
    )

    if completed_topics == total_topics:
        st.success("🎉 Congratulations! You completed this learning roadmap!")
elif page == "Learning Progress":
    st.title("📈 Learning Progress")
    st.write("Track your learning journey.")

    st.subheader("Overall Progress")
    st.progress(0)
    st.write("You have just started your learning journey!")

    st.subheader("Upcoming Goals")
    st.write("1. Explore your subjects")
    st.write("2. Complete your first knowledge check")
    st.write("3. Discover connections between concepts")
