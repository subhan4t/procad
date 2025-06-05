// frontend/src/context/AuthContext.js
import { createContext } from 'react';

export const AuthContext = createContext({
  auth: {
    loggedIn: false,
    user: null,
    isAdmin: false,
  },
  setAuth: () => {},
});
