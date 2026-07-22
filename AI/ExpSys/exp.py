tree = {
    "engine won't start": {
        "yes": {
            "battery warning light on": {
                "yes": "dead or weak battery",
                "no": "starter motor or ignition problem"
            }
        },
        "no": {
            "high temperature gauge": {
                "yes": {
                    "coolant level low": {
                        "yes": "coolant leak or low coolant",
                        "no": "engine overheating"
                    }
                },
                "no": {
                    "vehicle pulling to side": {
                        "yes": {
                            "uneven tire wear": {
                                "yes": "wheel alignment problem",
                                "no": "tire pressure imbalance"
                            }
                        },
                        "no": {
                            "warning lights on dashboard": {
                                "yes": {
                                    "check engine light on": {
                                        "yes": "engine sensor or emission issue",
                                        "no": "electrical or system fault"
                                    }
                                },
                                "no": {
                                    "brakes making noise": {
                                        "yes": "worn brake pads or brake issue",
                                        "no": "No clear issue found"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


def ask(q):
    while True:
        ans = input(f"Do you observe {q}? (y/n): ").lower()
        if ans == "y":
            return "yes"
        if ans == "n":
            return "no"
        print("Enter y or n")

def diagnose(node):
    if isinstance(node, str):
        return node
    question = list(node.keys())[0]
    answer = ask(question)

    return diagnose(node[question][answer])

print("--- Vehicle Diagnostics Expert System ---")
print("Answer with y/n\n")
result = diagnose(tree)
print("\n--- Diagnostic Result ---")
print("Most likely issue:", result + ".")