import google.generativeai as genai
from config import load_config

class TextToCypher:
    def __init__(self, schema: str):
        self._schema = schema
        
        # Load Gemini API key from config
        config = load_config()
        api_key = config.get_gemini_api_key()
        if not api_key or api_key == "YOUR_GEMINI_API_KEY":
            raise ValueError("Please set your Gemini API key in config.toml")
        
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel('gemini-2.5-flash')

    def __call__(self, question: str):
        # Enhanced prompt with examples
        prompt = f"""You are a Cypher query generator for Neo4j. Convert the question to a Cypher query.

Database Schema:
{self._schema}

CRITICAL RULES:
1. Hero properties: id, name (all lowercase like 'layla', 'miya')
2. Use relationships: (h:Hero)-[:HAS_ROLE]->(r:Role {{name: 'role_name'}})
3. NEVER use h.role or h.lane - they don't exist as properties
4. Role names: marksman, tank, mage, fighter, assassin, support
5. Return ONLY the Cypher query, NO explanations or markdown

EXAMPLES:
Question: List all marksman heroes
Cypher: MATCH (h:Hero)-[:HAS_ROLE]->(r:Role {{name: 'marksman'}}) RETURN h.name

Question: Show me all tank heroes  
Cypher: MATCH (h:Hero)-[:HAS_ROLE]->(r:Role {{name: 'tank'}}) RETURN h.name

Question: Who is Layla?
Cypher: MATCH (h:Hero {{name: 'layla'}}) RETURN h

Question: What heroes counter Miya?
Cypher: MATCH (h:Hero {{name: 'miya'}})<-[:COUNTERS]-(counter:Hero) RETURN counter.name

Question: How many heroes are there?
Cypher: MATCH (h:Hero) RETURN count(h) as total

Now convert this question to Cypher:
Question: {question}
Cypher:"""
        
        response = self._model.generate_content(prompt)
        generated_text = response.text.strip()
        
        # Clean up markdown code blocks if present
        if '```' in generated_text:
            # Extract code from markdown
            lines = generated_text.split('\n')
            code_lines = []
            in_code = False
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
                    continue
                if in_code or (not line.strip().startswith('```') and 'MATCH' in line):
                    code_lines.append(line)
            generated_text = '\n'.join(code_lines).strip()
        
        return generated_text

if __name__ == "__main__":
    with open("schema_example.txt") as fp:
        schema = fp.read().strip()

    print("Preparing pipeline ....")
    ttc = TextToCypher(schema)

    print("Generating ...")
    cypher = ttc("Find all players that submit a comment \"GG!\".")
    print(cypher)
