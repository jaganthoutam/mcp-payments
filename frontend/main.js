async function rpcCall(token, name, params) {
    const response = await fetch('/rpc', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ jsonrpc: '2.0', id: Date.now(), method: 'tools/call', params: { name, arguments: params } })
    });
    if (!response.ok) {
        const text = await response.text();
        throw new Error(text);
    }
    return await response.json();
}

document.getElementById('createPaymentForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const token = document.getElementById('token').value;
    const formData = new FormData(e.target);
    const params = Object.fromEntries(formData.entries());
    try {
        const result = await rpcCall(token, 'create_payment', params);
        document.getElementById('createPaymentResult').textContent = JSON.stringify(result, null, 2);
    } catch (err) {
        document.getElementById('createPaymentResult').textContent = err;
    }
});

document.getElementById('walletBalanceBtn').addEventListener('click', async () => {
    const token = document.getElementById('token').value;
    try {
        const result = await rpcCall(token, 'get_wallet_balance', {});
        document.getElementById('walletBalanceResult').textContent = JSON.stringify(result, null, 2);
    } catch (err) {
        document.getElementById('walletBalanceResult').textContent = err;
    }
});
