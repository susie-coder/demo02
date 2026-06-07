export interface Member {
  id: number;
  name: string;
  role: string;
  avatar: string;
  bio: string;
  email: string;
}

export interface Paper {
  id: number;
  title: string;
  authors: string;
  journal: string;
  year: number;
  abstract: string;
  doi: string;
}

export interface NewsItem {
  id: number;
  title: string;
  date: string;
  summary: string;
  content: string;
}

export interface ResearchArea {
  id: number;
  name: string;
  description: string;
  icon: string;
}
