
# Ravan Reflect

Ravan Reflect is a versatile CLI application designed to empower individuals on their journey of self-discovery, personal growth, and mental fitness. Combining the power of generative AI with guided reflection, Ravan Reflect offers an innovative way to engage with your thoughts, feelings, and experiences.



## Guide

## Reflect

Engage in a guided reflection session with Ravan.

**Command Syntax:**
```
ravan reflect
```

**Examples:**
1. 
```bash
$ ravan reflect
```

**Output:**
```
Let's begin your reflection.

How do you feel at this very moment?
Hint: Try to describe your emotions as vividly as you can.
...
```

2.
```bash
$ ravan reflect
```

**Output:**
```
Reflect on a challenge you faced today. What did you learn from it?
Hint: Consider how you approached the situation and if there's anything you'd do differently.
...
```

---

## Insight

Pose a question about yourself, and Ravan will provide answers based on your past reflections.

**Command Syntax:**
```
ravan insight "<your question>"
```

**Examples:**
1. 
```bash
$ ravan insight "How have I been feeling lately?"
```

**Output:**
```
Based on your recent reflections:
- You've expressed feeling overwhelmed on August 21.
- On August 20, you mentioned feeling content and productive.
...
```

2.
```bash
$ ravan insight "What did I learn from last week's challenges?"
```

**Output:**
```
From your reflections on last week:
- You recognized the importance of taking breaks during work on August 18.
- On August 17, you learned to communicate more effectively with challenging colleagues.
...
```

---

## Progress

See how many reflection sessions you've had with Ravan.

**Command Syntax:**
```
ravan progress
```

**Examples:**
1. 
```bash
$ ravan progress
```

**Output:**
```
You've had 12 reflection sessions with Ravan. Keep it up!
```

2.
```bash
$ ravan progress
```

**Output:**
```
You're on a streak! 5 days of continuous reflections with Ravan. Keep going!
```

---


### LS - List Reflections:

**Command:**
```bash
$ ravan ls
```

```
Reflections:

1. 2023-08-23: "Feeling a mix of anxiety and excitement after the interview..."
2. 2023-08-22: "Content day. Finished reading 'The Art of Happiness'..."
3. 2023-08-21: "Felt overwhelmed with work tasks. Need to manage time better..."
4. 2023-08-20: "Had a great day at the beach. Felt relaxed and at peace..."
5. 2023-08-19: "Attended a workshop on emotional intelligence. Took away some key insights..."

To dive deeper into a specific reflection, use: ravan view <reflection_number>
```

**Example to view a specific reflection:**

**Command:**
```bash
$ ravan view 3
```

```
2023-08-21:

Felt overwhelmed with work tasks. Need to manage time better. Started the day with back-to-back meetings which left little time for actual work. In the afternoon, had to juggle multiple tasks simultaneously. I need to improve my task prioritization and maybe communicate more with my team about workload distribution.
```

### Reflect - Extended Example:

**Command:**
```bash
$ ravan reflect
```

```
Ravan: Let's begin your reflection.
How do you feel at this very moment?
Hint: Try to describe your emotions as vividly as you can.
```

```
I feel a mix of anxiety and excitement. I had an interview today, and I'm not sure how it went.
```

```
Ravan: Interviews can indeed be nerve-wracking. Let's dive deeper.
What specifically about the interview makes you feel anxious?
Hint: Was it a particular question, the atmosphere, or maybe the impression you felt you left?
```

```
It was mainly the technical round. I felt unprepared for some of the questions, and I stuttered a few times.
```

```
Ravan: Understandable. It's natural to feel that way, especially when faced with unexpected challenges.
On the other hand, what made the experience exciting for you?
Hint: Was there a moment you felt proud of or perhaps an aspect of the job that excites you?
```

```
I was excited because the role aligns with what I've always wanted to do. Plus, the interviewer seemed impressed with my past projects.
```

```
Ravan: That's a positive takeaway! Remember, one round doesn't define the whole interview. Focus on the positives and learn from areas of improvement.
Would you like to set a reminder for some preparatory steps for future technical rounds?
Hint: Revisiting certain topics or practicing mock interviews can be beneficial.
```

```
Yes, that sounds like a good idea. I'd like to revisit some core concepts and practice mock interviews.
```

```
Ravan: Great choice! Reflecting on our experiences and preparing for the future is a key part of personal growth.
Thank you for today's reflection. Remember, every experience is a step towards growth.
```
