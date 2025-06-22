from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from server.resolvers import query, mutation
from pathlib import Path

schema_path = Path(__file__).resolve().parent.parent / "schema" / "schema.graphql"
type_defs = load_schema_from_path(schema_path)
schema = make_executable_schema(type_defs, query, mutation)

app = GraphQL(schema, debug=True)
