const PLANNER_BASE = 'planner';

const PERIODS_BASE = `${PLANNER_BASE}/periods`;
const PeriodRoutes = {
    base: PERIODS_BASE,
};

const PlannerRoutes = {
    periods: PeriodRoutes,
};

export const API_ROUTES = {
    planner: PlannerRoutes,
};
