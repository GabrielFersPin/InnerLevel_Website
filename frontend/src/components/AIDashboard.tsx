import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
    Card,
    CardContent,
    Typography,
    Grid,
    CircularProgress,
    Alert,
    Button,
    TextField,
    Box,
    LinearProgress,
    List,
    ListItem,
    ListItemText,
    Divider,
} from '@mui/material';
import { useAuth } from '../contexts/AuthContext';

interface Task {
    task: string;
    motivation: string;
    difficulty: number;
    estimated_xp: number;
}

interface EmotionalAnalysis {
    pattern: string;
    recommendation: string;
    positive_days: number;
    challenge_days: number;
}

interface HabitAnalysis {
    success_rate: number;
    best_days: string;
    emotional_correlation: string;
    recommendation: string;
    streak_analysis: string;
}

interface GoalAnalysis {
    progress_percentage: number;
    estimated_completion: string;
    key_milestones: string[];
    risk_factors: string[];
    recommendations: string[];
    momentum_score: number;
}

interface ProgressPrediction {
    daily_predictions: any[];
    weekly_summary: string;
    confidence_score: number;
    recommended_actions: string[];
    potential_challenges: string[];
    success_probability: number;
}

const AIDashboard: React.FC = () => {
    const { token } = useAuth();
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const [task, setTask] = useState<Task | null>(null);
    const [emotionalAnalysis, setEmotionalAnalysis] = useState<EmotionalAnalysis | null>(null);
    const [habitAnalysis, setHabitAnalysis] = useState<HabitAnalysis | null>(null);
    const [goalAnalysis, setGoalAnalysis] = useState<GoalAnalysis | null>(null);
    const [progressPrediction, setProgressPrediction] = useState<ProgressPrediction | null>(null);

    const [challenge, setChallenge] = useState<string>('');
    const [emotionalState, setEmotionalState] = useState<string>('');
    const [energyLevel, setEnergyLevel] = useState<number>(5);

    const generateTask = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await axios.post(
                '/api/ai/generate-task',
                {
                    challenge,
                    emotional_state: emotionalState,
                    energy_level: energyLevel,
                },
                {
                    headers: { Authorization: `Bearer ${token}` },
                }
            );
            setTask(response.data);
        } catch (err) {
            setError('Failed to generate task');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const analyzeEmotions = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await axios.post(
                '/api/ai/analyze-emotions',
                {
                    emotional_logs: [], // Add your emotional logs here
                },
                {
                    headers: { Authorization: `Bearer ${token}` },
                }
            );
            setEmotionalAnalysis(response.data);
        } catch (err) {
            setError('Failed to analyze emotions');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const analyzeHabit = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await axios.post(
                '/api/ai/analyze-habit',
                {
                    habit_name: 'Daily coding practice',
                    completion_logs: [], // Add your completion logs here
                    emotional_logs: [], // Add your emotional logs here
                },
                {
                    headers: { Authorization: `Bearer ${token}` },
                }
            );
            setHabitAnalysis(response.data);
        } catch (err) {
            setError('Failed to analyze habit');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const analyzeGoal = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await axios.post(
                '/api/ai/analyze-goal',
                {
                    goal: challenge,
                    current_progress: {}, // Add your current progress here
                    historical_data: [], // Add your historical data here
                },
                {
                    headers: { Authorization: `Bearer ${token}` },
                }
            );
            setGoalAnalysis(response.data);
        } catch (err) {
            setError('Failed to analyze goal');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const predictProgress = async () => {
        try {
            setLoading(true);
            setError(null);
            const response = await axios.post(
                '/api/ai/predict-progress',
                {
                    goal: challenge,
                    current_state: {}, // Add your current state here
                    historical_data: [], // Add your historical data here
                },
                {
                    headers: { Authorization: `Bearer ${token}` },
                }
            );
            setProgressPrediction(response.data);
        } catch (err) {
            setError('Failed to predict progress');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box sx={{ p: 3 }}>
            <Typography variant="h4" gutterBottom>
                AI Assistant Dashboard
            </Typography>

            {error && (
                <Alert severity="error" sx={{ mb: 2 }}>
                    {error}
                </Alert>
            )}

            <Grid container spacing={3}>
                {/* Task Generation Section */}
                <Grid item xs={12} md={6}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                Generate Daily Task
                            </Typography>
                            <Box sx={{ mb: 2 }}>
                                <TextField
                                    fullWidth
                                    label="Your Challenge"
                                    value={challenge}
                                    onChange={(e) => setChallenge(e.target.value)}
                                    margin="normal"
                                />
                                <TextField
                                    fullWidth
                                    label="Emotional State"
                                    value={emotionalState}
                                    onChange={(e) => setEmotionalState(e.target.value)}
                                    margin="normal"
                                />
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Energy Level (1-10)"
                                    value={energyLevel}
                                    onChange={(e) => setEnergyLevel(Number(e.target.value))}
                                    margin="normal"
                                    inputProps={{ min: 1, max: 10 }}
                                />
                                <Button
                                    variant="contained"
                                    onClick={generateTask}
                                    disabled={loading}
                                    sx={{ mt: 2 }}
                                >
                                    Generate Task
                                </Button>
                            </Box>
                            {task && (
                                <Box>
                                    <Typography variant="subtitle1">
                                        Task: {task.task}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        Motivation: {task.motivation}
                                    </Typography>
                                    <Typography variant="body2">
                                        Difficulty: {task.difficulty}/5
                                    </Typography>
                                    <Typography variant="body2">
                                        XP: {task.estimated_xp}
                                    </Typography>
                                </Box>
                            )}
                        </CardContent>
                    </Card>
                </Grid>

                {/* Emotional Analysis Section */}
                <Grid item xs={12} md={6}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                Emotional Analysis
                            </Typography>
                            <Button
                                variant="contained"
                                onClick={analyzeEmotions}
                                disabled={loading}
                                sx={{ mb: 2 }}
                            >
                                Analyze Emotions
                            </Button>
                            {emotionalAnalysis && (
                                <Box>
                                    <Typography variant="subtitle1">
                                        Pattern: {emotionalAnalysis.pattern}
                                    </Typography>
                                    <Typography variant="body2">
                                        Recommendation: {emotionalAnalysis.recommendation}
                                    </Typography>
                                    <Typography variant="body2">
                                        Positive Days: {emotionalAnalysis.positive_days}
                                    </Typography>
                                    <Typography variant="body2">
                                        Challenge Days: {emotionalAnalysis.challenge_days}
                                    </Typography>
                                </Box>
                            )}
                        </CardContent>
                    </Card>
                </Grid>

                {/* Goal Analysis Section */}
                <Grid item xs={12}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                Goal Analysis
                            </Typography>
                            <Button
                                variant="contained"
                                onClick={analyzeGoal}
                                disabled={loading}
                                sx={{ mb: 2 }}
                            >
                                Analyze Goal
                            </Button>
                            {goalAnalysis && (
                                <Box>
                                    <LinearProgress
                                        variant="determinate"
                                        value={goalAnalysis.progress_percentage}
                                        sx={{ mb: 2 }}
                                    />
                                    <Typography variant="subtitle1">
                                        Progress: {goalAnalysis.progress_percentage}%
                                    </Typography>
                                    <Typography variant="body2">
                                        Estimated Completion: {goalAnalysis.estimated_completion}
                                    </Typography>
                                    <Typography variant="subtitle2" sx={{ mt: 2 }}>
                                        Key Milestones:
                                    </Typography>
                                    <List>
                                        {goalAnalysis.key_milestones.map((milestone, index) => (
                                            <ListItem key={index}>
                                                <ListItemText primary={milestone} />
                                            </ListItem>
                                        ))}
                                    </List>
                                    <Typography variant="subtitle2">
                                        Recommendations:
                                    </Typography>
                                    <List>
                                        {goalAnalysis.recommendations.map((rec, index) => (
                                            <ListItem key={index}>
                                                <ListItemText primary={rec} />
                                            </ListItem>
                                        ))}
                                    </List>
                                </Box>
                            )}
                        </CardContent>
                    </Card>
                </Grid>

                {/* Progress Prediction Section */}
                <Grid item xs={12}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                Weekly Progress Prediction
                            </Typography>
                            <Button
                                variant="contained"
                                onClick={predictProgress}
                                disabled={loading}
                                sx={{ mb: 2 }}
                            >
                                Predict Progress
                            </Button>
                            {progressPrediction && (
                                <Box>
                                    <Typography variant="subtitle1">
                                        Weekly Summary: {progressPrediction.weekly_summary}
                                    </Typography>
                                    <Typography variant="body2">
                                        Confidence Score: {progressPrediction.confidence_score}/10
                                    </Typography>
                                    <Typography variant="body2">
                                        Success Probability: {progressPrediction.success_probability}%
                                    </Typography>
                                    <Typography variant="subtitle2" sx={{ mt: 2 }}>
                                        Recommended Actions:
                                    </Typography>
                                    <List>
                                        {progressPrediction.recommended_actions.map((action, index) => (
                                            <ListItem key={index}>
                                                <ListItemText primary={action} />
                                            </ListItem>
                                        ))}
                                    </List>
                                </Box>
                            )}
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>

            {loading && (
                <Box sx={{ display: 'flex', justifyContent: 'center', mt: 3 }}>
                    <CircularProgress />
                </Box>
            )}
        </Box>
    );
};

export default AIDashboard; 