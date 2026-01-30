package com.termux.app;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class BootReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (Intent.ACTION_BOOT_COMPLETED.equals(intent.getAction())) {
            Log.d("TermuxBoot", "Boot received, waking up ghost...");
            // This triggers the standard Termux background service
            TermuxService.onBoot(context);
        }
    }
}
