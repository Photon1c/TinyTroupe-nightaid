#!/usr/bin/env python3
"""
TinyTroupe Agent Tools

Additional utilities for working with TinyTroupe agent schemas:
- Fragment creation
- Schema validation  
- Batch operations
- Schema modification
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
import difflib

class FragmentCreator:
    """Create agent fragments that can be merged with existing agents"""
    
    def __init__(self):
        self.fragment_data = {
            "type": "Fragment",
            "persona": {}
        }
    
    def create_political_fragment(self):
        """Create a political orientation fragment"""
        print("POLITICAL ORIENTATION FRAGMENT")
        print("=" * 40)
        
        orientation = input("Political orientation (e.g., progressive, conservative, libertarian): ")
        
        # Collect political beliefs
        print("\nPolitical beliefs and positions:")
        beliefs = []
        while True:
            belief = input("Political belief (empty to finish): ").strip()
            if not belief:
                break
            beliefs.append(belief)
        
        # Collect political interests
        print("\nPolitical interests:")
        interests = []
        while True:
            interest = input("Political interest (empty to finish): ").strip()
            if not interest:
                break
            interests.append(interest)
        
        # Collect political behaviors
        print("\nPolitical behaviors:")
        behaviors = []
        while True:
            behavior = input("Political behavior (empty to finish): ").strip()
            if not behavior:
                break
            behaviors.append(behavior)
        
        self.fragment_data["persona"] = {
            "beliefs": beliefs,
            "preferences": {
                "interests": interests
            },
            "behaviors": {
                "general": behaviors
            }
        }
        
        # Save fragment
        filename = f"{orientation}.agent.fragment.json"
        with open(filename, 'w') as f:
            json.dump(self.fragment_data, f, indent=4)
        
        print(f"Political fragment saved to {filename}")
        return filename
    
    def create_hobby_fragment(self):
        """Create a hobby/interest fragment"""
        print("HOBBY/INTEREST FRAGMENT")
        print("=" * 30)
        
        hobby_name = input("Hobby/Interest name: ")
        
        # Collect hobby-related interests
        interests = []
        print(f"\n{hobby_name}-related interests:")
        while True:
            interest = input("Interest (empty to finish): ").strip()
            if not interest:
                break
            interests.append(interest)
        
        # Collect hobby-related skills
        skills = []
        print(f"\n{hobby_name}-related skills:")
        while True:
            skill = input("Skill (empty to finish): ").strip()
            if not skill:
                break
            skills.append(skill)
        
        # Collect hobby-related behaviors
        behaviors = []
        print(f"\n{hobby_name}-related behaviors:")
        while True:
            behavior = input("Behavior (empty to finish): ").strip()
            if not behavior:
                break
            behaviors.append(behavior)
        
        self.fragment_data["persona"] = {
            "preferences": {
                "interests": interests
            },
            "skills": skills,
            "behaviors": {
                "general": behaviors
            }
        }
        
        # Save fragment
        safe_name = re.sub(r'[^\w\s-]', '', hobby_name)
        safe_name = re.sub(r'[\s_-]+', '_', safe_name).lower()
        filename = f"{safe_name}_hobby.agent.fragment.json"
        
        with open(filename, 'w') as f:
            json.dump(self.fragment_data, f, indent=4)
        
        print(f"Hobby fragment saved to {filename}")
        return filename

class SchemaValidator:
    """Validate TinyTroupe agent schemas"""
    
    REQUIRED_FIELDS = {
        "type": str,
        "persona": dict
    }
    
    PERSONA_REQUIRED_FIELDS = {
        "name": str
    }
    
    PERSONA_OPTIONAL_FIELDS = {
        "age": int,
        "gender": str,
        "nationality": str,
        "residence": str,
        "education": str,
        "long_term_goals": list,
        "occupation": dict,
        "style": str,
        "personality": dict,
        "preferences": dict,
        "skills": list,
        "beliefs": list,
        "behaviors": dict,
        "health": str,
        "relationships": list,
        "other_facts": list
    }
    
    def validate_schema(self, schema_path: str) -> Dict[str, Any]:
        """Validate an agent schema file"""
        
        result = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "suggestions": []
        }
        
        try:
            with open(schema_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            result["valid"] = False
            result["errors"].append(f"Invalid JSON: {e}")
            return result
        except FileNotFoundError:
            result["valid"] = False
            result["errors"].append(f"File not found: {schema_path}")
            return result
        
        # Check top-level required fields
        for field, expected_type in self.REQUIRED_FIELDS.items():
            if field not in data:
                result["valid"] = False
                result["errors"].append(f"Missing required field: {field}")
            elif not isinstance(data[field], expected_type):
                result["valid"] = False
                result["errors"].append(f"Field '{field}' should be {expected_type.__name__}, got {type(data[field]).__name__}")
        
        # Check persona fields
        if "persona" in data:
            persona = data["persona"]
            
            # Required persona fields
            for field, expected_type in self.PERSONA_REQUIRED_FIELDS.items():
                if field not in persona:
                    result["valid"] = False
                    result["errors"].append(f"Missing required persona field: {field}")
                elif not isinstance(persona[field], expected_type):
                    result["valid"] = False
                    result["errors"].append(f"Persona field '{field}' should be {expected_type.__name__}")
            
            # Optional persona fields type checking
            for field, expected_type in self.PERSONA_OPTIONAL_FIELDS.items():
                if field in persona and not isinstance(persona[field], expected_type):
                    result["warnings"].append(f"Persona field '{field}' should be {expected_type.__name__}, got {type(persona[field]).__name__}")
            
            # Check for empty required lists
            for field in ["long_term_goals", "skills", "beliefs"]:
                if field in persona and isinstance(persona[field], list) and len(persona[field]) == 0:
                    result["warnings"].append(f"Field '{field}' is empty but typically should have at least one item")
            
            # Suggestions for missing recommended fields
            recommended_fields = ["age", "occupation", "personality", "preferences", "skills", "beliefs"]
            for field in recommended_fields:
                if field not in persona:
                    result["suggestions"].append(f"Consider adding '{field}' for a more complete agent")
        
        return result
    
    def print_validation_result(self, result: Dict[str, Any], schema_path: str):
        """Print validation results in a formatted way"""
        
        print(f"\nValidation Results for: {schema_path}")
        print("=" * 50)
        
        if result["valid"]:
            print("✅ Schema is valid!")
        else:
            print("❌ Schema has errors!")
        
        if result["errors"]:
            print(f"\n❌ Errors ({len(result['errors'])}):")
            for error in result["errors"]:
                print(f"  - {error}")
        
        if result["warnings"]:
            print(f"\n⚠️ Warnings ({len(result['warnings'])}):")
            for warning in result["warnings"]:
                print(f"  - {warning}")
        
        if result["suggestions"]:
            print(f"\n💡 Suggestions ({len(result['suggestions'])}):")
            for suggestion in result["suggestions"]:
                print(f"  - {suggestion}")

class SchemaMerger:
    """Merge agent fragments with base agents"""
    
    def merge_fragment_with_agent(self, agent_path: str, fragment_path: str, output_path: str = None):
        """Merge a fragment into an agent schema"""
        
        # Load agent and fragment
        with open(agent_path, 'r') as f:
            agent_data = json.load(f)
        
        with open(fragment_path, 'r') as f:
            fragment_data = json.load(f)
        
        # Merge persona data
        if "persona" in fragment_data:
            if "persona" not in agent_data:
                agent_data["persona"] = {}
            
            self._deep_merge(agent_data["persona"], fragment_data["persona"])
        
        # Save merged result
        if output_path is None:
            base_name = Path(agent_path).stem
            output_path = f"{base_name}_merged.agent.json"
        
        with open(output_path, 'w') as f:
            json.dump(agent_data, f, indent=4)
        
        print(f"Merged agent saved to: {output_path}")
        return output_path
    
    def _deep_merge(self, base_dict: dict, overlay_dict: dict):
        """Deep merge two dictionaries"""
        for key, value in overlay_dict.items():
            if key in base_dict:
                if isinstance(base_dict[key], dict) and isinstance(value, dict):
                    self._deep_merge(base_dict[key], value)
                elif isinstance(base_dict[key], list) and isinstance(value, list):
                    base_dict[key].extend(value)
                else:
                    base_dict[key] = value
            else:
                base_dict[key] = value

class SchemaEditor:
    """Edit existing agent schemas"""
    
    def add_relationship(self, agent_path: str, name: str, description: str):
        """Add a relationship to an agent"""
        with open(agent_path, 'r') as f:
            data = json.load(f)
        
        if "persona" not in data:
            data["persona"] = {}
        if "relationships" not in data["persona"]:
            data["persona"]["relationships"] = []
        
        data["persona"]["relationships"].append({
            "name": name,
            "description": description
        })
        
        with open(agent_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Added relationship to {agent_path}")
    
    def add_skill(self, agent_path: str, skill: str):
        """Add a skill to an agent"""
        with open(agent_path, 'r') as f:
            data = json.load(f)
        
        if "persona" not in data:
            data["persona"] = {}
        if "skills" not in data["persona"]:
            data["persona"]["skills"] = []
        
        data["persona"]["skills"].append(skill)
        
        with open(agent_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Added skill to {agent_path}")
    
    def update_age(self, agent_path: str, new_age: int):
        """Update an agent's age"""
        with open(agent_path, 'r') as f:
            data = json.load(f)
        
        if "persona" in data:
            old_age = data["persona"].get("age", "unknown")
            data["persona"]["age"] = new_age
            
            with open(agent_path, 'w') as f:
                json.dump(data, f, indent=4)
            
            print(f"Updated age from {old_age} to {new_age} in {agent_path}")
        else:
            print("No persona found in agent schema")

