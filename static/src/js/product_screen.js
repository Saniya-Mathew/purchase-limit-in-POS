/** @odoo-module **/
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { rpc } from "@web/core/network/rpc";


patch(PaymentScreen.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },
    async validateOrder(isForceValidate) {
        const currentOrder = this.pos.get_order()
        const client = currentOrder.get_partner();
        console.log(client.name)
        const totalAmount = this.currentOrder.get_total_with_tax();
        if (!client) {
        await this.env.services.dialog.add(AlertDialog, {
                title: 'Missing Customer',
                body: 'Please select a customer before making payment.',
            });
            return;
        }
        var purchaseLimit = client.amount || 0;
        if ( purchaseLimit < totalAmount) {
        await this.env.services.dialog.add(AlertDialog, {
                title: 'Limit is reached',
                body: 'Operation cannot be completed!.     Purchase limit of the customer is ' + purchaseLimit,
            });
            return;
        }
        const balance_amount = purchaseLimit - totalAmount
        await rpc("/pos/update_purchase_limit_limit", {
                partner_id: client.id,
                balance_amount: balance_amount
        });
        return super.validateOrder(isForceValidate);
    }
});
