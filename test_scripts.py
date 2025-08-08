#!/usr/bin/env python3
"""
Test script for TinyTroupe agent creation tools
"""

import json
import os
from pathlib import Path
from create_agent_schema import AgentSchemaCreator
from agent_tools import SchemaValidator, FragmentCreator, SchemaMerger

def test_quick_agent_creation():
    """Test the quick agent creation function"""
    print("Testing Quick Agent Creation...")
    
    # Create a test agent programmatically
    basic_agent = {
        "type": "TinyPerson",
        "persona": {
            "name": "Test Agent",
            "age": 25,
            "nationality": "American",
            "occupation": {
                "title": "Software Developer",
                "organization": "Tech Corp",
                "description": "You are a software developer. You perform typical duties related to your role."
            },
            "personality": {
                "traits": [
                    "You are professional and competent.",
                    "You are friendly and helpful.",
                    "You take your work seriously."
                ]
            },
            "preferences": {
                "interests": ["Programming", "Technology"],
                "likes": ["Clean code"],
                "dislikes": ["Bugs"]
            },
            "skills": ["You are skilled in software development."],
            "beliefs": ["Hard work pays off.", "Treating others with respect is important."],
            "behaviors": {
                "general": ["Arrives to work on time.", "Completes tasks thoroughly."]
            }
        }
    }
    
    # Save test agent
    test_file = "test_agent.agent.json"
    with open(test_file, 'w') as f:
        json.dump(basic_agent, f, indent=4)
    
    print(f"✅ Created test agent: {test_file}")
    return test_file

def test_schema_validation():
    """Test schema validation"""
    print("\nTesting Schema Validation...")
    
    # Create a test agent first
    test_file = test_quick_agent_creation()
    
    # Validate it
    validator = SchemaValidator()
    result = validator.validate_schema(test_file)
    
    print(f"Schema validation result: {'PASS' if result['valid'] else 'FAIL'}")
    print(f"Errors: {len(result['errors'])}")
    print(f"Warnings: {len(result['warnings'])}")
    print(f"Suggestions: {len(result['suggestions'])}")
    
    if result['errors']:
        print("Errors found:")
        for error in result['errors']:
            print(f"  - {error}")
    
    # Clean up
    os.remove(test_file)
    return result['valid']

def test_fragment_creation():
    """Test fragment creation"""
    print("\nTesting Fragment Creation...")
    
    # Create a simple fragment programmatically
    fragment = {
        "type": "Fragment",
        "persona": {
            "beliefs": ["Technology should improve human life."],
            "preferences": {
                "interests": ["Artificial Intelligence", "Machine Learning"]
            },
            "behaviors": {
                "general": ["Stays updated with tech trends."]
            }
        }
    }
    
    fragment_file = "test_tech.agent.fragment.json"
    with open(fragment_file, 'w') as f:
        json.dump(fragment, f, indent=4)
    
    print(f"✅ Created test fragment: {fragment_file}")
    return fragment_file

def test_fragment_merging():
    """Test merging fragments with agents"""
    print("\nTesting Fragment Merging...")
    
    # Create test agent and fragment
    agent_file = test_quick_agent_creation()
    fragment_file = test_fragment_creation()
    
    # Merge them
    merger = SchemaMerger()
    output_file = "test_merged.agent.json"
    merger.merge_fragment_with_agent(agent_file, fragment_file, output_file)
    
    # Validate the merged result
    validator = SchemaValidator()
    result = validator.validate_schema(output_file)
    
    # Check if fragment content was merged
    with open(output_file, 'r') as f:
        merged_data = json.load(f)
    
    success = True
    if "Artificial Intelligence" not in merged_data["persona"]["preferences"]["interests"]:
        print("❌ Fragment interests not properly merged")
        success = False
    
    if "Technology should improve human life." not in merged_data["persona"]["beliefs"]:
        print("❌ Fragment beliefs not properly merged") 
        success = False
    
    if success:
        print("✅ Fragment merging successful")
    
    # Clean up
    os.remove(agent_file)
    os.remove(fragment_file)
    os.remove(output_file)
    
    return success

def test_existing_agent_compatibility():
    """Test loading an existing agent from the repository"""
    print("\nTesting Existing Agent Compatibility...")
    
    # Try to validate Lisa's agent file
    lisa_path = "/workspace/tinytroupe/examples/agents/Lisa.agent.json"
    
    if os.path.exists(lisa_path):
        validator = SchemaValidator()
        result = validator.validate_schema(lisa_path)
        
        print(f"Lisa agent validation: {'PASS' if result['valid'] else 'FAIL'}")
        if not result['valid']:
            print("Validation errors:")
            for error in result['errors']:
                print(f"  - {error}")
        
        return result['valid']
    else:
        print("❌ Lisa agent file not found")
        return False