def main():
    """Main function for agent tools"""
    print("TinyTroupe Agent Tools")
    print("=" * 30)
    print("1. Create political fragment")
    print("2. Create hobby fragment") 
    print("3. Validate agent schema")
    print("4. Merge fragment with agent")
    print("5. Add relationship to agent")
    print("6. Add skill to agent")
    print("7. Update agent age")
    print("8. Exit")
    
    choice = input("\nSelect option (1-8): ").strip()
    
    if choice == "1":
        creator = FragmentCreator()
        creator.create_political_fragment()
    
    elif choice == "2":
        creator = FragmentCreator()
        creator.create_hobby_fragment()
    
    elif choice == "3":
        schema_path = input("Enter path to agent schema: ").strip()
        validator = SchemaValidator()
        result = validator.validate_schema(schema_path)
        validator.print_validation_result(result, schema_path)
    
    elif choice == "4":
        agent_path = input("Enter path to agent schema: ").strip()
        fragment_path = input("Enter path to fragment: ").strip()
        output_path = input("Enter output path (optional): ").strip() or None
        
        merger = SchemaMerger()
        merger.merge_fragment_with_agent(agent_path, fragment_path, output_path)
    
    elif choice == "5":
        agent_path = input("Enter path to agent schema: ").strip()
        name = input("Relationship name: ").strip()
        description = input("Relationship description: ").strip()
        
        editor = SchemaEditor()
        editor.add_relationship(agent_path, name, description)
    
    elif choice == "6":
        agent_path = input("Enter path to agent schema: ").strip()
        skill = input("Skill to add: ").strip()
        
        editor = SchemaEditor()
        editor.add_skill(agent_path, skill)
    
    elif choice == "7":
        agent_path = input("Enter path to agent schema: ").strip()
        new_age = int(input("New age: "))
        
        editor = SchemaEditor()
        editor.update_age(agent_path, new_age)
    
    elif choice == "8":
        print("Goodbye!")
        return
    
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()