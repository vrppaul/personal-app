export interface Period {
    uuid: string
    from_date: Date
    to_date: Date
    tasks_completed: number
    tasks_moved: number
    tasks_total: number
    period_type: number
}