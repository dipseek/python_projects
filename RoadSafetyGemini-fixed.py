import sys

def road_safety_demo():
    """Demonstrate road safety chatbot functionality without external dependencies"""
    print("=" * 60)
    print("ROAD SAFETY CHATBOT DEMONSTRATION")
    print("=" * 60)
    
    print("\nAvailable Road Safety Queries:")
    print("1. What are the basic road safety rules?")
    print("2. How to drive safely in rain?")
    print("3. What should I do at a traffic signal?")
    print("4. How to maintain safe distance while driving?")
    print("5. What are the speed limits for different roads?")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION MODE")
    print("=" * 60)
    
    # Simulate road safety responses
    safety_responses = {
        "basic road safety rules": [
            "• Always wear seatbelt while driving",
            "• Follow traffic signals and road signs",
            "• Maintain safe distance from other vehicles",
            "• Don't use mobile phone while driving",
            "• Regular vehicle maintenance is essential"
        ],
        "drive safely in rain": [
            "• Reduce speed and increase following distance",
            "• Use windshield wipers and defogger",
            "• Turn on headlights for better visibility",
            "• Avoid sudden braking or acceleration",
            "• Check tire tread depth regularly"
        ],
        "traffic signal": [
            "• Red: Stop completely before the stop line",
            "• Yellow: Prepare to stop, don't rush",
            "• Green: Proceed only when safe",
            "• Always check for pedestrians",
            "• Follow traffic police instructions"
        ],
        "safe distance": [
            "• Maintain 3-second rule in normal conditions",
            "• Increase distance in bad weather",
            "• More distance for larger vehicles",
            "• Adjust distance based on speed",
            "• Always have an escape route"
        ],
        "speed limits": [
            "• Residential areas: 30-40 km/h",
            "• City roads: 50-60 km/h",
            "• Highways: 80-100 km/h",
            "• Expressways: 100-120 km/h",
            "• Always follow posted speed limits"
        ]
    }
    
    queries = [
        "What are the basic road safety rules?",
        "How to drive safely in rain?",
        "What should I do at a traffic signal?",
        "How to maintain safe distance while driving?",
        "What are the speed limits for different roads?"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{i}. Query: {query}")
        
        # Find matching response
        response_found = False
        for key, response in safety_responses.items():
            if key in query.lower():
                print("   AI Response:")
                for point in response:
                    print(f"   {point}")
                response_found = True
                break
        
        if not response_found:
            print("   AI Response: Please ask a specific road safety question.")
        
        print(f"   Status: SUCCESS (Demo Mode)")
        print(f"   Note: In real application, this would use Gemini AI API")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("This demo shows how the Road Safety Chatbot would work.")
    print("In the actual application, it would:")
    print("- Use Gemini AI API for intelligent responses")
    print("- Have a Gradio web interface")
    print("- Provide real-time road safety guidance")
    print("- Handle various road safety queries")

if __name__ == "__main__":
    road_safety_demo()
