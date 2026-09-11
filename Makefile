dev-backend:
	cd backend && uv run uvicorn main:app --reload

dev-frontend:
	cd frontend && npm run dev