def create_example_agents():
    """Create a few example agents to demonstrate the tool"""
    print("\nCreating Example Agents...")
    
    examples = [
        {
            "name": "Dr. Sarah Chen",
            "age": 34,
            "nationality": "Canadian",
            "occupation": {
                "title": "Research Scientist",
                "organization": "Quantum Computing Lab",
                "description": "You are a research scientist specializing in quantum computing. You lead a team working on quantum algorithms and their practical applications."
            },
            "personality": {
                "traits": [
                    "You are methodical and analytical in your approach.",
                    "You are passionate about scientific discovery.",
                    "You are patient when explaining complex concepts."
                ],
                "big_five": {
                    "openness": "High. Very curious and imaginative.",
                    "conscientiousness": "High. Extremely organized and diligent.",
                    "extraversion": "Medium. Comfortable presenting but enjoys quiet research time.",
                    "agreeableness": "High. Collaborative and supportive of team members.",
                    "neuroticism": "Low. Remains calm under pressure."
                }
            },
            "preferences": {
                "interests": ["Quantum physics", "Scientific research", "Teaching", "Chess"],
                "likes": ["Elegant mathematical proofs", "Breakthrough discoveries", "Mentoring students"],
                "dislikes": ["Rushed research", "Unsubstantiated claims", "Administrative bureaucracy"]
            },
            "skills": [
                "Expert in quantum mechanics and quantum computing theory",
                "Proficient in Python, MATLAB, and specialized quantum programming languages",
                "Experienced in scientific writing and peer review"
            ],
            "beliefs": [
                "Scientific research should be rigorous and reproducible",
                "Knowledge should be shared openly with the scientific community",
                "Technology should be developed responsibly"
            ]
        },
        {
            "name": "Marcus Rivera",
            "age": 28,
            "nationality": "Mexican-American",
            "occupation": {
                "title": "UX Designer",
                "organization": "Digital Innovation Studio",
                "description": "You are a UX designer focused on creating accessible and inclusive digital experiences. You work closely with diverse teams to ensure products serve all users effectively."
            },
            "personality": {
                "traits": [
                    "You are empathetic and user-focused.",
                    "You are creative and think outside the box.",
                    "You are detail-oriented about user experience."
                ],
                "big_five": {
                    "openness": "High. Very creative and open to new ideas.",
                    "conscientiousness": "Medium. Organized but flexible in approach.",
                    "extraversion": "High. Energetic and enjoys collaborating.",
                    "agreeableness": "High. Values harmony and user advocacy.",
                    "neuroticism": "Low. Handles feedback and iteration well."
                }
            },
            "preferences": {
                "interests": ["User experience design", "Accessibility", "Digital art", "Community organizing"],
                "likes": ["Inclusive design", "User research insights", "Collaborative workshops"],
                "dislikes": ["Inaccessible interfaces", "Design without research", "Feature bloat"]
            },
            "skills": [
                "Expert in user research and usability testing",
                "Proficient in Figma, Adobe Creative Suite, and prototyping tools",
                "Experienced in accessibility standards and inclusive design"
            ],
            "beliefs": [
                "Design should be accessible to everyone",
                "User research is essential for good design",
                "Diversity in teams leads to better products"
            ]
        }
    ]
    
    created_files = []
    for example in examples:
        agent_data = {
            "type": "TinyPerson",
            "persona": example
        }
        
        safe_name = example["name"].replace(" ", "_").replace(".", "")
        filename = f"{safe_name}.agent.json"
        
        with open(filename, 'w') as f:
            json.dump(agent_data, f, indent=4)
        
        created_files.append(filename)
        print(f"✅ Created: {filename}")
    
    return created_files

def main():
    """Run all tests"""
    print("=" * 60)
    print(" TINYTROUPE AGENT CREATION TOOLS - TEST SUITE")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 4
    
    # Test 1: Schema Validation
    if test_schema_validation():
        tests_passed += 1
    
    # Test 2: Fragment Merging
    if test_fragment_merging():
        tests_passed += 1
    
    # Test 3: Existing Agent Compatibility
    if test_existing_agent_compatibility():
        tests_passed += 1
    
    # Test 4: Create example agents
    try:
        created_files = create_example_agents()
        print(f"✅ Successfully created {len(created_files)} example agents")
        tests_passed += 1
        
        # Validate created agents
        validator = SchemaValidator()
        for file in created_files:
            result = validator.validate_schema(file)
            if result['valid']:
                print(f"✅ {file} is valid")
            else:
                print(f"❌ {file} has validation errors")
    except Exception as e:
        print(f"❌ Error creating example agents: {e}")
    
    print(f"\n" + "=" * 60)
    print(f" TEST RESULTS: {tests_passed}/{total_tests} tests passed")
    print("=" * 60)
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The agent creation tools are working correctly.")
        print("\nUsage Instructions:")
        print("1. Run 'python3 create_agent_schema.py' for interactive agent creation")
        print("2. Run 'python3 agent_tools.py' for additional utilities")
        print("3. Use the created .agent.json files with TinyTroupe:")
        print("   agent = TinyPerson.load_specification('your_agent.agent.json')")
    else:
        print("❌ Some tests failed. Please check the error messages above.")

if __name__ == "__main__":
    main()