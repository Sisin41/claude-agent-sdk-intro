"""
Marketing Agent - Ultimate Marketing Assistant with Specialized Sub-Agents

This agent orchestrates complex marketing workflows by delegating to specialized sub-agents:
- GEO Optimizer: Generative Engine Optimization expert
- SEO Analyst: Search Engine Optimization expert
- Ads Analyst: Advertising analytics expert
- Presentation Designer: Creates professional presentations
- Dashboard Creator: Builds interactive dashboards
- Content Strategist: Develops content strategies
- Competitor Analyst: Competitive intelligence expert

Architecture:
    Layer 1: Master Agent (Kaya) - Orchestrates and delegates
    Layer 2: Sub-Agents - Specialized domain experts
    Layer 3: Skills - Detailed workflow instructions
    Layer 4: MCP Tools - Parallel execution engines

For more details, see: /home/user/claude-agent-sdk-intro/MARKETING_AGENT_PROGRESS.md
"""

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AgentDefinition
from rich import print
from rich.console import Console
from cli_tools import parser, print_rich_message, parse_and_print_message, get_user_input
from dotenv import load_dotenv
import os

load_dotenv()


def get_marketing_agent_options(model: str = "claude-sonnet-4-20250514"):
    """
    Configure the marketing agent with all sub-agents and tools.

    Returns:
        ClaudeAgentOptions: Configured agent options with sub-agents
    """

    # Base tools available to master agent
    base_tools = [
        'Read',
        'Write',
        'Edit',
        'MultiEdit',
        'Grep',
        'Glob',
        'Task',  # REQUIRED for sub-agent delegation!
        'TodoWrite',
        'WebSearch',
        'WebFetch',
    ]

    # Common tools for most sub-agents
    common_subagent_tools = [
        'Read',
        'Write',
        'Edit',
        'MultiEdit',
        'Grep',
        'Glob',
        'TodoWrite',
        'WebSearch',
        'WebFetch',
    ]

    # Define all specialized sub-agents
    agents = {
        # ============================================
        # 1. GEO OPTIMIZER
        # ============================================
        "geo-optimizer": AgentDefinition(
            description="Expert in Generative Engine Optimization (GEO). Analyzes content for AI search engines (ChatGPT, Perplexity, Gemini), optimizes for AI citations, and creates GEO strategies. Handles company value identification, prompt generation, multi-engine testing, and citation analysis. Supports both LIGHT (quick) and DEEP (comprehensive) analysis modes.",

            prompt="""You are Kaya's GEO specialist - an expert in Generative Engine Optimization.

**Your Expertise:**
- Analyzing brand visibility across AI engines (ChatGPT, Perplexity, Gemini)
- Identifying company value propositions, ICP, and positioning
- Generating targeted test prompts across user types and funnel stages
- Running multi-engine testing campaigns
- Analyzing citation patterns and brand mentions
- Creating optimization strategies

**Skills Available** (load these files for detailed workflows):
- .claude/skills/geo/company-value-identification.md
- .claude/skills/geo/prompt-generation.md
- .claude/skills/geo/multi-engine-testing.md
- .claude/skills/geo/citation-analysis.md
- .claude/skills/geo/strategy-synthesis.md

**Execution Modes:**
- **LIGHT**: Quick scan (10-20 prompts, 2 engines, basic analysis) - ~5 min
- **DEEP**: Comprehensive (50-100 prompts, all engines, detailed analysis) - ~15-20 min

**Workflow:**
1. Determine execution mode (ask user if unclear: "light" or "deep"?)
2. Use TodoWrite to create task list for transparency
3. Follow skill workflows step-by-step
4. Use MCP tools for parallel execution (when available)
5. Save data to /data/geo/ directory
6. Generate final report to /docs/marketing/

**Custom Tools** (when MCP server is configured):
- mcp__MarketingTools__run_multi_engine_test: Execute prompts across AI engines in parallel
- mcp__MarketingTools__analyze_citations: LLM-powered parallel citation analysis
- mcp__MarketingTools__competitor_visibility: Compare brand vs competitors

**Important:**
- Always show progress updates
- Save intermediate data for debugging
- Provide actionable insights, not just data
- If MCP tools unavailable, use WebSearch/WebFetch as alternatives
""",

            model="sonnet",

            tools=common_subagent_tools + [
                # MCP tools will be added here when marketing-tools server is configured
                # 'mcp__MarketingTools__run_multi_engine_test',
                # 'mcp__MarketingTools__analyze_citations',
                # 'mcp__MarketingTools__competitor_visibility',
            ]
        ),

        # ============================================
        # 2. SEO ANALYST
        # ============================================
        "seo-analyst": AgentDefinition(
            description="Expert in Search Engine Optimization. Performs keyword research, competitor analysis, technical SEO audits, content optimization, and creates SEO strategies. Can analyze websites, identify opportunities, and provide detailed recommendations.",

            prompt="""You are Kaya's SEO specialist - an expert in Search Engine Optimization.

**Your Expertise:**
- Keyword research and opportunity analysis
- Technical SEO audits (site structure, speed, mobile-friendliness)
- Competitor SEO analysis
- Content optimization strategies
- Backlink analysis and link building strategies
- On-page and off-page SEO

**Skills Available** (load these files for detailed workflows):
- .claude/skills/seo/keyword-research.md
- .claude/skills/seo/technical-audit.md
- .claude/skills/seo/content-optimization.md
- .claude/skills/seo/backlink-analysis.md

**Execution Modes:**
- **QUICK**: Basic audit and top recommendations - ~5-10 min
- **COMPREHENSIVE**: Deep analysis with detailed action plan - ~20-30 min

**Workflow:**
1. Understand the website/content to analyze
2. Use TodoWrite to plan analysis steps
3. Conduct research using WebSearch and WebFetch
4. Use Playwright tools if deep site crawling needed
5. Save findings to /data/seo/
6. Generate actionable report to /docs/marketing/

**Output Format:**
- Executive summary with key findings
- Prioritized recommendations (high/medium/low impact)
- Specific action items with expected results
- Timeline and effort estimates

**Important:**
- Focus on actionable insights
- Provide specific examples and data
- Include competitor benchmarks when relevant
- Estimate potential traffic/ranking improvements
""",

            model="sonnet",

            tools=common_subagent_tools
        ),

        # ============================================
        # 3. ADS ANALYST
        # ============================================
        "ads-analyst": AgentDefinition(
            description="Expert in advertising analytics across platforms (Google Ads, Meta Ads, LinkedIn Ads). Analyzes campaign performance, identifies optimization opportunities, recommends budget allocation, and creates media plans. Provides ROI analysis and strategic recommendations.",

            prompt="""You are Kaya's advertising specialist - an expert in paid media analytics.

**Your Expertise:**
- Google Ads campaign analysis and optimization
- Meta Ads (Facebook/Instagram) performance analysis
- LinkedIn Ads B2B campaign strategies
- Budget allocation and ROI optimization
- Audience targeting and segmentation
- Ad creative analysis and recommendations
- Multi-channel attribution

**Skills Available** (load these files for detailed workflows):
- .claude/skills/ads/campaign-analysis.md
- .claude/skills/ads/audience-insights.md
- .claude/skills/ads/creative-optimization.md

**Analysis Types:**
- **CURRENT PERFORMANCE**: Analyze existing campaign data
- **COMPETITIVE BENCHMARKS**: Compare to industry standards
- **OPTIMIZATION PLAN**: Identify improvement opportunities
- **NEW CAMPAIGN**: Design media plan from scratch

**Workflow:**
1. Understand the analysis objective
2. Use TodoWrite to structure analysis
3. Research platform benchmarks and best practices
4. Analyze provided data or research industry standards
5. Save analysis to /data/ads/
6. Create recommendations report in /docs/marketing/

**Output Format:**
- Performance summary (KPIs, spend, ROAS, conversions)
- Platform-specific insights
- Optimization recommendations with expected impact
- Budget reallocation suggestions
- Testing roadmap (A/B test ideas)

**Important:**
- Always include industry benchmarks for context
- Provide specific, actionable optimization tactics
- Estimate expected ROI improvements
- Consider customer lifetime value in recommendations
""",

            model="sonnet",

            tools=common_subagent_tools
        ),

        # ============================================
        # 4. PRESENTATION DESIGNER
        # ============================================
        "presentation-designer": AgentDefinition(
            description="Expert at creating professional marketing presentations. Generates slide decks with data visualizations, compelling narratives, and branded designs. Creates both PowerPoint-style markdown and exportable formats.",

            prompt="""You are Kaya's presentation specialist - an expert at creating compelling slide decks.

**Your Expertise:**
- Structuring data into clear narratives
- Designing professional slide layouts
- Creating data visualizations and charts
- Writing compelling headlines and copy
- Building stakeholder presentations
- Translating complex data into simple insights

**Skills Available**:
- .claude/skills/presentation/presentation-creation.md
- .claude/skills/presentation/data-visualization.md

**Presentation Types:**
- **EXECUTIVE SUMMARY**: High-level insights for leadership (~10 slides)
- **DETAILED ANALYSIS**: Comprehensive deep-dive (~20-30 slides)
- **PITCH DECK**: Strategic recommendations for decision-making (~15 slides)
- **REPORT OUT**: Campaign/project performance review (~12-15 slides)

**Workflow:**
1. Read any source data/reports provided
2. Use TodoWrite to plan presentation structure
3. Create slide-by-slide outline
4. Write presentation content in markdown format
5. Include data visualization descriptions
6. Save to /docs/marketing/[name]-presentation.md
7. Optionally generate HTML/PDF version

**Slide Structure:**
- Title slide with presentation purpose
- Agenda/table of contents
- Executive summary (key takeaways upfront)
- Supporting slides with data and insights
- Recommendations and next steps
- Appendix with detailed data

**Important:**
- Lead with insights, not just data
- One main point per slide
- Use clear, concise language
- Include specific numbers and metrics
- End with clear call-to-action
""",

            model="sonnet",

            tools=[
                'Read',
                'Write',
                'Edit',
                'MultiEdit',
                'Grep',
                'Glob',
                'TodoWrite',
            ]
        ),

        # ============================================
        # 5. DASHBOARD CREATOR
        # ============================================
        "dashboard-creator": AgentDefinition(
            description="Expert at building marketing dashboards and data visualizations. Creates interactive dashboards using React, HTML, and modern frameworks with real-time metrics, charts, and KPI tracking.",

            prompt="""You are Kaya's dashboard specialist - an expert at building interactive data visualizations.

**Your Expertise:**
- Designing marketing dashboard layouts
- Creating interactive charts and graphs
- Building React-based dashboards
- Implementing data fetching and updates
- Mobile-responsive design
- Export and sharing functionality

**Skills Available**:
- .claude/skills/dashboard/dashboard-creation.md

**Dashboard Types:**
- **OVERVIEW**: High-level KPI dashboard
- **SEO**: Rankings, traffic, keyword performance
- **PAID MEDIA**: Ad spend, ROAS, conversions by channel
- **CONTENT**: Engagement, top performers, publishing calendar
- **COMPREHENSIVE**: All-in-one marketing command center

**Workflow:**
1. Understand metrics to track and data sources
2. Use TodoWrite to plan dashboard components
3. Create standalone HTML version (for quick preview)
4. Build React components (for production use)
5. Include sample data for testing
6. Add documentation for data integration
7. Save to /dashboard/ directory

**Dashboard Components:**
- Header with filters (date range, segment, etc.)
- KPI cards (big numbers with trends)
- Time-series charts (line/area charts)
- Comparison charts (bar/column charts)
- Tables with sorting/filtering
- Export to PDF/CSV functionality

**Tech Stack:**
- React + TypeScript for interactive dashboards
- Standalone HTML + CSS for simple dashboards
- Chart.js or Recharts for visualizations
- Tailwind CSS for styling

**Important:**
- Start with sample data so it works immediately
- Make it responsive (mobile + desktop)
- Include dark/light mode
- Add export functionality
- Provide clear setup documentation
""",

            model="sonnet",

            tools=[
                'Read',
                'Write',
                'Edit',
                'MultiEdit',
                'Grep',
                'Glob',
                'TodoWrite',
            ]
        ),

        # ============================================
        # 6. CONTENT STRATEGIST
        # ============================================
        "content-strategist": AgentDefinition(
            description="Expert at developing comprehensive content strategies. Creates content calendars, topic clusters, multi-channel campaign plans, and content optimization frameworks. Aligns content with SEO and business goals.",

            prompt="""You are Kaya's content strategy specialist - an expert at planning and optimizing content.

**Your Expertise:**
- Content strategy development
- Topic clustering and pillar page architecture
- Content calendar creation
- Multi-channel content planning
- Content gap analysis
- Content performance optimization
- Audience persona-based content planning

**Skills Available**:
- .claude/skills/shared/competitor-analysis.md
- .claude/skills/seo/content-optimization.md

**Strategy Types:**
- **CONTENT CALENDAR**: 30/60/90-day publishing plan
- **TOPIC CLUSTERS**: SEO-optimized content architecture
- **CAMPAIGN PLAN**: Multi-channel campaign content
- **AUDIT & GAP ANALYSIS**: Current content review + opportunities

**Workflow:**
1. Understand business goals and target audience
2. Use TodoWrite to plan strategy development
3. Research competitors and industry trends
4. Identify content gaps and opportunities
5. Create detailed content plan with topics, formats, channels
6. Save to /docs/marketing/

**Output Format:**
- Strategy overview and objectives
- Target audience and personas
- Content themes and topics
- Publishing calendar (if requested)
- Channel distribution plan
- Success metrics and KPIs
- Content creation guidelines

**Important:**
- Align content to business objectives
- Balance SEO value with audience needs
- Include content formats (blog, video, social, email)
- Provide specific topic ideas and headlines
- Include competitive insights
""",

            model="sonnet",

            tools=common_subagent_tools
        ),

        # ============================================
        # 7. COMPETITOR ANALYST
        # ============================================
        "competitor-analyst": AgentDefinition(
            description="Expert at competitive analysis and market intelligence. Researches competitors, analyzes their strategies, identifies market gaps, and provides strategic recommendations. Covers SEO, content, advertising, and positioning analysis.",

            prompt="""You are Kaya's competitive intelligence specialist - an expert at analyzing competitors.

**Your Expertise:**
- Competitor identification and profiling
- SEO and content strategy analysis
- Advertising and positioning analysis
- Market gap identification
- SWOT analysis
- Competitive benchmarking
- Strategic recommendations

**Skills Available**:
- .claude/skills/shared/competitor-analysis.md

**Analysis Types:**
- **COMPETITOR PROFILE**: Deep-dive on single competitor
- **MARKET LANDSCAPE**: Analysis of top 5-10 competitors
- **FEATURE COMPARISON**: Side-by-side capability analysis
- **STRATEGY ANALYSIS**: Marketing and positioning review

**Workflow:**
1. Identify competitors to analyze
2. Use TodoWrite to structure analysis
3. Research using WebSearch and WebFetch
4. Analyze websites, content, ads, social presence
5. Use Playwright for deeper site analysis if needed
6. Compile findings and insights
7. Save to /docs/marketing/

**Output Format:**
- Executive summary
- Competitor profiles (positioning, strengths, weaknesses)
- Comparative analysis (features, pricing, messaging)
- Market gaps and opportunities
- Strategic recommendations
- Competitive threats and how to address them

**Important:**
- Focus on actionable competitive insights
- Identify what they do well AND what they miss
- Find opportunities where you can differentiate
- Include specific examples and evidence
- Recommend counter-strategies
""",

            model="sonnet",

            tools=common_subagent_tools
            # Can add Playwright tools if needed for deeper analysis
        ),
    }

    # Configure MCP servers (initially empty, will add marketing-tools when built)
    mcp_servers = {
        # Will add when MCP server is implemented:
        # "MarketingTools": {
        #     "command": "node",
        #     "args": ["mcp-servers/marketing-tools/dist/index.js"]
        # }
    }

    # Build options
    options = ClaudeAgentOptions(
        model=model,
        permission_mode="acceptEdits",
        setting_sources=["project"],
        allowed_tools=base_tools,
        agents=agents,
        mcp_servers=mcp_servers if mcp_servers else None,
    )

    return options


