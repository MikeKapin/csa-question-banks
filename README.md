# CSA Gas Technician Question Banks

Complete question banks for CSA Gas Technician G2 and G3 certification exams, extracted from official TSSA training materials.

## Overview

This repository contains 2,506 practice questions from 64 exams and quizzes covering all aspects of gas technician certification in Ontario, Canada.

### Statistics

- **G2 Exams**: 38 exams with 2,103 questions
- **G3 Quizzes**: 26 quizzes with 403 questions
- **Total Questions**: 2,506

## Repository Structure

```
csa-question-banks/
├── README.md                 # This file
├── index.json               # Complete metadata and directory
├── g2-exams/                # G2 Gas Technician exam questions
│   ├── exam-01.json
│   ├── exam-02.json
│   ├── ...
│   └── gas-tech-ii-level-3-final-exam.json
└── g3-quizzes/              # G3 Gas Technician quiz questions
    ├── unit-03-gas-properties.json
    ├── b149-code-quiz-5.json
    ├── g3-tssa-prep-exam-1-2022.json
    └── ...
```

## Data Format

All question files follow a consistent JSON structure:

```json
{
  "exam_id": "exam_1",
  "exam_name": "Exam 1",
  "question_count": 48,
  "source_file": "Exam 1.docx",
  "questions": [
    {
      "question_number": 1,
      "question_text": "The best method of removing dust from a house is by",
      "options": {
        "A": "Humidification",
        "B": "Exfiltration",
        "C": "Filtration",
        "D": "Infiltration"
      },
      "correct_answer": null
    }
  ]
}
```

### Field Descriptions

- `exam_id`: Unique identifier for the exam/quiz
- `exam_name`: Human-readable name
- `question_count`: Total number of questions
- `source_file`: Original source document
- `questions`: Array of question objects
  - `question_number`: Sequential question number
  - `question_text`: The question itself
  - `options`: Object with A, B, C, D answer choices
  - `correct_answer`: Answer key (may be null for some exams)

## G2 Gas Technician (Level 2)

The G2 certification covers:

- Forced air heating systems
- Water heaters and combination systems
- Commercial and residential installations
- Venting systems
- Building science and HVAC
- Air quality and filtration
- Ductwork design and installation

### Key G2 Exams

- **TSSA Practice Exams (2023)**: Official practice exams #1-6
- **Gas Tech II Exams**: Level 2 and Level 3 final exams
- **Module-Specific Exams**: Forced air add-ons, specific system types
- **Standard Exams 1-38**: Core curriculum coverage

## G3 Gas Technician (Level 1)

The G3 certification covers:

- CSA B149.1 Code fundamentals
- Gas properties and safety
- Basic piping systems
- Gas appliances
- Customer relations
- Technical manuals and documentation
- TSSA Act and regulations

### Key G3 Materials

#### Unit Quizzes
- Unit 3: Gas Properties
- Unit 4: Codes & Standards
- Unit 5: Electricity & Combustion
- Unit 6: Technical Manuals
- Unit 7: Customer Relations
- Unit 8: Piping Systems
- Unit 9: Gas Appliances

#### TSSA Exam Prep
- **G3 TSSA Prep Exam #1 (2022)**: 161 questions - comprehensive review
- **Gas Tech 3 Level 2 Review**: 69 questions
- **B149 Code Quizzes**: Code-specific questions
- **TSSA Act Quiz**: Regulatory compliance

## Usage

### Loading Questions

```javascript
// Load an exam
const exam = require('./g2-exams/exam-01.json');
console.log(`${exam.exam_name}: ${exam.question_count} questions`);

// Access questions
exam.questions.forEach(q => {
  console.log(`Q${q.question_number}: ${q.question_text}`);
  console.log(`A) ${q.options.A}`);
  console.log(`B) ${q.options.B}`);
  console.log(`C) ${q.options.C}`);
  console.log(`D) ${q.options.D}`);
});
```

### Random Question Generator

```javascript
const fs = require('fs');
const path = require('path');

function getRandomQuestions(count, category = 'g2') {
  const dir = category === 'g2' ? './g2-exams' : './g3-quizzes';
  const files = fs.readdirSync(dir);
  const allQuestions = [];

  files.forEach(file => {
    const data = JSON.parse(fs.readFileSync(path.join(dir, file)));
    allQuestions.push(...data.questions);
  });

  // Shuffle and return
  return allQuestions
    .sort(() => Math.random() - 0.5)
    .slice(0, count);
}

// Get 20 random G2 questions
const quiz = getRandomQuestions(20, 'g2');
```

