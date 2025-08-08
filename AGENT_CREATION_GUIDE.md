# TinyTroupe Agent Schema Creation Tools

This repository contains powerful tools to simplify the creation and management of agent schemas for the TinyTroupe library. Instead of manually writing complex JSON files, you can now use interactive scripts that guide you through the process.

## 🚀 Quick Start

1. **Interactive Agent Creation**: Run the main creation script
   ```bash
   python3 create_agent_schema.py
   ```

2. **Quick Agent Template**: For simple agents, choose option 2 for template-based creation

3. **Additional Tools**: Access utilities for validation, fragments, and editing
   ```bash
   python3 agent_tools.py
   ```

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `create_agent_schema.py` | Main interactive agent creation tool |
| `agent_tools.py` | Additional utilities (validation, fragments, editing) |
| `test_scripts.py` | Test suite and examples |
| `AGENT_CREATION_GUIDE.md` | This documentation |

## 🎯 Features

### 1. Interactive Agent Creation (`create_agent_schema.py`)

**Comprehensive Mode**: Guides you through creating detailed agent personas including:
- Basic information (name, age, nationality, education)
- Occupation details with role descriptions
- Personality traits and Big Five assessment
- Preferences, interests, likes/dislikes
- Skills and core beliefs
- Behavioral patterns and daily routines
- Health status and relationships
- Background information and life experiences

**Quick Template Mode**: Creates basic agents with minimal input for rapid prototyping.

### 2. Agent Tools (`agent_tools.py`)

**Fragment Creation**: 
- Political orientation fragments
- Hobby/interest fragments
- Custom personality overlays

**Schema Validation**:
- Validates JSON structure
- Checks required fields
- Provides suggestions for improvement
- Compatible with existing TinyTroupe agents

**Fragment Merging**:
- Combine base agents with personality fragments
- Deep merge functionality preserves existing data
- Useful for creating agent variants

**Schema Editing**:
- Add relationships to existing agents
- Update skills and attributes
- Modify agent characteristics

## 🔧 Usage Examples

### Creating a New Agent

```bash
$ python3 create_agent_schema.py

TinyTroupe Agent Schema Creator
===============================
1. Interactive agent creation (comprehensive)
2. Quick agent creation (template-based)
3. Exit

Select option (1-3): 1
```

The script will guide you through each section:

1. **Basic Information**
   - Agent name: "Dr. Sarah Chen"
   - Age: 34
   - Nationality: "Canadian"
   - etc.

2. **Occupation**
   - Job title: "Research Scientist"
   - Organization: "Quantum Computing Lab"
   - Detailed role description

3. **Personality** 
   - Communication style
   - Personality traits
   - Big Five assessment

4. **And much more...**

### Validating an Agent Schema

```bash
$ python3 agent_tools.py

TinyTroupe Agent Tools
======================
3. Validate agent schema

Enter path to agent schema: Dr_Sarah_Chen.agent.json

✅ Schema is valid!
💡 Suggestions (2):
  - Consider adding 'health' for a more complete agent
  - Consider adding 'other_facts' for a more complete agent
```

### Creating and Merging Fragments

```bash
# Create a political orientation fragment
$ python3 agent_tools.py
1. Create political fragment

Political orientation: progressive
# ... follow prompts ...

# Merge with existing agent
4. Merge fragment with agent
Enter path to agent schema: Dr_Sarah_Chen.agent.json
Enter path to fragment: progressive.agent.fragment.json
Merged agent saved to: Dr_Sarah_Chen_merged.agent.json
```

## 📋 Agent Schema Structure

The tools create agents following this structure:

