import Cookies from 'js-cookie';
import axios, { AxiosResponse, Method } from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000/api',
    headers: {
        'Content-type': 'application/json',
    },
    // Timeout 10 seconds should be more than reasonable
    timeout: 10000,
});
instance.interceptors.request.use((config) => {
    const changedConfig = config;
    if (changedConfig.headers === undefined) changedConfig.headers = {};
    changedConfig.headers['X-CSRFTOKEN'] = Cookies.get('csrftoken') || '';
    return changedConfig;
});

const getResponseBody = <R>(response: AxiosResponse<R>): R => response.data;

export const requests = {
    get: async <R>(url: string): Promise<R> => {
        return instance.get(url).then(getResponseBody);
    },
    post: async <T, R>(url: string, body?: T): Promise<R> => {
        return instance.post<T, AxiosResponse<R>>(url, body).then<R>(getResponseBody);
    },
    put: async <T, R>(url: string, body: T): Promise<R> => {
        return instance.put<T, AxiosResponse<R>>(url, body).then(getResponseBody);
    },
    patch: async <T, R>(url: string, body: T): Promise<R> => {
        return instance.patch<T, AxiosResponse<R>>(url, body).then(getResponseBody);
    },
    delete: async <R>(url: string): Promise<R> => {
        return instance.delete(url).then(getResponseBody);
    },
    customRequest: async <T, R>(method: Method, url: string, body: T, headers: Record<string, string>): Promise<R> => {
        return instance(url, { method, data: body, headers }).then(getResponseBody);
    },
};
