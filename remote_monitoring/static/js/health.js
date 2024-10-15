document.addEventListener('DOMContentLoaded', () => {
    const machines = document.querySelectorAll('.machine');

    machines.forEach(machine => {
        const status = machine.getAttribute('data-status');
        const statusCircle = machine.querySelector('.status-circle');

        if (status === 'healthy') {
            statusCircle.style.backgroundColor = 'green';
        } else if (status === 'unhealthy') {
            statusCircle.style.backgroundColor = 'red';
        }
    });
});