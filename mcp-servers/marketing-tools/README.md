# Marketing Tools MCP Server

Unified Model Context Protocol (MCP) server providing 33 marketing analysis tools for SEO, GEO, Ads Analytics, and more.

## 🚀 Quick Start

### Installation

```bash
cd mcp-servers/marketing-tools
npm install
```

### Configuration

Copy `.env.example` to `.env` and configure API keys:

```bash
cp .env.example .env
```

Required environment variables:
- `OPENAI_API_KEY` - For ChatGPT integration
- `PERPLEXITY_API_KEY` - For Perplexity integration
- `GEMINI_API_KEY` - For Google Gemini integration
- `REDIS_URL` (optional) - For caching (defaults to `redis://localhost:6379`)

### Development

```bash
# Build TypeScript
npm run build

# Run in development mode (watch)
npm run dev

# Run in production
npm start
```

### Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- multiEngineTest

# Watch mode
npm run test:watch
```

## 📚 Available Tools

### ✅ Implemented (P0)

#### GEO-001: Multi-Engine Test
Execute prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to analyze brand visibility.

**Usage**:
```typescript
import { runMultiEngineTest } from './tools/geo/multiEngineTest';

const results = await runMultiEngineTest({
  prompts: [
    { prompt_id: 'p1', text: 'What are the best marketing analytics tools?' },
    { prompt_id: 'p2', text: 'Compare Acme vs Competitor A' }
  ],
  engines: ['chatgpt', 'perplexity', 'gemini'],
  target_brand: 'Acme Corp',
  max_concurrent: 50,
});

console.log(results.data.summary.brand_mention_rate);
```

**Features**:
- ✅ Parallel execution across 50 concurrent requests
- ✅ Automatic retry with exponential backoff
- ✅ Citation extraction
- ✅ Brand mention detection
- ✅ Per-engine analytics

**Docs**: [docs/tools/GEO-001.md](docs/tools/GEO-001.md)

#### GEO-002: Analyze Citations
LLM-powered parallel analysis of citations to determine sentiment, relevance, and competitive positioning.

**Usage**:
```typescript
import { analyzeCitations } from './tools/geo/analyzeCitations';

const analysis = await analyzeCitations({
  test_results: multiEngineResults.data.results,
  target_brand: 'Acme Corp',
  competitors: ['Competitor A', 'Competitor B'],
  analysis_depth: 'DEEP',
  include_sentiment: true,
});

console.log(analysis.data.insights.overall_sentiment);
console.log(analysis.data.insights.recommendations);
```

**Features**:
- ✅ Sentiment analysis (positive/neutral/negative)
- ✅ Relevance scoring
- ✅ Competitive positioning analysis
- ✅ Theme extraction
- ✅ Actionable recommendations

**Docs**: [docs/tools/GEO-002.md](docs/tools/GEO-002.md)

### ⏳ Planned (P1-P3)

See [MCP_TOOLS_COMPREHENSIVE_PLAN.md](../../MCP_TOOLS_COMPREHENSIVE_PLAN.md) for complete roadmap of 33 tools.

## 🏗️ Project Structure

```
marketing-tools/
├── src/
│   ├── index.ts                    # MCP server entry point
│   ├── tools/
│   │   ├── geo/                   # GEO tools (✅ 2/3 implemented)
│   │   │   ├── multiEngineTest.ts       # GEO-001
│   │   │   ├── analyzeCitations.ts      # GEO-002
│   │   │   └── competitorVisibility.ts  # GEO-003 (planned)
│   │   ├── seo/                   # SEO tools (⏳ 0/4 implemented)
│   │   ├── ads/                   # Ads tools (⏳ 0/6 implemented)
│   │   └── shared/
│   │       └── types.ts           # Shared type definitions
│   ├── clients/                   # API clients (to be implemented)
│   └── utils/
│       ├── errors.ts              # Error classes
│       └── logger.ts              # Structured logging
├── tests/
│   ├── unit/                      # Unit tests
│   ├── integration/               # Integration tests
│   ├── fixtures/                  # Test data
│   └── helpers/                   # Test utilities
├── docs/
│   └── tools/                     # Per-tool documentation
└── package.json
```

## 🧪 Testing Framework

All tools follow comprehensive testing standards:

- **Unit Tests**: 80%+ code coverage
- **Input Validation Tests**: All edge cases
- **Error Handling Tests**: All failure modes
- **Performance Tests**: Concurrency limits
- **Integration Tests**: Cross-tool workflows

**Test a specific tool**:
```bash
npm test -- multiEngineTest.test
```

**Generate coverage report**:
```bash
npm run test:coverage
open coverage/lcov-report/index.html
```

## 📖 Development Standards

All tools must follow the standards defined in [MCP_DEVELOPMENT_FRAMEWORK.md](../../MCP_DEVELOPMENT_FRAMEWORK.md):

- ✅ TypeScript strict mode
- ✅ Zod input validation
- ✅ Comprehensive error handling
- ✅ Structured logging
- ✅ JSDoc documentation
- ✅ 80%+ test coverage

## 🔄 Development Workflow

### Adding a New Tool

1. **Spec**: Define tool in `docs/tools/{TOOL-ID}.md`
2. **Types**: Create types in `src/tools/{category}/{toolName}.ts`
3. **Validation**: Add Zod schemas
4. **Implementation**: Implement core logic
5. **Tests**: Write comprehensive tests
6. **Docs**: Update documentation

See [MCP_DEVELOPMENT_FRAMEWORK.md](../../MCP_DEVELOPMENT_FRAMEWORK.md) for detailed workflow.

## 📊 Performance

- **GEO-001**: ~2-5 seconds for 100 prompts across 3 engines (with 50 concurrent requests)
- **GEO-002**: ~5-10 seconds for 100 citation analyses (with 20 concurrent LLM calls)

## 🐛 Troubleshooting

### Missing API Keys
```
Error: OPENAI_API_KEY not configured
```
**Solution**: Copy `.env.example` to `.env` and add your API keys.

### Rate Limit Errors
```
RateLimitError: Rate limit exceeded
```
**Solution**: Reduce `max_concurrent` parameter or wait for rate limit window to reset.

### Tests Failing
```
FAIL tests/unit/tools/geo/multiEngineTest.test.ts
```
**Solution**: Ensure all dependencies are installed (`npm install`) and environment is configured.

## 📝 License

MIT

## 🤝 Contributing

1. Follow [MCP_DEVELOPMENT_FRAMEWORK.md](../../MCP_DEVELOPMENT_FRAMEWORK.md)
2. Write tests for all new code
3. Ensure `npm test` and `npm run lint` pass
4. Update documentation

## 📞 Support

For issues or questions:
- Review [MCP_TOOLS_REQUIREMENTS.md](../../MCP_TOOLS_REQUIREMENTS.md) for tool specifications
- Review [MCP_TOOLS_COMPREHENSIVE_PLAN.md](../../MCP_TOOLS_COMPREHENSIVE_PLAN.md) for roadmap
- Check test files for usage examples

---

**Status**: 🚧 In Development
**Tools Implemented**: 2 of 33 (6%)
**Next**: GEO-003 (Competitor Visibility), SEO-001 (Keyword Research)
