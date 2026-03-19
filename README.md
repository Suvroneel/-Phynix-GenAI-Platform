# Phynix: AI-Powered Mental Health Chatbot Platform

**🔗 Live Demo:** https://phynix.streamlit.app/

Phynix is an **end-to-end AI mental health platform** designed to provide users a secure and interactive environment to express emotions, track mental well-being, and receive personalized AI-powered guidance. The heart of the system is **Ashva**, an intelligent companion powered by **BERT for emotion detection** and **advanced Generative AI models** for empathetic, context-aware conversations.

This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, hybrid AI/NLP backend, and relational database analytics.

---

## 🆕 Recent Updates

### v2.1.1 — Ashva Diaries (Mood Journal) — March 2026
Replaced the static placeholder with a fully functional journaling feature. Users can write daily reflections, optionally attach an image, and view today's entries as timestamped cards. Entries are stored in Supabase PostgreSQL with images in a dedicated Supabase Storage bucket. Fresh slate every day at midnight IST. Built with privacy-first design — no mood tagging, no sentiment analysis, just open reflection.

### v2.0 — Multi-Model GenAI Backend - Feb 26, 2026
Replaced static hard-coded responses with a live multi-model GenAI backend. Ashva now generates dynamic, context-aware empathetic responses using 5 LLMs (Llama 3.1, Mistral 7B, Zephyr 7B, Phi-2, Gemma 2B) via Hugging Face Inference API. Users can switch models in real-time mid-conversation.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Page Descriptions](#page-descriptions)
  - [Login & Signup Page](#login--signup-page)
  - [Chat Page](#chat-page)
  - [Home Page](#home-page)
  - [Mood Journal Page](#mood-journal-page)
- [Backend Architecture](#backend-architecture)
- [AI & NLP Layer](#ai--nlp-layer)
- [Frontend & UX Design](#frontend--ux-design)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)

---

## Overview

Phynix serves as a **digital mental health companion**, combining:

- **Hybrid Conversational AI**: Emotion classification via fine-tuned BERT, coupled with state-of-the-art Generative AI models for fluid, empathetic dialogue
- **Multi-Model Architecture**: Supports 5 different AI models with real-time switching capabilities for optimal response quality
- **Analytics & Dashboards**: Track emotional trends, risk levels, and confidence metrics over time
- **Private Journaling**: Secure mood journaling for personal reflection and mental health tracking

The platform emphasizes **privacy, data security, and actionable insights**, offering a mental refuge for individuals dealing with stress, anxiety, or depression.

---

## 📁 Project Structure
