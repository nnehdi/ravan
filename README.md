
# Ravan Reflect

Ravan Reflect is a versatile CLI application designed to empower individuals on their journey of self-discovery, personal growth, and mental fitness. Combining the power of generative AI with guided reflection, Ravan Reflect offers an innovative way to engage with your thoughts, feelings, and experiences.

## Features

- **Guided Reflection:** Initiate interactive sessions through the terminal using the `ravan reflect` command, engaging in conversation-like journaling powered by large language models (LLMs).
- **Quick Entries:** Record journal entries on-the-fly with the `ravan reflect -m "entry"` command, allowing you to capture your thoughts without launching a full session.
- **Organized Management:** Efficiently manage your entries with commands like `ravan list`, `ravan view`, `ravan edit`, and `ravan delete`.
- **Insightful Analysis:** Gain insights into personality traits, emotional patterns, and personal growth using the `ravan insight` command, driven by AI analysis of your entries.
- **Progress Tracking:** Monitor mood, emotions, and entry count with the `ravan track` command over a specific time frame or date.
- **Day-based Entries:** Associate each entry with a day, enabling easy listing and viewing using the `ravan list -d <date>` command.
- **Personal Recognition:** Ravan Reflect remembers individuals, life events, milestones, and cherished memories, creating a more intimate and meaningful reflection experience.
- **Effortless Search:** Easily search through your entries using keywords, dates, or specific criteria for quick access to past reflections.

## Installation

Ravan Reflect is distributed via pipx, ensuring cross-platform compatibility. To install Ravan Reflect, open your terminal and run:

```bash
pipx install ravan-reflect
```

## Usage

- To launch an interactive reflection session:
```bash
ravan reflect
```

- To quickly record an entry without an interactive session:
```bash
ravan reflect -m "Today, I learned a valuable lesson about perseverance."
```

### Entry Management

- List all journal entries:
```bash
ravan list
```
*Example:*
```
- Entry 1: 2023-08-10
- Entry 2: 2023-08-11
- Entry 3: 2023-08-12
```

- View a specific journal entry:
```bash
ravan view 2
```
*Example:*
```
Date: 2023-08-11
-----
Today was a productive day. I completed my coding project and went for a long walk in the evening. Feeling accomplished!
```

- Edit a specific journal entry:
```bash
ravan edit 3
```

- Delete a specific journal entry:
```bash
ravan delete 1
```

### Insights and Tracking

- Gain insights based on your journal entries:
```bash
ravan insight
```
*Example:*
```
Insights for the past week:

- Mood: Positive
- Emotions: Optimistic, Content
- Entries recorded: 10

Your journaling efforts have contributed to a positive outlook and productive week. Keep up the great work!
```

- Track mood, emotions, and entries over time:
```bash
ravan track
```
*Example:*
```
Tracking summary for the past month:

- Mood: Mixed
- Emotions: Stressed, Hopeful
- Entries recorded: 30
```

### Day-based Entries

- List and view entries for a specific day:
```bash
ravan list -d 2023-08-11
```
*Example:*
```
Entries for 2023-08-11:

1. Reflecting on today's achievements.
2. Meeting with Jane and discussing project plans.
```

### Effortless Search

- Search through entries using keywords, dates, or criteria:
```bash
ravan search "project"
```
*Example:*
```
Search results for "project":

1. Project brainstorming session with team.
2. Completed coding project and submitted final report.
```

## Roadmap

We're continuously working to enhance Ravan Reflect with new features and improvements. Stay tuned for updates on our [roadmap](roadmap-link-here).

## Contributing

We welcome contributions from the community! If you'd like to contribute, please refer to our [contribution guidelines](contributing-link-here).

## License

Ravan Reflect is open-source and licensed under the [MIT License](license-link-here).

---

Transform your introspection into a journey of self-discovery with Ravan Reflect. Engage, reflect, and evolve.

For more information, visit our [website](https://ravan-reflect.com) or contact us at contact@ravan-reflect.com.