```json
{
    "type": "TinyPerson",
    "persona": {
        "name": "Agent Name",
        "age": 30,
        "nationality": "Country",
        "education": "Educational background",
        "long_term_goals": ["Goal 1", "Goal 2"],
        "occupation": {
            "title": "Job Title",
            "organization": "Company Name",
            "description": "Detailed role description..."
        },
        "style": "Communication style",
        "personality": {
            "traits": ["Trait 1", "Trait 2"],
            "big_five": {
                "openness": "High. Description",
                "conscientiousness": "Medium. Description",
                "extraversion": "Low. Description",
                "agreeableness": "High. Description",
                "neuroticism": "Low. Description"
            }
        },
        "preferences": {
            "interests": ["Interest 1", "Interest 2"],
            "likes": ["Like 1", "Like 2"],
            "dislikes": ["Dislike 1", "Dislike 2"]
        },
        "skills": ["Skill 1", "Skill 2"],
        "beliefs": ["Belief 1", "Belief 2"],
        "behaviors": {
            "general": ["Behavior 1", "Behavior 2"],
            "routines": {
                "morning": ["Morning activity 1"],
                "workday": ["Work activity 1"],
                "evening": ["Evening activity 1"],
                "weekend": ["Weekend activity 1"]
            }
        },
        "health": "Health description",
        "relationships": [
            {
                "name": "Person Name",
                "description": "Relationship description"
            }
        ],
        "other_facts": ["Background fact 1", "Background fact 2"]
    }
}
```

## 🧩 Fragment System

Fragments allow you to create reusable personality components:

```json
{
    "type": "Fragment",
    "persona": {
        "beliefs": ["Fragment-specific beliefs"],
        "preferences": {
            "interests": ["Fragment interests"]
        },
        "behaviors": {
            "general": ["Fragment behaviors"]
        }
    }
}
```

Common fragment types:
- **Political orientations**: Progressive, conservative, libertarian, etc.
- **Hobbies**: Sports, arts, technology, etc.
- **Professional traits**: Leadership, technical, creative, etc.

## 🎓 Integration with TinyTroupe

Once you've created an agent schema, use it in TinyTroupe:

```python
from tinytroupe.agent import TinyPerson

# Load your custom agent
agent = TinyPerson.load_specification('Dr_Sarah_Chen.agent.json')

# Use the agent in simulations
agent.say("Hello, I'm Dr. Sarah Chen!")
```

## ✅ Best Practices

1. **Be Specific**: Provide detailed descriptions for occupation and personality
2. **Use Second Person**: Write traits and skills as "You are..." or "You can..."
3. **Include Context**: Add background information and relationships for richer interactions
4. **Validate Early**: Use the validation tool to catch issues before testing
5. **Use Fragments**: Create reusable components for common personality traits
6. **Test Iteratively**: Start with basic agents and add complexity over time

## 🔍 Validation and Quality Checks

The validation system checks for:

- **Required fields**: `type`, `persona.name`
- **Field types**: Ensures strings, lists, and objects are used correctly
- **Completeness**: Suggests missing recommended fields
- **Structure**: Validates nested objects like `occupation` and `personality`

## 🚀 Advanced Usage

### Batch Operations

Create multiple similar agents by:
1. Creating a base agent
2. Creating personality fragments for variations
3. Merging fragments with the base agent

### Agent Families

Create related agents (e.g., team members) by:
1. Defining shared characteristics in fragments
2. Creating individual base agents
3. Merging shared fragments across agents

### Version Control

- Use descriptive filenames: `Sarah_Chen_v2.agent.json`
- Keep fragments separate: `quantum_researcher.fragment.json`
- Document changes in agent `other_facts`

## 🐛 Troubleshooting

### Common Issues

1. **JSON Validation Errors**: Use the validation tool to identify syntax issues
2. **Missing Required Fields**: The validator will highlight what's missing
3. **Type Mismatches**: Ensure lists are arrays and objects are dictionaries
4. **File Not Found**: Check file paths and working directory

### Getting Help

1. Run `python3 test_scripts.py` to verify installation
2. Check existing agents in `tinytroupe/examples/agents/` for reference
3. Use the validation tool for detailed error messages

## 📊 Example Agents

The test suite creates two example agents:

1. **Dr. Sarah Chen**: Research scientist with quantum computing expertise
2. **Marcus Rivera**: UX designer focused on accessibility and inclusion

These demonstrate different personality types and professional backgrounds.

## 🤝 Contributing

To extend these tools:

1. **Add new fragment types** in `agent_tools.py`
2. **Enhance validation rules** in the `SchemaValidator` class
3. **Create new templates** in the quick creation function
4. **Add batch operations** for specific use cases

## 📝 License

These tools are designed to work with the TinyTroupe library and follow the same licensing terms.