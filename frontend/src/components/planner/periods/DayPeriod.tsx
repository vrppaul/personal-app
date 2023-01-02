import type React from 'react';

interface DayPeriodProps {
    uuid: string;
    date: Date;
    tasksCompleted: number;
    tasksMoved: number;
    tasksTotal: number;
}

export const DayPeriod: React.FC<DayPeriodProps> = ({
    uuid,
    date,
    tasksCompleted,
    tasksMoved,
    tasksTotal,
}: DayPeriodProps) => {
    return (
        <li className="day-period">
            <span>{date.toString()}</span>
            <span>{tasksCompleted}</span>
            <span>{tasksMoved}</span>
            <span>{tasksTotal}</span>
        </li>
    );
};