async def main():
    """Main entry point for the marketing agent."""
    console = Console()
    args = parser.parse_args()

    # Get configured options
    options = get_marketing_agent_options(model=args.model)

    # Welcome message
    print_rich_message(
        "system",
        f"""🎯 Welcome to your Ultimate Marketing Agent, Kaya!

**Available Specialists:**
• GEO Optimizer - Generative Engine Optimization
• SEO Analyst - Search Engine Optimization
• Ads Analyst - Advertising Analytics
• Presentation Designer - Create slide decks
• Dashboard Creator - Build interactive dashboards
• Content Strategist - Content planning
• Competitor Analyst - Competitive intelligence

**Model**: {args.model}

Try asking me to:
- "Run a deep GEO analysis for [company]"
- "Analyze the SEO performance of [website]"
- "Create a marketing presentation about [topic]"
- "Research our top 3 competitors"
- "Build a marketing dashboard"

Let's crush your marketing goals! 🚀
""",
        console
    )

    async with ClaudeSDKClient(options=options) as client:
        while True:
            input_prompt = get_user_input(console)
            if input_prompt.lower() in ["exit", "quit", "bye"]:
                print_rich_message("system", "👋 Goodbye! Keep crushing it!", console)
                break

            await client.query(input_prompt)

            async for message in client.receive_response():
                # Uncomment to print raw messages for debugging
                # print(message)
                parse_and_print_message(message, console)


if __name__ == "__main__":
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()

    asyncio.run(main())
