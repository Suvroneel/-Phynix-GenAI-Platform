# Phynix

> *The more you talk to it, the more it becomes YOURS.*

Most AI talks at you. Phynix grows with you. It remembers what you shared last session, notices your patterns over time, and meets you where you actually are instead of starting from zero every single time.

**🔗 Live Demo:** https://phynix.streamlit.app/

Phynix is an **end-to-end mood-aware GenAI platform** designed to give users a personalised AI experience that genuinely evolves with them. The heart of the system is **Ashva**, an intelligent companion powered by **fine-tuned BERT for emotion detection**, a **RAG memory engine** for persistent context, and **advanced Generative AI models** for casual, human-like conversations.

This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, hybrid AI/NLP backend, RAG pipeline, and relational database analytics.

---

## 🆕 Recent Updates

### v2.2 - RAG Memory Engine + pgvector - April 2026
Ashva now actually remembers you. Not just your last emotion, but real context from both your past conversations and diary entries. Built a unified RAG pipeline using pgvector on Supabase PostgreSQL with sentence-transformers (all-MiniLM-L6-v2) for semantic embeddings. Every chat message and diary entry gets embedded and stored in a vector store. When you return, Ashva retrieves the most semantically relevant memories across both sources and uses them to generate a genuinely personal welcome, powered by the LLM. The more you talk and write, the more Ashva actually knows you. Falls back to emotion-based greeting if no embeddings exist yet, and a generic welcome for brand new users. This is what "the more you talk to it, the more it becomes YOURS" actually means under the hood.

### v2.1.1 - Ashva Diaries (Mood Journal) - March 2026
Replaced the static placeholder with a fully functional journaling feature. Users can write daily reflections, optionally attach an image, and view today's entries as timestamped cards. Entries are stored in Supabase PostgreSQL with images in a dedicated Supabase Storage bucket. Fresh slate every day at midnight IST. Built with privacy-first design, no mood tagging, no sentiment analysis, just open reflection.

### v2.0 - Multi-Model GenAI Backend - February 2026
Replaced static hard-coded responses with a live multi-model GenAI backend. Ashva now generates dynamic, context-aware responses using 5 LLMs (Llama 3.1, Mistral 7B, Zephyr 7B, Phi-2, Gemma 2B) via Hugging Face Inference API. Users can switch models in real-time mid-conversation.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Page Descriptions](#page-descriptions)
- [Backend Architecture](#backend-architecture)
- [AI & NLP Layer](#ai--nlp-layer)
- [Frontend & UX Design](#frontend--ux-design)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)

---

## Overview

Phynix is a **mood-aware conversational AI platform** that combines:

- **RAG Memory Engine**: pgvector on Supabase PostgreSQL stores semantic embeddings of every conversation and diary entry. Ashva retrieves the most relevant past context on every login.
- **Hybrid Conversational AI**: Emotion classification via fine-tuned BERT, coupled with state-of-the-art Generative AI models for fluid, casual dialogue that actually sounds human.
- **Multi-Model Architecture**: Supports 5 different AI models with real-time switching capabilities.
- **Analytics & Dashboards**: Track emotional trends, confidence metrics, and patterns over time.
- **Private Journaling**: Secure daily journaling that feeds into the RAG memory pool.

The platform emphasises **personalisation, privacy, and genuine contextual awareness** over generic AI responses.

---

## 📁 Project Structure
