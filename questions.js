/**
 * Show das Escrituras - Banco Consolidado de 500 Perguntas das Obras-Padrão
 * 
 * Contém 100 perguntas para cada uma das 5 Obras-Padrão:
 * - QUESTIONS_BOM (100 perguntas - Livro de Mórmon)
 * - QUESTIONS_NT  (100 perguntas - Novo Testamento)
 * - QUESTIONS_OT  (100 perguntas - Velho Testamento)
 * - QUESTIONS_DC  (100 perguntas - Doutrina e Convênios)
 * - QUESTIONS_PGV (100 perguntas - Pérola de Grande Valor)
 * 
 * Total: 500 perguntas de alta dificuldade e variedade com referências das escrituras.
 */

var QUESTIONS_DATABASE = [
  ...(typeof QUESTIONS_BOM !== "undefined" ? QUESTIONS_BOM : []),
  ...(typeof QUESTIONS_NT !== "undefined" ? QUESTIONS_NT : []),
  ...(typeof QUESTIONS_OT !== "undefined" ? QUESTIONS_OT : []),
  ...(typeof QUESTIONS_DC !== "undefined" ? QUESTIONS_DC : []),
  ...(typeof QUESTIONS_PGV !== "undefined" ? QUESTIONS_PGV : [])
];

// Níveis de prêmios da escada
const PRIZE_LADDER = [
  { level: 1, prize: 1000, stop: 0, wrong: 0, difficulty: 1 },
  { level: 2, prize: 2000, stop: 1000, wrong: 500, difficulty: 1 },
  { level: 3, prize: 3000, stop: 2000, wrong: 1000, difficulty: 1 },
  { level: 4, prize: 4000, stop: 3000, wrong: 1500, difficulty: 1 },
  { level: 5, prize: 5000, stop: 4000, wrong: 2000, difficulty: 1 },
  { level: 6, prize: 10000, stop: 5000, wrong: 2500, difficulty: 2 },
  { level: 7, prize: 20000, stop: 10000, wrong: 5000, difficulty: 2 },
  { level: 8, prize: 30000, stop: 20000, wrong: 10000, difficulty: 2 },
  { level: 9, prize: 40000, stop: 30000, wrong: 15000, difficulty: 2 },
  { level: 10, prize: 50000, stop: 40000, wrong: 20000, difficulty: 2 },
  { level: 11, prize: 100000, stop: 50000, wrong: 25000, difficulty: 3 },
  { level: 12, prize: 200000, stop: 100000, wrong: 50000, difficulty: 3 },
  { level: 13, prize: 300000, stop: 200000, wrong: 100000, difficulty: 3 },
  { level: 14, prize: 400000, stop: 300000, wrong: 150000, difficulty: 3 },
  { level: 15, prize: 500000, stop: 400000, wrong: 200000, difficulty: 3 },
  { level: 16, prize: 1000000, stop: 500000, wrong: 0, difficulty: 4 } // Pergunta do Milhão
];

const CATEGORIES_INFO = {
  all: { name: "Todas as Obras-Padrão", badge: "🌟 Universal", color: "#fdb813" },
  bom: { name: "Livro de Mórmon", badge: "📖 Livro de Mórmon", color: "#38bdf8" },
  nt: { name: "Novo Testamento", badge: "✝️ Novo Testamento", color: "#a855f7" },
  ot: { name: "Velho Testamento", badge: "📜 Velho Testamento", color: "#f97316" },
  dc: { name: "Doutrina e Convênios", badge: "🕊️ D&C", color: "#10b981" },
  pgv: { name: "Pérola de Grande Valor", badge: "💎 Pérola de Grande Valor", color: "#ec4899" }
};
