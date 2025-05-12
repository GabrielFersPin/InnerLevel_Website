import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import taskReducer from './slices/taskSlice';
import habitReducer from './slices/habitSlice';
import rewardReducer from './slices/rewardSlice';

const store = configureStore({
  reducer: {
    auth: authReducer,
    tasks: taskReducer,
    habits: habitReducer,
    rewards: rewardReducer,
  },
});

export default store; 