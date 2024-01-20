import PropTypes from 'prop-types';
import MagnifyingGlassIcon from '@heroicons/react/24/solid/MagnifyingGlassIcon';
import {
    Avatar,
    Box,
    IconButton,
    Stack,
    SvgIcon,
    Tooltip,
} from '@mui/material';

const SIDE_NAV_WIDTH = 0;
const TOP_NAV_HEIGHT = 64;

const TopNav = (props) => {

    return (
        <>
            <Box
                component="header"
                sx={{
                    backdropFilter: 'blur(6px)',
                    position: 'sticky',
                    left: {
                        lg: `${SIDE_NAV_WIDTH}px`
                    },
                    top: 0,
                    width: {
                        lg: `calc(100% - ${SIDE_NAV_WIDTH}px)`
                    },
                    zIndex: 10
                }}
            >
                <Stack
                    alignItems="center"
                    direction="row"
                    justifyContent="space-between"
                    spacing={2}
                    sx={{
                        minHeight: TOP_NAV_HEIGHT,
                        px: 2
                    }}
                >
                    <Stack
                        alignItems="center"
                        direction="row"
                        spacing={2}
                    >
                        {/* <IconButton>
                            <SvgIcon fontSize="small">
                                <Bars3Icon />
                            </SvgIcon>
                        </IconButton> */}
                        <Tooltip title="Search">
                            <IconButton>
                                <SvgIcon fontSize="medium">
                                    <MagnifyingGlassIcon />
                                </SvgIcon>
                            </IconButton>
                        </Tooltip>
                    </Stack>
                    <Stack
                        alignItems="center"
                        direction="row"
                        spacing={2}
                    >
                        <Avatar
                            // onClick={accountPopover.handleOpen}
                            // ref={accountPopover.anchorRef}
                            sx={{
                                cursor: 'pointer',
                                height: 40,
                                width: 40
                            }}
                            src="/assets/avatars/avatar-anika-visser.png"
                        />
                    </Stack>
                </Stack>
            </Box>
        </>
    );
};

TopNav.propTypes = {
    onNavOpen: PropTypes.func
};

export default TopNav