export const useIsCollapsed = () => {
    const isCollapsed = useState<Boolean>(
        'collapseNavBar',
        () => true
    )

    const setIsCollapsed = () => {
        isCollapsed.value = !isCollapsed.value
    }

    return {
        isCollapsed,
        setIsCollapsed
    }
}