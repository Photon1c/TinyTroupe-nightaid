#!/usr/bin/env python3
"""
TinyTroupe Agent Schema Creator

This script provides an interactive way to create agent schemas for the TinyTroupe library.
It guides users through defining agent characteristics and saves the schema in the proper format.
"""

import json
import os
import re
from typing import Dict, List, Any, Optional
from pathlib import Path

class AgentSchemaCreator:
    def __init__(self):
        self.agent_data = {
            "type": "TinyPerson",
            "persona": {}
        }
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self, title: str):
        """Print a formatted header"""
        print("=" * 60)
        print(f" {title}")
        print("=" * 60)
        print()
    
    def get_input(self, prompt: str, required: bool = True, default: str = None) -> str:
        """Get user input with validation"""
        while True:
            if default:
                user_input = input(f"{prompt} (default: {default}): ").strip()
                if not user_input:
                    return default
            else:
                user_input = input(f"{prompt}: ").strip()
            
            if user_input or not required:
                return user_input
            
            if required and not user_input:
                print("This field is required. Please enter a value.")
    
    def get_list_input(self, prompt: str, required: bool = True) -> List[str]:
        """Get a list of items from user input"""
        print(f"\n{prompt}")
        print("Enter items one by one. Press Enter with empty input to finish.")
        
        items = []
        while True:
            item = input(f"  - ").strip()
            if not item:
                break
            items.append(item)
        
        if required and not items:
            print("At least one item is required.")
            return self.get_list_input(prompt, required)
        
        return items
    
    def get_number_input(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        """Get a number input with validation"""
        while True:
            try:
                value = int(input(f"{prompt}: "))
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number.")
    
    def get_choice(self, prompt: str, choices: List[str]) -> str:
        """Get a choice from a list of options"""
        print(f"\n{prompt}")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice}")
        
        while True:
            try:
                choice_num = int(input("Enter choice number: "))
                if 1 <= choice_num <= len(choices):
                    return choices[choice_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(choices)}")
            except ValueError:
                print("Please enter a valid number.")
    
    def get_big_five_trait(self, trait_name: str) -> str:
        """Get Big Five personality trait description"""
        levels = ["Low", "Medium", "High"]
        descriptions = {
            "openness": {
                "Low": "Prefers routine and traditional approaches",
                "Medium": "Balanced between routine and new experiences", 
                "High": "Very imaginative and curious"
            },
            "conscientiousness": {
                "Low": "More spontaneous and flexible",
                "Medium": "Moderately organized and reliable",
                "High": "Meticulously organized and dependable"
            },
            "extraversion": {
                "Low": "Prefers solitude and quiet environments",
                "Medium": "Balanced between social and solitary activities",
                "High": "Very social and energetic"
            },
            "agreeableness": {
                "Low": "More competitive and challenging",
                "Medium": "Balanced cooperation and assertiveness",
                "High": "Supportive and empathetic towards others"
            },
            "neuroticism": {
                "Low": "Generally calm and composed under pressure",
                "Medium": "Moderate emotional responses to stress",
                "High": "More sensitive to stress and emotions"
            }
        }
        
        print(f"\n{trait_name.title()} level:")
        for level in levels:
            print(f"  {level}: {descriptions[trait_name][level]}")
        
        level = self.get_choice("Select level", levels)
        return f"{level}. {descriptions[trait_name][level]}"
    
    def collect_basic_info(self):
        """Collect basic agent information"""
        self.print_header("BASIC INFORMATION")
        
        persona = self.agent_data["persona"]
        
        persona["name"] = self.get_input("Agent name")
        persona["age"] = self.get_number_input("Age", 1, 150)
        persona["gender"] = self.get_input("Gender", required=False)
        persona["nationality"] = self.get_input("Nationality")
        persona["residence"] = self.get_input("Current residence", required=False)
        persona["education"] = self.get_input("Educational background")
        
        # Long-term goals
        persona["long_term_goals"] = self.get_list_input("Long-term goals")
    
    def collect_occupation_info(self):
        """Collect occupation information"""
        self.print_header("OCCUPATION")
        
        persona = self.agent_data["persona"]
        occupation = {}
        
        occupation["title"] = self.get_input("Job title")
        occupation["organization"] = self.get_input("Organization/Company")
        
        print("\nJob description:")
        print("Provide a detailed description of the agent's role, responsibilities, and challenges.")
        print("This should be written in second person ('You are...', 'Your role is...', etc.)")
        occupation["description"] = self.get_input("Description")
        
        persona["occupation"] = occupation
    
    def collect_personality_info(self):
        """Collect personality information"""
        self.print_header("PERSONALITY")
        
        persona = self.agent_data["persona"]
        personality = {}
        
        # Communication style
        persona["style"] = self.get_input("Communication style (how they interact with others)")
        
        # Personality traits
        personality["traits"] = self.get_list_input("Personality traits (write in second person: 'You are...')")
        
        # Big Five personality traits
        print("\nBig Five Personality Traits:")
        big_five = {}
        for trait in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
            big_five[trait] = self.get_big_five_trait(trait)
        
        personality["big_five"] = big_five
        persona["personality"] = personality
    
    def collect_preferences(self):
        """Collect preferences and interests"""
        self.print_header("PREFERENCES & INTERESTS")
        
        persona = self.agent_data["persona"]
        preferences = {}
        
        preferences["interests"] = self.get_list_input("Interests and hobbies")
        preferences["likes"] = self.get_list_input("Things they like")
        preferences["dislikes"] = self.get_list_input("Things they dislike")
        
        persona["preferences"] = preferences
    
    def collect_skills_and_beliefs(self):
        """Collect skills and beliefs"""
        self.print_header("SKILLS & BELIEFS")
        
        persona = self.agent_data["persona"]
        
        # Skills
        persona["skills"] = self.get_list_input("Skills and abilities (write in second person: 'You are proficient in...')")
        
        # Beliefs
        persona["beliefs"] = self.get_list_input("Core beliefs and values")
    
    def collect_behaviors(self):
        """Collect behavioral information"""
        self.print_header("BEHAVIORS & ROUTINES")
        
        persona = self.agent_data["persona"]
        behaviors = {}
        
        # General behaviors
        behaviors["general"] = self.get_list_input("General behaviors and habits")
        
        # Daily routines
        routines = {}
        routine_types = ["morning", "workday", "evening", "weekend"]
        
        for routine_type in routine_types:
            print(f"\n{routine_type.title()} routine:")
            routines[routine_type] = self.get_list_input(f"Activities during {routine_type}", required=False)
        
        behaviors["routines"] = routines
        persona["behaviors"] = behaviors
    
    def collect_health_and_relationships(self):
        """Collect health and relationship information"""
        self.print_header("HEALTH & RELATIONSHIPS")
        
        persona = self.agent_data["persona"]
        
        # Health
        persona["health"] = self.get_input("Health status and any relevant medical information", required=False)
        
        # Relationships
        relationships = []
        print("\nRelationships:")
        print("Add important people in the agent's life (colleagues, family, friends, etc.)")
        
        while True:
            add_relationship = input("\nAdd a relationship? (y/n): ").lower().strip()
            if add_relationship != 'y':
                break
            
            name = self.get_input("Person's name")
            description = self.get_input("Relationship description")
            relationships.append({"name": name, "description": description})
        
        persona["relationships"] = relationships
    
    def collect_other_facts(self):
        """Collect additional background information"""
        self.print_header("BACKGROUND & OTHER FACTS")
        
        persona = self.agent_data["persona"]
        
        persona["other_facts"] = self.get_list_input("Additional background information, childhood, notable experiences, etc.", required=False)
    
    def preview_agent(self):
        """Show a preview of the created agent"""
        self.print_header("AGENT PREVIEW")
        
        persona = self.agent_data["persona"]
        
        print(f"Name: {persona.get('name', 'N/A')}")
        print(f"Age: {persona.get('age', 'N/A')}")
        print(f"Occupation: {persona.get('occupation', {}).get('title', 'N/A')} at {persona.get('occupation', {}).get('organization', 'N/A')}")
        print(f"Nationality: {persona.get('nationality', 'N/A')}")
        print(f"Interests: {', '.join(persona.get('preferences', {}).get('interests', [])[:3])}...")
        
        print("\nThis is a summary. The full schema contains much more detail.")
    
    def save_agent(self) -> str:
        """Save the agent schema to a JSON file"""
        persona = self.agent_data["persona"]
        agent_name = persona.get('name', 'Agent')
        
        # Clean the name for filename
        safe_name = re.sub(r'[^\w\s-]', '', agent_name)
        safe_name = re.sub(r'[\s_-]+', '_', safe_name)
        
        # Determine save location
        save_dir = input(f"\nSave directory (default: current directory): ").strip()
        if not save_dir:
            save_dir = "."
        
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{safe_name}.agent.json"
        filepath = save_dir / filename
        
        # Save the file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.agent_data, f, indent=4, ensure_ascii=False)
        
        return str(filepath)
    
    def create_agent_interactive(self):
        """Main interactive agent creation process"""
        self.clear_screen()
        self.print_header("TINYTROUPE AGENT SCHEMA CREATOR")
        
        print("This tool will guide you through creating a comprehensive agent schema for TinyTroupe.")
        print("Answer the questions to define your agent's personality, background, and characteristics.")
        print("\nPress Enter to continue...")
        input()
        
        try:
            # Collect all information
            self.collect_basic_info()
            self.collect_occupation_info()
            self.collect_personality_info()
            self.collect_preferences()
            self.collect_skills_and_beliefs()
            self.collect_behaviors()
            self.collect_health_and_relationships()
            self.collect_other_facts()
            
            # Preview and save
            self.preview_agent()
            
            save_choice = input("\nSave this agent schema? (y/n): ").lower().strip()
            if save_choice == 'y':
                filepath = self.save_agent()
                print(f"\n✅ Agent schema saved to: {filepath}")
                print("\nYou can now use this agent in TinyTroupe with:")
                print(f"agent = TinyPerson.load_specification('{filepath}')")
            else:
                print("Agent schema not saved.")
        
        except KeyboardInterrupt:
            print("\n\nAgent creation cancelled.")
        except Exception as e:
            print(f"\nError occurred: {e}")

