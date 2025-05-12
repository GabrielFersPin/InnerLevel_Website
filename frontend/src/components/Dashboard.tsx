import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

interface Task {
  id: number;
  name: string;
  points: number;
  category: string;
  status: string;
  due_date: string;
}

interface Habit {
  id: number;
  name: string;
  category: string;
  points: number;
}

interface Reward {
  id: number;
  name: string;
  description: string;
  points_required: number;
  category: string;
  redeemed: boolean;
}

const Dashboard: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [habits, setHabits] = useState<Habit[]>([]);
  const [rewards, setRewards] = useState<Reward[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          navigate('/login');
          return;
        }

        const config = {
          headers: { Authorization: `Bearer ${token}` }
        };

        const [tasksRes, habitsRes, rewardsRes] = await Promise.all([
          axios.get('http://localhost:8000/tasks/', config),
          axios.get('http://localhost:8000/habits/', config),
          axios.get('http://localhost:8000/rewards/', config)
        ]);

        setTasks(tasksRes.data);
        setHabits(habitsRes.data);
        setRewards(rewardsRes.data);
      } catch (error) {
        console.error('Error fetching data:', error);
        navigate('/login');
      }
    };

    fetchData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <div className="flex-shrink-0 flex items-center">
                <h1 className="text-xl font-bold text-indigo-600">InnerLevel</h1>
              </div>
            </div>
            <div className="flex items-center">
              <button
                onClick={handleLogout}
                className="ml-4 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {/* Tasks Section */}
            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="px-4 py-5 sm:p-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">Tasks</h3>
                <div className="mt-4 space-y-4">
                  {tasks.map((task) => (
                    <div
                      key={task.id}
                      className="flex items-center justify-between p-4 bg-gray-50 rounded-md"
                    >
                      <div>
                        <h4 className="text-sm font-medium text-gray-900">{task.name}</h4>
                        <p className="text-sm text-gray-500">{task.category}</p>
                      </div>
                      <span className="text-sm font-medium text-indigo-600">
                        {task.points} pts
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Habits Section */}
            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="px-4 py-5 sm:p-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">Habits</h3>
                <div className="mt-4 space-y-4">
                  {habits.map((habit) => (
                    <div
                      key={habit.id}
                      className="flex items-center justify-between p-4 bg-gray-50 rounded-md"
                    >
                      <div>
                        <h4 className="text-sm font-medium text-gray-900">{habit.name}</h4>
                        <p className="text-sm text-gray-500">{habit.category}</p>
                      </div>
                      <span className="text-sm font-medium text-indigo-600">
                        {habit.points} pts
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Rewards Section */}
            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="px-4 py-5 sm:p-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">Rewards</h3>
                <div className="mt-4 space-y-4">
                  {rewards.map((reward) => (
                    <div
                      key={reward.id}
                      className="flex items-center justify-between p-4 bg-gray-50 rounded-md"
                    >
                      <div>
                        <h4 className="text-sm font-medium text-gray-900">{reward.name}</h4>
                        <p className="text-sm text-gray-500">{reward.description}</p>
                      </div>
                      <span className="text-sm font-medium text-indigo-600">
                        {reward.points_required} pts
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard; 