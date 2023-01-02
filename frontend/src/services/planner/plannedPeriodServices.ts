import type { PaginatedPeriods } from '../../types/periods';
import { requests } from '../api';
import { API_ROUTES } from '../apiRoutes';

export const PeriodServices = {
    getPeriodsInRange: async (fromDate: string, toDate: string): Promise<PaginatedPeriods> => {
        return requests.get(`${API_ROUTES.planner.periods.base}/?from_date=${fromDate}&to_date=${toDate}`);
    },
};