def create_agent_from_template():
    """Create an agent from a simplified template for quick setup"""
    print("QUICK AGENT CREATION")
    print("=" * 30)
    
    name = input("Agent name: ")
    occupation = input("Occupation: ")
    
    basic_agent = {
        "type": "TinyPerson",
        "persona": {
            "name": name,
            "age": 30,
            "nationality": "American",
            "occupation": {
                "title": occupation,
                "organization": "Generic Corp",
                "description": f"You are a {occupation.lower()}. You perform typical duties related to your role."
            },
            "personality": {
                "traits": [
                    "You are professional and competent.",
                    "You are friendly and helpful.",
                    "You take your work seriously."
                ]
            },
            "preferences": {
                "interests": ["Work-related topics"],
                "likes": ["Efficient processes"],
                "dislikes": ["Inefficiency"]
            },
            "skills": [f"You are skilled in {occupation.lower()} work."],
            "beliefs": ["Hard work pays off.", "Treating others with respect is important."],
            "behaviors": {
                "general": ["Arrives to work on time.", "Completes tasks thoroughly."]
            }
        }
    }
    
    filename = f"{name.replace(' ', '_')}.agent.json"
    with open(filename, 'w') as f:
        json.dump(basic_agent, f, indent=4)
    
    print(f"Basic agent schema saved to {filename}")
    return filename

def main():
    """Main function"""
    print("TinyTroupe Agent Schema Creator")
    print("=" * 40)
    print("1. Interactive agent creation (comprehensive)")
    print("2. Quick agent creation (template-based)")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        creator = AgentSchemaCreator()
        creator.create_agent_interactive()
    elif choice == "2":
        create_agent_from_template()
    elif choice == "3":
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()