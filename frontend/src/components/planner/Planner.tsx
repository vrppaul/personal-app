import React, { useEffect, useState } from 'react';
import { startOfWeek, endOfWeek, format } from 'date-fns';
import type { PaginatedPeriods, Period } from '../../types/periods';
import { DayPeriod } from './periods/DayPeriod';
import { PeriodServices } from '../../services/planner/plannedPeriodServices';

export const Planner: React.FC = () => {
    const [periods, setPeriods] = useState<Period[]>([]);

    useEffect(() => {
        const today = new Date();
        const fromDate = format(startOfWeek(today), 'yyyy-MM-dd');
        const toDate = format(endOfWeek(today), 'yyyy-MM-dd');

        PeriodServices.getPeriodsInRange(fromDate, toDate).then((fetchedPeriods: PaginatedPeriods) =>
            setPeriods(fetchedPeriods.items),
        );
    }, []);

    return periods.map((period) => (
        <DayPeriod
            key={period.uuid}
            uuid={period.uuid}
            date={period.from_date}
            tasksCompleted={period.tasks_completed}
            tasksMoved={period.tasks_moved}
            tasksTotal={period.tasks_total}
        />
    ));
};
