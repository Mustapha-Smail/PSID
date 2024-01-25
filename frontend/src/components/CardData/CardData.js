import { Avatar, Card, CardContent, SvgIcon, Tooltip, Typography } from '@mui/material'
import { Stack } from '@mui/system'
import React from 'react'

const CardData = ({ title, value, children }) => {

    const convertNumber = (value) => {
        const num = parseInt(value)
        if (num >= 1e9) {
            return (num / 1e9).toFixed(1) + 'B';
        } else if (num >= 1e6) {
            return (num / 1e6).toFixed(1) + 'M';
        } else if (num >= 1e3) {
            return (num / 1e3).toFixed(1) + 'K';
        } else {
            return value;
        }
    }
    return (
        <Card sx={{ borderRadius: '20px', height: '100%', margin: '0 0.3rem' }}>
            <CardContent>
                <Stack
                    alignItems="flex-start"
                    direction="row"
                    justifyContent="space-between"
                    spacing={3}
                >
                    <Stack spacing={1}>
                        <Typography
                            color="text.secondary"
                            variant="overline"
                        >
                            {title}
                        </Typography>
                        <Tooltip title={value}>
                            <Stack direction={'row'} spacing={1} alignItems="center" justifyContent="space-between">
                                <Typography variant="h4" sx={{ overflow: 'scroll' }}>
                                    {convertNumber(value)}
                                </Typography>
                                <Avatar
                                    sx={{
                                        backgroundColor: 'error.main',
                                        height: 42,
                                        width: 42
                                    }}
                                >
                                    <SvgIcon>
                                        {children}
                                    </SvgIcon>
                                </Avatar>
                            </Stack>
                        </Tooltip>
                    </Stack>
                </Stack>
            </CardContent>
        </Card>
    )
}

export default CardData