### Filter by Topic

```javascript
const index = require('./index.json');

// Find all G3 B149 Code quizzes
const codeQuizzes = index.g3_quizzes.by_topic['CSA B149 Code'];
codeQuizzes.forEach(quiz => {
  console.log(`${quiz.quiz_name}: ${quiz.question_count} questions`);
  const data = require(`./${quiz.file}`);
  // Process questions...
});
```

## Study Tips

### For G3 Candidates

1. **Start with Fundamentals**: Begin with Unit 3-9 quizzes
2. **Master the Code**: Focus heavily on B149 Code quizzes
3. **Know the TSSA Act**: Complete the TSSA Act quiz thoroughly
4. **Practice Tests**: Use the G3 TSSA Prep Exam #1 (161 questions) for final review

### For G2 Candidates

1. **Building Science**: Focus on exams 1, 9, 10 for HVAC fundamentals
2. **Water Heaters**: Exam 11 covers water heaters and combo systems
3. **Decorative Appliances**: Exam 6 covers fireplaces, room heaters, etc.
4. **Forced Air Systems**: Exam 5 and Mod 23 cover furnaces in detail
5. **Final Review**: Complete all TSSA Practice Exams from 2023

## Topics Covered

### G2 Topics
- Building envelope and heat loss
- HVAC systems and ductwork
- Air quality and filtration systems
- Electronic air cleaners
- Humidifiers and dehumidifiers
- Forced air furnaces (all types)
- Water heaters (all configurations)
- Combination heating systems
- Venting systems (all categories)
- Gas pressure regulation
- Electrical controls and troubleshooting
- Appliance installation and clearances

### G3 Topics
- CSA B149.1 and B149.2 Code
- Gas properties and characteristics
- Piping materials and methods
- Gas appliances (ranges, dryers, etc.)
- Pressure testing
- Venting fundamentals
- Safety devices and controls
- Customer service
- Documentation requirements
- TSSA regulations and compliance

## Important Notes

1. **Answer Keys**: Some exams may not include answer keys (`correct_answer` fields are `null`)
2. **Code References**: Many questions reference specific code sections
3. **Practice Only**: These are practice materials - actual TSSA exams may differ
4. **Current Standards**: Questions are based on CSA B149.1-25 (2025 edition) where applicable
5. **Ontario-Specific**: Content is specific to Ontario regulations and TSSA requirements

## Data Source

All questions extracted from:
- Official TSSA training materials
- CSA Gas Trade Edition 7 curriculum
- TSSA Practice Exams (2022-2023)
- College program final exams
- Industry standard training documents

## Certification Information

### TSSA G3 Gas Technician
- **Level**: Entry level (G3)
- **Scope**: Install, service, and maintain simple gas appliances
- **Requirements**: Pass TSSA G3 written exam
- **Typical Appliances**: Ranges, dryers, water heaters, simple heating equipment

### TSSA G2 Gas Technician
- **Level**: Advanced (G2)
- **Scope**: All G3 work plus complex systems
- **Requirements**: Pass TSSA G2 written exam + practical experience
- **Typical Systems**: Forced air systems, boilers, complex venting, commercial equipment

## License

This data is provided for educational and training purposes. All content is sourced from official CSA and TSSA training materials.

## Contributing

This repository is automatically maintained. Questions are extracted from the official CSA dev-tools MCP server.

### Extraction Tools Used
- `mcp__dev-tools__dev_list_exams`
- `mcp__dev-tools__dev_list_g3_quizzes`
- `mcp__dev-tools__dev_get_exam_questions`
- `mcp__dev-tools__dev_get_random_g3_questions`

## Support

For questions about:
- **TSSA Certification**: Visit [TSSA.org](https://www.tssa.org)
- **CSA Standards**: Visit [CSA Group](https://www.csagroup.org)
- **This Repository**: Open an issue

## Version History

- **v1.0.0** (2026-02-05): Initial release with 2,506 questions from 64 exams/quizzes

---

**Last Updated**: February 5, 2026
**Questions**: 2,506
**Exams**: 64 (38 G2 + 26 G3)
