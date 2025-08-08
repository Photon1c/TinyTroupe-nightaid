#!/usr/bin/env python3
"""
TinyTroupe Agent Tools Launcher

Simple launcher to access all agent creation and management tools.
"""

import subprocess
import sys
import os

def main():
    """Main launcher interface"""
    
    print("🤖 TinyTroupe Agent Tools Launcher")
    print("=" * 50)
    print()
    print("Available Tools:")
    print("1. 🆕 Create New Agent (Interactive)")
    print("2. 🔧 Agent Tools & Utilities")
    print("3. ✅ Run Test Suite")
    print("4. 📖 View Documentation")
    print("5. 🧪 Create Example Agents")
    print("6. ❌ Exit")
    print()
    
    while True:
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            print("\n🆕 Launching Agent Creator...")
            subprocess.run([sys.executable, "create_agent_schema.py"])
            break
            
        elif choice == "2":
            print("\n🔧 Launching Agent Tools...")
            subprocess.run([sys.executable, "agent_tools.py"])
            break
            
        elif choice == "3":
            print("\n✅ Running Test Suite...")
            subprocess.run([sys.executable, "test_scripts.py"])
            break
            
        elif choice == "4":
            print("\n📖 Opening Documentation...")
            if os.path.exists("AGENT_CREATION_GUIDE.md"):
                # Try to open with default system program
                if sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(["open", "AGENT_CREATION_GUIDE.md"])
                elif sys.platform.startswith('linux'):  # Linux
                    subprocess.run(["xdg-open", "AGENT_CREATION_GUIDE.md"])
                elif sys.platform.startswith('win'):  # Windows
                    subprocess.run(["start", "AGENT_CREATION_GUIDE.md"], shell=True)
                else:
                    print("Documentation available in: AGENT_CREATION_GUIDE.md")
            else:
                print("Documentation file not found!")
            break
            
        elif choice == "5":
            print("\n🧪 Creating Example Agents...")
            # Run just the example creation part of the test script
            from test_scripts import create_example_agents
            try:
                files = create_example_agents()
                print(f"\n✅ Created {len(files)} example agents:")
                for f in files:
                    print(f"  - {f}")
                print("\nUse these agents in TinyTroupe with:")
                print("agent = TinyPerson.load_specification('filename.agent.json')")
            except Exception as e:
                print(f"❌ Error creating examples: {e}")
            break
            
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()