import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {

    activeUrl: SafeResourceUrl;
  
    predictions = [
      { key: 'revenue-invest', label: 'Revenue by Investment', url: 'http://127.0.0.1:5001' },
      { key: 'future-revenue', label: 'Future Revenue', url: 'http://127.0.0.1:5002' },
      { key: 'product-rec', label: 'Product Recommendation', url: 'http://127.0.0.1:5003' },
      { key: 'dpo', label: 'DPO Prediction', url: 'http://127.0.0.1:5004' },
      { key: 'dispute', label: 'Dispute Forecast', url: 'http://127.0.0.1:5005' }
    ];
  
    urls: { [key: string]: SafeResourceUrl } = {};
  
    constructor(private sanitizer: DomSanitizer) {
      this.urls['powerbi'] = this.sanitizer.bypassSecurityTrustResourceUrl(
        'https://app.powerbi.com/reportEmbed?reportId=396d13ff-8a85-4514-add2-8f822c233cca&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730'
      );
  
      this.predictions.forEach(pred => {
        this.urls[pred.key] = this.sanitizer.bypassSecurityTrustResourceUrl(pred.url);
      });
  
      this.activeUrl = this.urls['powerbi'];
    }
  
    setView(viewKey: string): void {
      this.activeUrl = this.urls[viewKey];
    }
  }
  